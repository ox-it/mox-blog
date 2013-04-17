Exception Tracking and JIRA
###########################
:date: 2010-11-09 17:41

Keeping track of exceptions, especially in a large project like Mobile
Oxford, can be at times a challenging task. The solution we currently
use is to have an exception generate an e-mail to us, with information
about the exception, and the request that caused it. Some clever
hashing, combined with a decent e-mail client, allows these e-mails to
be threaded, but languishing in our inboxes probably isn't the best way
to handle them. Unhandled exceptions are bugs, and should be handled as
such within our current bug tracking systems.

.. raw:: html

   </p>

One thing we've started doing at Mobile Oxford is looking at the tools
we're using, particularly for bug tracking. Previously we used
`SourceForge`_, but found its tools to be below the standard we're
looking for. We looked at a myriad at other tools - `Github`_,
`Launchpad`_, `Playnice.ly`_, \ `Hoptoad`_ and `Lighthouse`_, with mixed
reactions. Hoptoad in particular had us interested, especially with the
`django-hoptoad`_ integration, which would make it easy to drop in to
the Mobile Oxford deployment, but Lighthouse's issue tracking
functionality let it down.

.. raw:: html

   </p>

Internally, `OUCS`_ uses `JIRA`_ as a tool for bug tracking, which is an
insanely powerful tool that does everything we want, and more, so
inspired by Hoptoad and the django-hoptoad library, we investigated
getting Django reporting exceptions to JIRA, with the same sort of
duplication checking, etc - and an afternoon of coding later, we're
successful. It's external to the Molly Project, and can be dropped in to
any Django project as middleware. There are a few more settings than I'd
have liked to see in the finished product, but that just comes down to
the massive flexibility of JIRA.

.. raw:: html

   </p>

`The package is hosted on Github`_, feel free to fork it, and there are
some simple instructions in the `README`_ on how to add it, and the
settings that need to be added to your settings.py to get it working -
let us know your feedback, if you find it useful, or if you spot any
bugs!

.. raw:: html

   </p>

.. raw:: html

   </p>

`Permalink`_

\| `Leave a comment  »`_

.. raw:: html

   </p>

.. _SourceForge: https://sourceforge.net/projects/mollyproject/
.. _Github: https://github.com/
.. _Launchpad: https://launchpad.net/
.. _Playnice.ly: http://playnice.ly
.. _Hoptoad: https://hoptoadapp.com/
.. _Lighthouse: https://lighthouseapp.com/
.. _django-hoptoad: http://stevelosh.com/projects/django-hoptoad/
.. _OUCS: http://www.oucs.ox.ac.uk/
.. _JIRA: http://www.atlassian.com/software/jira/
.. _The package is hosted on Github: https://github.com/cnorthwood/django-jira
.. _README: https://github.com/cnorthwood/django-jira/blob/master/README
.. _Permalink: http://mobileoxfordtech.posterous.com/exception-tracking-and-jira
.. _Leave a comment  »: http://mobileoxfordtech.posterous.com/exception-tracking-and-jira#comment
