from galaxycloudrunner.server import get_next_server

from galaxy.jobs import JobDestination
from galaxy.jobs.mapper import JobNotReadyException


def galaxycloudrunner(app):
    next_server = get_next_server()
    if next_server.get('url'):
        return JobDestination(
            runner=next_server.get('runner'),
            params={"url": next_server.get('url'),
                    "private_token": next_server.get('auth_token')})
    return JobNotReadyException  # This will attempt to reschedule the job
