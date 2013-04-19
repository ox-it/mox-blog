Building web services for the new Mobile Oxford
###############################################

:date: 2013-04-03 10:20
:slug: mobile-oxford-services
:author: Martin Filliau
:email: martin@filliau.com
:summary: How we decided to build a generic API ready to support a various range of clients around the University

We began to build an entirely `new version of Mobile Oxford <http://new.m.ox.ac.uk>`_ to replace the old one which had built up technical debt over the years and with the rapid changes in smartphone technology, was unable to target our market appropriately (more details in a different blog post).

The new architecture is centered around an API providing data to a JS application (client). We decided to build our
API over HTTP (RESTful-ish), serving JSON as our primary representation and architecting in such a way that it is easy to extend this to other representations.

The API presents information about different domains in the university, some of which are already provided by the
current `Mobile Oxford <http://m.ox.ac.uk>`_ and some new ones as well. After analysing our use cases, we found that most were search problems and as such we organised as a search solution, for example:

- searching for people
- search libraries (books)
- search graduate courses
- search for places

Towards a generic API
---------------------

The current version of Mobile Oxford is already consumed by other clients (such as the `Blavatnik School of Government <http://www.bsg.ox.ac.uk/>`_ internal iPad application), as the system was not originally designed for this purpose, it provided a sub-optimal experience for those trying to integrate with it (a JSON output of a template context for an HTML page).

With that information in mind, we decided that our API should be generic enough to be consumed by other applications
as well, Mobile Oxford being the first consumer for it. Being an aggregator and an integrator of many disparate systems in the university, it makes sense for us to be able to output these to others in a consistent, easy to use form.

This of course raises some issues, we now have to carefully consider the clear separation between data and our client
(versus having a "private" API tailored for our client and a public one, which we currently do not feel the need to have).

Providing links in our API
--------------------------

As we want our API to be easily usable and understandable, we investigated options to embed qualified links between
resources in our API (hypermedia). Various options are available (JSON-LD, OData, Collection+JSON...) and we made
the choice of `HAL (Hypertext Application Language) <http://stateless.co/hal_specification.html>`_ because it makes a
clear separation between properties of your resources and metadata (links) by using a standard syntax, which is easy to understand
and not coupled to JSON.

You can visit `api.m.ox.ac.uk <http://api.m.ox.ac.uk>`_ to have an overview of the API using the
`HAL browser <http://github.com/mikekelly/hal-browser>`_, a developer friendly browser to view resources and follow
links (similar to the `Google API Explorer <https://developers.google.com/apis-explorer/>`_).

.. image:: |filename|/images/hal_browser_19_apr_2013.png

For example, our API provides Points of Interest (POI) around Oxford, some of them having *real-time* information,
a client can follow the link ``rti`` to discover an associated resource. Alternatively, you can get the parent POI
by following the link ``parent``.

[gist:id=5406037]

Our code is open-sourced on GitHub as "`Moxie <https://github.com/ox-it/moxie>`_", this is a work in progress and we
will publish more technical details in a different blog post soon.
