"""
This is a legacy layer for Galaxy versions prior to 19.01
as they do not support chaining dynamic rules. This provides a single
rule that simulates the chaining of burst, to_destination_if_size
and cloudlaunch_pulsar_burst rules.
"""
from galaxy.jobs.stock_rules import burst
from galaxy.util import asbool
from galaxycloudrunner.runners.cl_pulsar_burst import get_destination
from .helper_rules import to_destination_if_size


def cloudlaunch_pulsar_burst_compat(
        app, rule_helper, job,
        cloudlaunch_api_endpoint=None, cloudlaunch_api_token=None,
        pulsar_runner_id=None,
        pulsar_fallback_destination_id=None,
        burst_enabled=None,
        burst_from_destination_ids=None,
        burst_num_jobs=None,
        burst_job_states=None,
        dest_if_size_enabled=None,
        dest_if_size_max_size=None,
        dest_if_size_fallback_destination_id=None):
    burst_enabled = asbool(burst_enabled)
    dest_if_size_enabled = asbool(dest_if_size_enabled)
    destination = None
    if burst_enabled:
        destination = burst(
            rule_helper, job, burst_from_destination_ids,
            "dest_if_size" if dest_if_size_enabled else "galaxycloudrunner",
            burst_num_jobs, job_states=burst_job_states)
    if (destination and destination not in
            ["dest_if_size", "galaxycloudrunner"]):
        # Not a destination we know, just return
        return destination
    if destination == "dest_if_size" or dest_if_size_enabled:
        destination = to_destination_if_size(
            job, dest_if_size_max_size,
            "galaxycloudrunner",
            dest_if_size_fallback_destination_id)
    if (destination and destination not in ["galaxycloudrunner"]):
        # Not a destination we know, just return
        return destination

    return get_destination(app, None,
                           cloudlaunch_api_endpoint,
                           cloudlaunch_api_token,
                           pulsar_runner_id,
                           pulsar_fallback_destination_id)
