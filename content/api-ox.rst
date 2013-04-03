Building services for the new Mobile Oxford
###########################################

:date: 2013-04-03 10:20
:slug: mobile-oxford-services
:author: Martin Filliau
:status: draft
:summary: How we decided to build a generic API to support a various range of clients around the University

Difficulties with current Mobile Oxford: large code base mostly untested, various performance problems and already used as an API although it has not been built with that goal in mind.

Will to have a client application that can be used in various contexts for Mobile Oxford.

Towards a generic API
---------------------

Design a generic API that could be used by various clients, with a JavaScript client (the new Mobile Oxford) as the first consumer.

Common needs, build reusable services. Serve JSON, HTTP as an unified interface.

Hypermedia API
--------------

As we want our API to be easily usable and understandable, we knew that our API had to be an hypermedia API embedding links

Various options are available and we made the choice of `HAL (Hypertext Application Language) <http://stateless.co/hal_specification.html>`_ 
