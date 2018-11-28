import os

import cachetools

from cloudlaunch_cli.api.client import APIClient
from galaxy.jobs import JobDestination
from galaxy.jobs.mapper import JobNotReadyException


CACHE_TIMEOUT = os.environ.get('CLOUDLAUNCH_QUERY_CACHE_PERIOD', 300)

# Global variable for tracking round-robin index
current_server_index = 0


def _get_cloudlaunch_client(cloudlaunch_api_endpoint, cloudlaunch_api_token):
    # Obtain from app.config later
    cloudlaunch_url = cloudlaunch_api_endpoint or os.environ.get(
        'CLOUDLAUNCH_API_ENDPOINT',
        'https://launch.usegalaxy.org/cloudlaunch/api/v1')
    cloudlaunch_token = cloudlaunch_api_token or os.environ.get(
        'CLOUDLAUNCH_API_TOKEN')
    return APIClient(cloudlaunch_url, token=cloudlaunch_token)


# Key function hashes args to a constant value since we allow only one item
@cachetools.cached(cachetools.TTLCache(maxsize=1, ttl=CACHE_TIMEOUT),
                   key=lambda *_, **__: 'hash_to_constant')
def _get_pulsar_servers(cloudlaunch_client):
    """
    Return an array of tuples, consisting of the Pulsar url and auth token.
    """
    server_list = []
    # List servers sorted from oldest to newest, so that newly added servers
    # will be used before round-robin wrap around
    for deployment in cloudlaunch_client.deployments.list(
            application='pulsar-standalone', version='0.1',
            archived=False, status='SUCCESS', ordering='added'):
        launch_data = deployment.launch_task.result.get('pulsar', {})
        if launch_data and launch_data.get('api_url'):
            server_list.append(
                (launch_data.get('api_url'), launch_data.get('auth_token')))
    return server_list


def get_next_server(cloudlaunch_api_endpoint, cloudlaunch_api_token):
    """
    Round-robin implementation for returning next available job server.

    For the time being, this will always be a Pulsar server.

    :rtype: ``tuple``
    :return: A tuple with the following values:
        - 'url': string representing the runner endpoint
        - 'auth_token': auth token used to communicate with the supplied server
    """
    global current_server_index
    client = _get_cloudlaunch_client(cloudlaunch_api_endpoint,
                                     cloudlaunch_api_token)
    servers = _get_pulsar_servers(client)
    if current_server_index >= len(servers):
        current_server_index = 0
    if servers:
        url, token = servers[current_server_index]
        current_server_index += 1
        return url, token
    return None, None


def get_destination(app, referrer=None,
                    cloudlaunch_api_endpoint=None,
                    cloudlaunch_api_token=None,
                    pulsar_runner_id="pulsar",
                    fallback_destination_id=None):
    """
    Returns an available Pulsar JobDestination by querying
    cloudlaunch. If no Pulsar server is available, returns
    a fallback destination (if specified by the user) or
    raises a JobNotReadyException, so that the job will be
    rescheduled.
    """
    url, token = get_next_server(cloudlaunch_api_endpoint,
                                 cloudlaunch_api_token)
    if url:
        if referrer:
            resubmit_dest = referrer.get('resubmit')
        return JobDestination(runner=pulsar_runner_id,
                              params={"url": url,
                                      "private_token": token
                                      },
                              resubmit=resubmit_dest)
    elif fallback_destination_id:
        return fallback_destination_id
    else:
        raise JobNotReadyException  # This will attempt to reschedule the job
