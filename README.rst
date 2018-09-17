
=================
Uperations Kernel
=================

This repository contains the required models to build an [Uperation](https://github.com/baminou/uperations) project.


Library
-------

A library contains a group of operations. Once your Uperation project done, you can create a module that will
contain all your operations and upload to pypi. Those operations can then be re-used in another project,
a Dockerfile or any other system. In an Uperation project, a default command has the following format:

.. code-block::

    ./uperation [LIBRARY_NAME] [OPERATION_NAME]


- LIBRARY_NAME: The name of the library that is defined by the user of this one in the kernel.py file. To avoid collisions between library names, the user of the library can rename the LIBRARY_NAME in his project.

- OPERATION_NAME: Name of the operation in the library. This is defined by the creator of the library.


Operation
---------

An operation is an action to be executed. The purpose of an operation is to be easily re-usable in different workflows, or any other projects. An operation is by default independent of other operations, and is easy to document.
Once an operation is created, the testing of this operation can be easily done following pytest convention.