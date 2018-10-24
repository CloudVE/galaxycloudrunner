from cloudfling.server import get_next_server

from galaxy.jobs import JobDestination


def cloudfling_runner(app):
    next_server = get_next_server()
    if next_server.get('url'):
        return JobDestination(
            runner=next_server.get('runner'),
            params={"url": next_server.get('url'),
                    "private_token": next_server.get('auth_token')})
    return None  # Requires https://github.com/galaxyproject/galaxy/pull/6920
