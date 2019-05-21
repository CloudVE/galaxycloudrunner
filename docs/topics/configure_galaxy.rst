Configuring Galaxy
==================

Configuring Galaxy 19.01 or higher
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

Reducing data transfers
-----------------------

If you would like to control the data transfer configurations for Pulsar, an
additional option can be specified in the ``job_conf`` destination for the
GalaxyCloudRunner rule. This is particularly useful for Galaxy's reference data
because the remote Pulsar nodes have been configured to mount the Galaxy public
file system repository with pre-formatted reference data for a number of tools.
In turn, this speeds up job execution and reduces data transfers from your
Galaxy instance because the relevant files do not need to be transferred to the
remote node with each job.

Note that this configuration is necessary only if your file system paths differ
from those on the remote Pulsar nodes. Specifically for the reference data,
Pulsar nodes mount Galaxy Project's CVMFS repository, which is available under
``/cvmfs/data.galaxyproject.org/`` directory. The layout of that directory can
be inspected here: https://gist.github.com/afgane/b527eb857244f43a680c9654b30deb1f

To enable this feature for the GalaxyCloudRunner, it is necessary to add the
following ``param`` to the existing job destination in ``job_conf.xml``:

.. code-block:: xml

    <!-- Path for the Pulsar destination config file for path rewrites. -->
    <param id="pulsar_file_action_config">config/pulsar_actions.yml</param>


In addition, *transfer actions* need to be defined that specify how paths should
be translated between the systems. This is done in a dedicated file pointed to
in the above ``param`` tag, in above example ``config/pulsar_actions.yml``. A
basic example of the file is available below while complete details about the
available transfer action options are available as part of the `Pulsar
documentation`_.

.. code-block:: yaml

  paths:
    - path: /galayx/server/tool-data/sacCer2/bwa_mem_index/sacCer2/
      path_types: unstructured
      action: rewrite
      source_directory: /galaxy/server/sacCer2/bwa_mem_index/sacCer2/
      destination_directory: /cvmfs/data.galaxyproject.org/managed/bwa_mem_index/sacCer2/


.. _Pulsar documentation: https://pulsar.readthedocs.io/en/latest/galaxy_conf.html#data-staging
