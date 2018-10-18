from galaxy.jobs import JobDestination
import os

def remote_pulsar_runner(job):
    token = "this"
    return JobDestination(runner="pulsar", params={"url": "http://127.0.0.1:8913", "private_token": token})
