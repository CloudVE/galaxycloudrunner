.. _additional-configuration:

Additional Configuration and Limitations
----------------------------------------

1. Configuring the query timeout

   You can set the environment variable ``CLOUDLAUNCH_QUERY_CACHE_PERIOD``
   before starting Galaxy to control the caching period (in seconds). Setting
   this to 0 will allow you to get around the node removal issue where, if a
   Pulsar node is removed, jobs may be routed to a dead node for the duration of
   the caching period. However, we recommend setting a value greater than 0 to
   avoid repeatedly querying a remote server during each job submission.

2. Incompatible tools

   Due to the nature of how Galaxy collects metadata on datasets, certain tools
   are not compatible with job execution in the bursting mode. Some of these
   issues will be resolved once Pulsar is upgraded to collect metadata itself
   but for the time being the following is an (incomplete) list of tools and
   tool classes that will not operate when executed via the GalaxyCloudRunner:
   upload tool, data managers, tools that use metadata input, and tools that
   use custom data discovery.

3. Auto-scaling

   Currently, the GalaxyCloudRunner does not support automatic scaling, you must
   manually add and remove individual nodes but you can add as many as you would
   like. We will be adding autoscaling features as part of CloudMan v2.0 in
   future.

4. Galaxy versions prior to 19.01

   Galaxy versions prior to 19.01 do not support certain features required by
   GalaxyCloudRunner and therefore, need more complex configuration steps.
