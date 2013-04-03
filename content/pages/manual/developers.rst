Resources for developers
########################

:date: 2013-04-03 10:20
:slug: developers
:author: Martin Filliau
:summary: How developers are working

Development environment
=======================

We use `Vagrant <http://www.vagrantup.com/>`_ (to build virtual machines for developers) and `Puppet <https://puppetlabs.com/>`_ (configuration management tool) to use the same, reproductible environment that will be used in production.

*Why?* Although we do not develop specifically for this environment, we reduce the risk of having a problem (e.g. version of dependencies) when deploying the application in production.

Prepare your application for easy monitoring
============================================

Every external service accessed by your application (e.g. search server, database, cache server) should be monitored via an health check (basic check to test that the service is available).

We usually have a "special" path (`/_health`) responding with HTTP 200 if everything is fine or HTTP 500 if there is a problem.

*Why?* the application can be easily monitored by an external service (such as Nagios) and the output gives a rapid idea of where the problem can be situated.

See `Mobile Oxford API <http://api.m.ox.ac.uk/_health>`_ for an example.

Break down your application in small(er) components
===================================================

*Why?* it is easier to test, easier to re-use.

See the project `cucm-http-api <https://github.com/ox-it/cucm-http-api>`_ developed as part of Telecoms Self-Service.

Security
========

See our `security checklist <|filename|security.rst>`_

Documentation
=============

Documentation of essential functions and design decisions should be written at the same time than code.

We usually have a `docs` directory at the root of the application containing documentation written with `Sphinx <http://sphinx-doc.org/>`_.

Tests and Continuous Integration
================================

Unit testing
------------

Unit test critical parts of components, CI to be configured appropriately.

Reliability testing
-------------------

"Design for failure", assume that some part of your service will run into troubles at some points, and try to degrade gracefully.

We use `Vaurien <http://vaurien.readthedocs.org/en/latest/>`_ to test the connection between our applications and external components (database, external HTTP service, cache server...).

Development process
-------------------

Develop new functions in branches, do a pull request with review before merging.