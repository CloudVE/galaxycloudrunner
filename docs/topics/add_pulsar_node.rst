Adding new Pulsar nodes
-----------------------

1. To launch a new Pulsar node, go to `https://launch.usegalaxy.org/`_
2. Select the ``Pulsar Standalone`` appliance.

.. image:: ../images/pulsar_select_appliance.png

3. You may be asked to login through a social network provider.
4. Once logged in, fill in the following fields:

   a. The target cloud you want to launch in
   b. Your credentials for the cloud.
   c. Click the 'Test and use these Credentials button' to validate them.
   d. Click next

.. image:: ../images/pulsar_select_target_cloud.png

5. Finally, select the size of the Virtual Machine you want, and click Launch.

.. image:: ../images/pulsar_launch_appliance.png

6. Simply launching the node is enough, the GalaxyCloudRunner will now pick up
   your new nodes by querying the CloudLaunch API.

.. _https://launch.usegalaxy.org/: https://launch.usegalaxy.org/
