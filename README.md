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
    environment via `pip install galaxycloudrunner`.
2.  Add a job rule to Galaxy which will determine the Pulsar node to
    route to.
3.  Configure your `job_conf.xml` to use this rule.
4.  Launch as many Pulsar nodes as you need through
    [CloudLaunch](https://launch.usegalaxy.org/).
5.  Submit jobs as usual.

For detailed instructions, see:
[https://galaxycloudrunner.readthedocs.io/](https://galaxycloudrunner.readthedocs.io/)

## Developer installation

Clone the source code repository and install the library with the dev
dependencies.

```
git clone https://github.com/CloudVE/galaxycloudrunner.git
cd galaxycloudrunner
pip install --upgrade .[dev]
```

To build the HTML docs locally, run the following commands. The built site will
be available in `docs/_build/html`.

```
cd docs
make html
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


## Release process
1. Update any dependencies in `setup.py` and commit the changes.
2. Increment the library version number in `galaxycloudrunner/__init__.py` as
   per [semver rules](https://semver.org/).
3. Add release notes to `CHANGELOG.rst`, adding the most recent commit hash to
   the changelog, and make a commit. List of commits can be obtained using
   `git shortlog <last release hash>..HEAD`
4. Test the release with PyPI staging server, as described in
   https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
   You will need to `pip install -U wheel twine` for this step.
5. Release to PyPI
   ```
   # Remove stale files or wheel might package them
   rm -r build dist
   python setup.py sdist bdist_wheel
   twine upload -r pypi dist/galaxycloudrunner-*
   ```
6. Tag release and make a GitHub release. Alternatively, push the current
   commits and make a release directly on GitHub to include the release
   changelog in the tag body.
   ```
   git tag -a v0.3.0 -m "Release 0.3.0"
   git push
   git push --tags
   ```
7. Increment version number in `galaxycloudrunner/__init__.py` to
   `<current-version>+dev` to indicate the development cycle; commit, and push
   the changes.
