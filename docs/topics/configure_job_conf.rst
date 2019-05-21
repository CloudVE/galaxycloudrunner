Job configuration for Galaxy 19.01 or higher
==============================================

Simple configuration
--------------------

The following is a simple job configuration sample that you can use to get
started.

.. literalinclude:: ../samples/job_conf.xml.basic
   :language: xml
   :linenos:
   :emphasize-lines: 7,9-22

In this simple configuration, all jobs are routed to GalaxyCloudRunner by
default. This works as follows:

1. If a Pulsar node is available, it will return that node.
2. If multiple Pulsar nodes are available, they will be returned in a
   round-robin loop.
3. You can add or remove Pulsar nodes at any time. However, there's a caching
   period (currently 5 minutes) to avoid repeatedly querying the server, which
   will result in a short period of time before the change is detected by
   the GalaxyCloudRunner. This has implications for node addition and in
   particular removal. When adding a node, there could be a delay of a few
   minutes before the node is picked up. If a Pulsar node is removed, your jobs
   may be routed to a dead node for the duration of the caching period.
   Therefore, we recommend attempting a job resubmission through the resubmit
   tag as shown in the example. See :ref:`additional-configuration` on how to
   change this cache period.
4. If no node is available, it will return the ``fallback_destination_id``, if
   specified, in which case the job will be routed there. If no
   ``fallback_destination_id`` is specified, the job will be re-queued till a node
   becomes available.


To burst or not to burst?
-------------------------

In the above example, all jobs are routed to the GalaxyCloudRunner by default.
However, it is often the case that jobs should be routed to the remote cloud
nodes only if the local queue is full. To support this scenario, we recommend
a configuration like the following.


.. literalinclude:: ../samples/job_conf.xml.burst_if_queued
   :language: xml
   :linenos:
   :emphasize-lines: 8,10-16

Note the emphasized lines. In this example, we route to the built-in rule
``burst_if_queued`` first, which determines whether or not the cloud bursting
should occur. It examines how many jobs in the
``from_destination_ids`` are in the given state (``queued`` in this case),
and if there are above ``num_jobs``, routes to the
to the ``to_destination_id`` destination (``galaxycloudrunner`` in this case).
If bursting should not occur, it routes
to the first destination in the ``from_destination_ids`` list. This provides a
simple method to scale to Pulsar nodes only if a desired queue has a backlog
of jobs. You may need to experiment with these values to find ones that work
best for your requirements.

Advanced bursting
-----------------

In this final example, we show how a complex chain of rules can be used to
exert fine-grained control over the job routing process.

.. literalinclude:: ../samples/job_conf.xml.burst_if_size
   :language: xml
   :linenos:
   :emphasize-lines: 17-24

Jobs are first routed to the built-in ``burst_if_queued`` rule, which determines
whether the bursting should occur. If it should, it is then routed to the
``burst_if_size`` destination, which will check the total size of the input
files. If they are less than 1GB, they are routed to the ``galaxycloudrRunner``
destination. If not, they are routed to a local queue.


Job configuration for Galaxy versions lower than 19.01
========================================================

Simple configuration
--------------------

The following is a simple job configuration sample that you can use to get
started.

.. literalinclude:: ../samples/job_conf.xml.legacy.basic
   :language: xml
   :linenos:
   :emphasize-lines: 7,9-19

In this simple configuration, all jobs are routed to GalaxyCloudRunner by
default. This works as follows:

1. If a Pulsar node is available, it will return that node.
2. If multiple Pulsar nodes are available, they will be returned in a
   round-robin loop.
3. You can add or remove Pulsar nodes at any time. However, there's a caching
   period (currently 5 minutes) to avoid repeatedly querying the server, that
   will result in a short period of time before the change is detected by
   the GalaxyCloudRunner. This has implications for node addition and in
   particular removal. When adding a node, there could be a delay of a few
   minutes before the node is picked up. If a Pulsar node is removed, your jobs
   may be routed to a dead node for the duration of the caching period.
   Therefore, we recommend a job resubmission through a resubmit tag. However,
   Galaxy versions prior to 19.01 do not support resubmissions for Pulsar, and
   you may need to change the cache period to zero to handle this scenario. See
   :ref:`additional-configuration` on how to change this cache period.
4. If no node is available, it will return the ``fallback_destination_id``, if
   specified, in which case the job will be routed there. If no
   ``fallback_destination_id`` is specified, the job will be re-queued till a node
   becomes available.

Note that you must manually add the galaxy rule as described here: :ref:`galaxy_configuration_legacy`

To burst or not to burst?
-------------------------

In the above example, all jobs are routed to the GalaxyCloudRunner by default.
However, it is often the case that jobs should be routed to the remote cloud
nodes only if the local queue is full. To support this scenario, we recommend
a configuration like the following.


.. literalinclude:: ../samples/job_conf.xml.legacy.burst_if_queued
   :language: xml
   :linenos:
   :emphasize-lines: 20-23

Galaxy versions prior to 19.01 do not support chaining dynamic rules, and
therefore, we have provided a single monolithic rule that can handle both
scenarios.

Note the ``burst_enabled`` flag, which will activate the bursting rule.
This rule will determine whether or not the cloud bursting
should occur. It examines how many jobs in the
``burst_from_destinations`` are in the given state (``queued`` in this case),
and bursts to pulsar only if they are above ``burst_num_jobs``. If bursting
should not occur, it routes to the first destination in the
``from_destinations`` list. This provides a simple method to scale to Pulsar
nodes only if a desired queue has a backlog of jobs. You may need to
experiment with these values to find ones that work best for your requirements.

Advanced bursting
-----------------

In this final example, we expand this compound rule to also filter jobs by size.

.. literalinclude:: ../samples/job_conf.xml.legacy.burst_if_size
   :language: xml
   :linenos:
   :emphasize-lines: 24-26

Enable the ``dest_if_size_enabled`` flag as highlighted to filter by size.
This will make sure that the job is routed to Pulsar only if the total size of
the input files are less than 1GB. If not, they are routed to
``dest_if_size_fallback_destination_id``, which in this case, is a local queue.



.. _https://launch.usegalaxy.org/: https://launch.usegalaxy.org/
.. _CloudLaunch: https://launch.usegalaxy.org/
