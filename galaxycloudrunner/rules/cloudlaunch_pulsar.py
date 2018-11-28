from galaxycloudrunner.runners.cl_pulsar_burst import get_destination


def cloudlaunch_pulsar_burst(app, referrer,
                             cloudlaunch_api_endpoint=None,
                             cloudlaunch_api_token=None,
                             pulsar_runner_id="pulsar",
                             fallback_destination_id=None):
    return get_destination(app, referrer,
                           cloudlaunch_api_endpoint,
                           cloudlaunch_api_token,
                           pulsar_runner_id,
                           fallback_destination_id)
