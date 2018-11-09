GalaxyCloudRunner enables bursting of user jobs to remote compute resources for
the [Galaxy application](https://galaxyproject.org/). It provides a dynamic job
runner that can be plugged into Galaxy.

## Overview

## Installation and Setup
Clone and install the repository to your local machine. As always, use of
virutalenv is encouraged.
```
git clone https://github.com/CloudVE/galaxycloudrunner.git
cd galaxycloudrunner
python setup.py install
```

For the time being, it is also necessary to install an updated version of the
CloudLaunch-CLI library from its repository:
```
pip install -U git+https://github.com/CloudVE/cloudlaunch-cli.git
```

## Usage
Take a look at `docs/cloud_burst.py` file for an example of a Galaxy dynamic
job runner and `docs/job_conf.xml` for an example of Galaxy job config on how
to enable GalaxyCloudRunner in your Galaxy.

If wanting to test the library interactively, try the following. You can obtain
your CloudLaunch API key from the credentials page on the CloudLaunch server.
```
$ export CLOUDLAUNCH_API_ENDPOINT="https://launch.usegalaxy.org/cloudlaunch/api/v1"
$ export CLOUDLAUNCH_API_TOKEN="hre9ufhaijs9cjasdoicmsnad"
$ python
>>> from galaxycloudrunner.server import get_next_server
>>> get_next_server()
```

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
