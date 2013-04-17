Secure off-site media with Django-Compress
##########################################
:date: 2010-11-19 11:03

.. raw:: html

   <div style="color: #000000; font-family: Arial, Helvetica, sans-serif; font-size: 13px; background-color: #ffffff; margin: 8px;">

.. raw:: html

   </p>

The next version of Mobile Oxford will coincide with several
improvements to our server infrastructure, including off-loading our
static content to a second, dedicated, Lighttpd server, however this
deployment wasn't just as simple as changing the MEDIA\_URL setting in
the Django config. Because we use SSL for certain parts of the website,
we need to set our media to load from our static server using https, but
setting the MEDIA\_URL requires the protocol to be specified when using
a full URL (previously we just used a relative one, which meant we
didn't have an issue).

.. raw:: html

   </p>

A \ `Django snippet`_ revealed a context processor (which is now \ `in
molly.utils`_) to dynamically alter the MEDIA\_URL template tag based on
whether or not the request is secure, but we use \ `django-compress`_ to
minify our CSS and JavaScript, which doesn't use the MEDIA\_URL template
tag to generate it's URLs. Fortunately, we're not the first person to
come across this problem, and \ `Michael Lim`_ has `forked the original
django-compress on Github`_ which implements the same logic as the
context processor to dynamically alter the URL used for the compress JS
and CSS files.

.. raw:: html

   </p>

One gotcha however is that this requires
the \ `django.core.context\_processors.request`_ context processor to be
activate, which isn't by default, but\ `adding that to the config`_ and
we're all set.

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   </p>

 

.. raw:: html

   </p>

.. raw:: html

   </p>

`Permalink`_

\| `Leave a comment  »`_

.. raw:: html

   </p>

.. _Django snippet: http://djangosnippets.org/snippets/1754/
.. _in molly.utils: https://github.com/mollyproject/mollyproject/commit/08b0505c71ad028a6d632a71a2c58e641900c109
.. _django-compress: http://code.google.com/p/django-compress/
.. _Michael Lim: https://github.com/mikelim
.. _forked the original django-compress on Github: https://github.com/mikelim/django-compress
.. _django.core.context\_processors.request: http://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request
.. _adding that to the config: https://github.com/mollyproject/mollyproject/commit/43ee9e1d78ead024e5e9e93e9c6deea1d293e4c6
.. _Permalink: http://mobileoxfordtech.posterous.com/33885695
.. _Leave a comment  »: http://mobileoxfordtech.posterous.com/33885695#comment
