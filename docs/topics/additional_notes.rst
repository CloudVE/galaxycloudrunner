.. _additional-configuration:

Additional Configuration and Limitations
----------------------------------------

1. Configuring the query timeout

   You can set the environment variable ``CLOUDLAUNCH_QUERY_CACHE_PERIOD``
   before starting Galaxy to control the caching period (in seconds). Setting
   this to 0 will allow you to get around the node removal issue where, if a
   Pulsar node is removed, your jobs may be routed to a dead node for the
   duration of the caching period. However, we recommend setting a value greater
   than 0 to avoid repeatedly querying a remote server during each job
   submission.

2. Upload tool

   Jobs for the upload tool (tool id `upload1`) cannot be sent to remote Pulsar
   nodes.

3. Auto-scaling

   Currently, the GalaxyCloudRunner does not support automatic scaling, you must
   manually add and remove nodes. We will be adding autoscaling features as
   part of CloudMan v2.0 in future.

4. Galaxy versions prior to 19.01

   Galaxy versions prior to 19.01 do not support certain features required by
   GalaxyCloudRunner and therefore, need more complex configuration steps.
