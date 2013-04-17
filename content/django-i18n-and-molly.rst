Django, i18n and Molly
######################
:date: 2011-06-03 10:31
:author: Chris Northwood

Here in the Mobile Oxford team, we've been working with the team at
`Bangor University`_ to help get the `Molly Project`_, the open source
project which grew from Mobile Oxford's code base, ready to be
translated into multiple languages (in Bangor's case - Welsh!).

As Molly is a Django project, we can use Django's `extensive i18n
framework`_ to do most of the work for us, however, this does rely on us
marking up the text for translation. When it comes to testing i18n, we
needed a quick way of generating a test language file for us to drop in
to check we've caught all of the strings that need to be translated.

Inspired by `Richard Mitchell at Isotoma, who suggested using upside
down English to test for Unicode bugs`_, we decided that testing i18n
using upside-down English makes the most sense for us. `And so, I wrote
a script which did this`_. It ignores formatting strings and inside
HTML, but everything else gets inverted using the lookup table defined
at the top. We used this as we marked up each app in a feedback loop to
make sure everything is marked up, and I think we got everything.

Data from external services (e.g., the library) isn't translated, but
where our data sources (e.g., the OpenStreetMap planet.osm dumps and the
NaPTAN) do contain multi-lingual data, this is now imported into our
database and tagged as the correct language, and where the data exists,
it means you'll see it in different languages!

However, we did find a few gotchas with Django's i18n. First of all,
there's `a fairly major bug in Django's makemessages function`_, which
means that the output of makemessages for JavaScript is unreliable as to
whether or not we caught all the strings. The only real alternative is
to generate a .po file by hand, however we cheated by `creating a
'dummy.js' file`_ which manually contains all the JS scripts, to make
sure they're found. However, this does mean we have to update this file
every time we add a new string, which is a pain.

We've no plans to launch multiple languages on Mobile Oxford at the
moment, but this is perhaps something we can look at in the future -
translating the site into multiple languages to make it more useful for
tourists to the city!

.. _Bangor University: http://www.bangor.ac.uk/
.. _Molly Project: http://mollyproject.org/
.. _extensive i18n framework: https://docs.djangoproject.com/en/1.2/topics/i18n/
.. _Richard Mitchell at Isotoma, who suggested using upside down English to test for Unicode bugs: http://blog.isotoma.com/2010/06/generating-sample-unicode-values-for-testing/
.. _And so, I wrote a script which did this: https://github.com/mollyproject/mollyproject/blob/b19a2d6efccb041db4bc626b666764672bf50255/scripts/testlanguage.py
.. _a fairly major bug in Django's makemessages function: https://code.djangoproject.com/ticket/7704
.. _creating a 'dummy.js' file: https://github.com/mollyproject/mollyproject/commit/c9916356601ac273521c2169d979330572c9680f#molly/media/site/js/dummy.js
