import os

import cachetools

from cloudlaunch_cli.api.client import APIClient


# Global variable for tracking round-robin index
current_server_index = 0


def _get_cloudlaunch_client():
    # Obtain from app.config later
    cloudlaunch_url = os.environ.get(
        'CLOUDLAUNCH_API_ENDPOINT',
        'https://launch.usegalaxy.org/cloudlaunch/api/v1')
    cloudlaunch_token = os.environ.get('CLOUDLAUNCH_API_TOKEN')
    return APIClient(cloudlaunch_url, token=cloudlaunch_token)


@cachetools.cached(cachetools.TTLCache(maxsize=1, ttl=300))
def _get_pulsar_servers():
    """
    Return an array of tuples, consisting of the Pulsar url and auth token.
    """
    client = _get_cloudlaunch_client()
    server_list = []
    # List servers sorted from oldest to newest, so that newly added servers
    # will be used before round-robin wrap around
    print("Getting a new list of deploys")
    for deployment in client.deployments.list(
            application='pulsar-standalone', version='0.1',
            archived=False, status='SUCCESS', ordering='added'):
        launch_data = deployment.launch_task.result.get('pulsar', {})
        if launch_data and launch_data.get('api_url'):
            server_list.append(
                (launch_data.get('api_url'), launch_data.get('auth_token')))
    return server_list


def get_next_server():
    """
    Round-robin implementation for returning next available job server.

    For the time being, this will always be a Pulsar server.

    :rtype: ``dict``
    :return: A dictionary with the following keys:
        - 'runner' (currently always pulsar)
        - 'url': string representing the runner endpoint
        - 'auth_token': auth token used to communicate with the supplied server
    """
    server = {'runner': 'pulsar',
              'url': None,
              'auth_token': None}
    global current_server_index
    servers = _get_pulsar_servers()
    if current_server_index >= len(servers):
        current_server_index = 0
    if servers:
        next_server = servers[current_server_index]
        current_server_index += 1
        server['url'] = next_server[0]
        server['auth_token'] = next_server[1]
    return server
