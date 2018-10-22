import os

from galaxy.jobs import JobDestination

from cloudlaunch_cli.api.client import APIClient


# Global variable for tracking round-robin index
current_server_index = 0


def _get_cloudlaunch_client(app):
    # Obtain from app.config later
    cloudlaunch_url = os.environ.get('CLOUDLAUNCH_API_ENDPOINT',
                                     'http://localhost:8000/api/v1')
    cloudlaunch_token = os.environ.get('CLOUDLAUNCH_API_TOKEN')
    return APIClient(cloudlaunch_url, token=cloudlaunch_token)


def _get_pulsar_servers(app):
    """
    Returns an array of tuples, consisting of the pulsar url and auth token

    TODO: Add a caching implementation so that the API is not repeatedly
    queried on each job dispatch
    """
    client = _get_cloudlaunch_client(app)
    server_list = []
    # TODO: Filter deployments by app name
    for deployment in client.deployments.list():
        launch_data = deployment.launch_task.result.get('pulsar', {})
        # TODO: Remove this if when filtering implemented
        if (not deployment.archived and
                launch_data and launch_data.get('api_url') and
                # Filter only running instances: temp solution as this may not
                # work if the user closes the browser before health check runs
                deployment.latest_task.result.get('instance_status', '') ==
                'running'):
            server_list.append(
                (launch_data.get('api_url'), launch_data.get('auth_token')))
    return server_list


def _get_next_pulsar_server(app):
    """
    Round-robin implementation for returning next available pulsar server
    """
    global current_server_index
    servers = _get_pulsar_servers(app)
    if current_server_index >= len(servers):
        current_server_index = 0
    if servers:
        next_server = servers[current_server_index]
        current_server_index += 1
        return next_server
    return None, None


def remote_pulsar_runner(app):
    url, token = _get_next_pulsar_server(app)
    return JobDestination(runner="pulsar",
                          params={"url": url, "private_token": token})
