Configuring Galaxy
==================

Configuring Galaxy v19.01 or higher
-----------------------------------
1. First install the GalaxyCloudRunner into your Galaxy virtual environment.

.. code-block:: shell

    cd <galaxy_home>
    source .venv/bin/activate
    pip install galaxycloudrunner

2. Edit your `job_conf.xml` in the `<galaxy_home>/config` folder and add the
   highlighted sections to it.

   You will need to add your own value for the ``cloudlaunch_api_token`` to the
   file. Instructions on how to obtain your CloudLaunch API key are given below.

.. literalinclude:: ../samples/job_conf.xml.basic
   :language: xml
   :linenos:
   :emphasize-lines: 7,9-22

3. Launch as many Pulsar nodes as you need through `CloudLaunch`_. The job rule
   will periodically query CloudLaunch, discover these new nodes, and route jobs
   to them.
   Instructions on how to launch new Pulsar nodes are below.

4. Submit your jobs as usual.


.. _galaxy_configuration_legacy:

Configuring Galaxy versions lower than 19.01
--------------------------------------------
1. First install the GalaxyCloudRunner into your Galaxy virtual environment.

.. code-block:: shell

    cd <galaxy_home>
    source .venv/bin/activate
    pip install galaxycloudrunner

2. For prior prior to Galaxy 19.01, you will need to add a GalaxyCloudRunner
   job rule to your Galaxy configuration by pasting the following file contents
   into your Galaxy job rules folder in:
   `<galaxy_home>/lib/galaxy/jobs/rules/`.

   Create a file named galaxycloudrunner.py and paste the following contents
   into the file at the location above.

.. literalinclude:: ../../galaxycloudrunner/rules/cloudlaunch_pulsar.py
   :language: python
   :linenos:

3. Edit your job_conf.xml in the `<galaxy_home>/config` folder and add the
   highlighted sections to it.

   You will need to add your own ``cloudlaunch_api_token`` to the file.
   Instructions on how to obtain your CloudLaunch API key are given below.
   If you have a Galaxy version prior to 19.01, the line
   `<param id="rules_module">galaxycloudrunner.rules</param>` passed to your
   destination will not work. This is the reason that we need to perform step 2.

.. literalinclude:: ../samples/job_conf.xml.legacy.basic
   :language: xml
   :linenos:
   :emphasize-lines: 7,9-19

4. Launch as many Pulsar nodes as you need through `CloudLaunch`_. The job rule
   will periodically query CloudLaunch, discover these new nodes, and route jobs
   to them.
   Instructions on how to launch new Pulsar nodes are below.


5. Submit your jobs as usual.

.. _CloudLaunch: https://launch.usegalaxy.org/
