from galaxycloudrunner.runners.cl_pulsar_burst import get_destination


def cloudlaunch_pulsar_burst(app, cloudlaunch_api_endpoint=None,
                             cloudlaunch_api_token=None,
                             fallback_destination_id=None):
    return get_destination(app, cloudlaunch_api_endpoint,
                           cloudlaunch_api_token, fallback_destination_id)
