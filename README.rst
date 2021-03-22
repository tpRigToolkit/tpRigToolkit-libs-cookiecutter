tpRigToolkit-libs-cookiecutter
============================================================

Cookiecutter Project template for tpRigToolkit libs

.. image:: https://img.shields.io/badge/Python-2.7-yellow?logo=python
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/Python-3.7-yellow?logo=python
    :target: https://www.python.org/

.. image:: https://img.shields.io/github/license/tpRigToolkit/tpRigToolkit-tools-cookiecutter
    :target: https://github.com/tpRigToolkit/tpRigToolkit-tools-cookiecutter/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code_style-pep8-blue
    :target: https://www.python.org/dev/peps/pep-0008/

How to use (Manual Configuration)
============================================================

1. Go to the parent folder where you want to create project template into.

2. Open command line and execute cookiecutter command:

    .. code-block::

        cookiecutter https://github.com/tpRigToolkit/tpRigToolkit-libs-cookiecutter.git

    .. note::
        If you do not have Python available in your system paths, you can execute cookiecutter by launching the full path:

        .. code-block::

            "C:\Python27\Scripts\cookiecutter.exe" https://github.com/tpRigToolkit/tpRigToolkit-libs-cookiecutter.git


How to use (Automatic Configuration)
============================================================

1. Go to the parent folder where you want to create project template into.

2. Create a new file called **cookiecutter.yaml** and fill it with proper data. Here you have an example:

.. code-block:: yaml

    default_context:
        lib_name: "controlrig"
        lib_nice_name: "ControlRig"
        lib_description: "Library to manage control rig creation"
        lib_class: "ControlRig"
        lib_tags: "['tpRigToolkit', 'dcc', 'libs', 'control', 'rig']"
        author: "Tomas Poveda"
        email: "tpovedatd@gmail.com"
        year: "{% now 'utc', '%Y' %}"
        version: "0.0.1"
        supported_dccs: {'maya': ['2017', '2018', '2019', '2020', '2021']}


3. Open command line and execute cookiecutter command:

    .. code-block::

        cookiecutter https://github.com/tpRigToolkit/tpRigToolkit-libs-cookiecutter.git --config-file "D:\tpRigToolkit\cookiecutter.yaml" --no-input

    .. note::
        If you do not have Python available in your system paths, you can execute cookiecutter by launching the full path:

        .. code-block::

            "C:\Python27\Scripts\cookiecutter https://github.com/tpRigToolkit/tpRigToolkit-libs-cookiecutter.git --config-file "D:\tpRigToolkit\cookiecutter.yaml" --no-input
