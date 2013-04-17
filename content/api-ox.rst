Building web services for the new Mobile Oxford
###############################################

:date: 2013-04-03 10:20
:slug: mobile-oxford-services
:author: Martin Filliau
:email: martin@filliau.com
:summary: How we decided to build a generic API ready to support a various range of clients around the University

We began to build an entirely new version of Mobile Oxford to replace the old one which had some conceptual issues
(large code base mostly untested, various performance problems...) and wasn't adapted anymore to the market we are
targeting (will be described in more details in a different blog post).

The new architecture is centered around an API providing data to a JS application (client). We decided to build an
API over HTTP (RESTful-ish), serving JSON as our primary representation as it serves our immediate needs
(but it should be easily extensible).

The API is presenting information about different domains of the university, some services already provided by the
current `Mobile Oxford <http://m.ox.ac.uk>`_ and new features as well. It is mostly organised as a search solution,
for example:

- searching for people
- search libraries (books)
- search graduate courses
- search for places 

Towards a generic API
---------------------

We knew that the current version of Mobile Oxford was already consumed by other clients (such as an internal iPad
application), although it wasn't developed with that goal in mind, and not very easy to consume due to the way
information was represented (a JSON output of the template context).

With that information in mind, we decided that our API should be generic enough to be consumed by other applications
as well, Mobile Oxford being the first consumer for it. It makes sense for us to build reusable services as we have
the feeling that some other teams might have the same needs than us.

This of course raises some issues, we now have to carefully consider the clear separation between data and our client
(versus having a "private" API tailored for our client and a public one, which we currently do not feel the need to have).

Providing links in our API
--------------------------

As we want our API to be easily usable and understandable, we investigated options to embed qualified links between
resources in our API (hypermedia). Various options are available (JSON-LD, OData, Collection+JSON...) and we made
the choice of `HAL (Hypertext Application Language) <http://stateless.co/hal_specification.html>`_ because it makes a
clear separation between properties of your resources and metadata (links) by using a standard syntax, easy to understand
and not coupled to JSON.

You can visit `api.m.ox.ac.uk <http://api.m.ox.ac.uk>`_ to have an overview of the API using the
`HAL browser <http://github.com/mikekelly/hal-browser>`_, a developer friendly browser to view resources and follow
links (similar to the `Google API Explorer <https://developers.google.com/apis-explorer/>`_).

For example, our API provides Points of Interest (POI) around Oxford, some of them having *real-time* information,
a client can follow the link ``rti`` to discover an associated resource. Alternatively, you can get the parent POI
by following the link ``parent``.

[gist:id=5406037]

Our code is open-sourced on GitHub as "`Moxie <https://github.com/ox-it/moxie>`_", this is a work in progress and we
will publish more technical details in a different blog post soon.
