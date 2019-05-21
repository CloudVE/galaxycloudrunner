GalaxyCloudRunner: job bursting for Galaxy
==========================================

GalaxyCloudRunner enables bursting of user jobs to remote compute resources for
the `Galaxy application`_. It provides several dynamic job rules that can be
plugged into Galaxy, enabling Galaxy to submit jobs to remote compute nodes.

How it works
------------
The GalaxyCloudRunner provides a library of rules that can be plugged into
Galaxy through its configuration via ``job_conf.xml``. Once configured, Galaxy
jobs can be automatically routed to a Galaxy remote job runner, called
`Pulsar`_, on nodes running on the cloud. Adding a new node is a simple matter
of visiting the `CloudLaunch`_ site and launching a new worker node on your
desired cloud. The GalaxyCloudRunner will discover what Pulsar nodes are
available by querying the `CloudLaunch`_ API.


Getting Started
---------------
Getting started with the GalaxyCloudRunner is a simple process.

1. First, install ``galaxycloudrunner`` library into your Galaxy's virtual environment
2. Configure Galaxy to use GalaxyCloudRunner job destination rules
3. Launch as many worker nodes as you need through `CloudLaunch`_
4. Submit jobs as usual


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
.. _Pulsar: https://pulsar.readthedocs.io/en/latest/
.. _CloudLaunch: https://launch.usegalaxy.org/
