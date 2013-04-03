Resources for operations
########################

:date: 2013-04-03 10:20
:slug: operations
:author: Martin Filliau
:summary: How operations are working

Environment
===========

Use `Puppet <https://puppetlabs.com/>`_ (same environment than `developers <|filename|developers.rst>`_), no manual operation should be done on machines.

Deployment
==========

PaaS-like, services to be deployed by `Puppet <https://puppetlabs.com/>`_, applications in a virtual environment (why? TODO) via a script (again, no manual operation on the machine please) See fabric scripts

Ability to roll back

Identifying deployments
-----------------------

It should be easy to track when the deployment has been done and what has been deployed (using the hash of HEAD of the given branch)

*Why?* it is easier to track bug by browsing code on the state where the machine has been deployed

Monitoring
==========

Use Monit to check machine constants (hard drive, memory and main services such as database, cache service).

Use an external monitoring solution (e.g. nagios) to monitor the state of an application by its route `/_health` (will return HTTP 200 if OK else HTTP 500).

Use an exception monitoring tool (e.g. `Sentry <http://getsentry.com>`_) to . See `our instance <http://sentry.oucs.ox.ac.uk/>`_ for an example.

Use graphite for performance monitoring.

Backups
=======

Data (e.g. contained in a database) that cannot be re-created rapidly **SHOULD** be backed up on an external service.

Communication
=============

If a deployment might cause a service interruption
--------------------------------------------------

Send an alert as early as possible if the service may encounter an at-risk period.

If an incident happens
----------------------

- send a post-mortem email to the rest of the team and appropriate persons giving details on what happened and what actions have been taken to mitigate this incident in the future
- add an entry to the downtime logs
