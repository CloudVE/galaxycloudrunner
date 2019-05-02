.. GalaxyCloudRunner documentation master file, created by
   sphinx-quickstart on Sat Nov 10 18:16:35 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GalaxyCloudRunner's documentation!
=============================================

GalaxyCloudRunner enables bursting of user jobs to remote compute resources for
the `Galaxy application`_. It provides several dynamic
job rules that can be plugged into Galaxy, enabling Galaxy to submit jobs to
remote cloud nodes.

How it works
------------
The GalaxyCloudRunner provides a library of rules that can be plugged into Galaxy
through ``job_conf.xml``. Once configured, you can get your jobs to be automatically
routed to remote Pulsar nodes running on the cloud. The GalaxyCloudRunner will discover
what Pulsar nodes are available by querying the `CloudLaunch`_ API.
Adding a new node is a simple matter of visiting the `CloudLaunch`_ site and launching
a new Pulsar node on your desired cloud.


Getting Started
---------------
Getting started with the GalaxyCloudRunner is a simple process.

1. First, install ``galaxycloudrunner`` library into your Galaxy's virtual environment
2. Add a job rule to Galaxy which will determine the Pulsar node to route to
3. Configure Galaxy's ``job_conf.xml`` file to use this rule
4. Launch as many Pulsar nodes as you need through `CloudLaunch`_
5. Submit jobs as usual


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   topics/configure_galaxy.rst
   topics/cloudlaunch_api_key.rst
   topics/add_pulsar_node.rst
   topics/configure_job_conf.rst
   topics/additional_notes.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Galaxy application: https://galaxyproject.org/
.. _CloudLaunch: https://launch.usegalaxy.org/
