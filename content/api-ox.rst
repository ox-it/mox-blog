Building web services for the new Mobile Oxford
###############################################

:date: 2013-04-03 10:20
:slug: mobile-oxford-services
:author: Martin Filliau
:status: draft
:summary: How we decided to build a generic API ready to support a various range of clients around the University

We began to build an entirely new version of Mobile Oxford to replace the old one which had some conceptual issues (large code base mostly untested, various performance problems...) and wasn't adapted anymore to the market we are targeting (will be described in more details in a different blog post).

The new architecture is centered around a JavaScript client and an API providing data to the client. The API could be considered as a "search" solution mostly. We decided to build an API over HTTP (RESTful-ish), serving JSON as our primary representation as it serves our immediate needs.

Towards a generic API
---------------------

We knew that the current version of Mobile Oxford was already consumed by other clients (thanks to a JSON output of the template context), although it wasn't developed with that goal in mind, and not very easy to consume due to the way information was represented.

With that information in mind, we decided that our API should be generic enough to be consumed by other applications as well, Mobile Oxford being the first consumer for it.
It makes sense to us to build reusable services as we have the feeling that some other teams might have the same needs than us.

This is of course raising some issues as well, as we have to constantly think about having to make a clear separation between data and our client (versus having a "private" API for our client and a public one, but we do not feel the need to have a separation, at least for now).

Hypermedia API: ease discovery, favorise reusability
----------------------------------------------------

As we want our API to be easily usable and understandable, we knew that our API had to be an hypermedia API embedding links between representations.
Various options are available and we made the choice of `HAL (Hypertext Application Language) <http://stateless.co/hal_specification.html>`_ because it is very clear, easy to understand and not coupled to JSON.

You can visit `api.m.ox.ac.uk <http://api.m.ox.ac.uk>`_ to have an overview of the API using the `HAL browser <http://github.com/mikekelly/hal-browser>`_, a developer friendly browser allowing to follow the links in the
API (in the line of the Google API Explorer).
