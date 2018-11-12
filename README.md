[![Documentation Status](https://readthedocs.org/projects/galaxycloudrunner/badge/?version=latest)](http://galaxycloudrunner.readthedocs.org/en/latest/?badge=latest)

GalaxyCloudRunner enables bursting of user jobs to remote compute resources for
the [Galaxy application](https://galaxyproject.org/). It provides a dynamic job
runner that can be plugged into Galaxy.

## Overview

GalaxyCloudRunner enables bursting of user jobs to remote compute
resources for the [Galaxy application](https://galaxyproject.org/).
It provides several dynamic job rules that can be plugged into Galaxy,
enabling Galaxy to submit jobs to remote cloud nodes.

## How it works

The GalaxyCloudRunner provides a library of rules that can be plugged
into Galaxy through `job_conf.xml`. Once configured, you can get your
jobs to be automatically routed to remote Pulsar nodes running on the
cloud. The GalaxyCloudRunner will discover what Pulsar nodes are
available by querying the [CloudLaunch](https://launch.usegalaxy.org/) API.
Adding a new node is a simple matter of visiting the
[CloudLaunch](https://launch.usegalaxy.org/) site and launching a new
Pulsar node on your desired cloud.

## Getting Started

Getting started with the GalaxyCloudRunner is a simple process.

1.  First, install galaxycloudrunner into your Galaxy's virtual
    environment.
2.  Add a job rule to Galaxy which will determine the Pulsar node to
    route to.
3.  Configure your job\_conf.xml to use this rule.
4.  Launch as many Pulsar nodes as you need through
    [CloudLaunch](https://launch.usegalaxy.org/).
5.  Submit your jobs as usual.

For detailed instructions, see:
[https://galaxycloudrunner.readthedocs.io/](https://galaxycloudrunner.readthedocs.io/)

## Contributing
Community contributions for any part of the project are welcome. If you have
a completely new idea or would like to bounce your idea before moving forward
with the implementation, feel free to create an issue to start a discussion.

Contributions should come in the form of a pull request. The code needs to be
well documented and all methods have docstrings. We are largely adhering to the
[PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) with 80 character
lines, 4-space indentation (spaces instead of tabs), explicit, one-per-line
imports among others. Please keep the style consistent with the rest of the
project.
