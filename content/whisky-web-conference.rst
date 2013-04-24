Whisky Web conference
#####################

:date: 2013-04-25 09:40
:slug: whisky-web-conference
:author: Martin Filliau, David King
:summary: Some notes on what we have seen at the Whisky Web Conference

Last week we attended the `Whisky Web conference <http://whiskyweb.co.uk>`_, held in Edinburgh and
had a very enjoyable experience with very good speakers. Below are a few notes.

How Google Builds Web Services
------------------------------

Ian Barber, developer advocate for Google Plus gave a very good presentation about web services at Google,
it was very relevant to us regarding what we are doing with the new Mobile Oxford.

They usually build a "private" API for internal use, not released to the general public and a "public" API.
This separation allow them to publish less/different data from their private API, they can also change
their private API more easily to fit their needs (the public API has to be stable). He also raised the question
of identifying the customers of your API; how do you get to know them and what they want (+ cost vs. benefit when building an API).

They of course, need their API to be easily usable, they have built an "API for APIs" to help `discovery <https://developers.google.com/discovery/>`_,
in addition to use a "discovery document" (using `JSON Schema <http://json-schema.org/>`_) to describe methods available
on their API and describe how the resources will look, which fields are available etc.
This can be seen as a *light* version of `WSDL <http://en.wikipedia.org/wiki/Web_Services_Description_Language>`_
(generally used to descripe SOAP web services). This "discovery document" is used to generate client libraries per
language, which allow more advanced uses in addition to plain HTTP calls such as `RPC Batch <https://developers.google.com/api-client-library/javascript/features/rpcbatch>`_
(sending multiple requests at once), `CloudEndpoint <https://developers.google.com/appengine/docs/java/endpoints/overview>`_
(generating APIs) and `Protobuffers <https://developers.google.com/protocol-buffers/docs/overview>`_.

We have similar concerns about the discovery of our API in Mobile Oxford so it was interesting to see how they resolved some concerns that
we have - although we are taking a different approach (see `our blog post on building web services for the new version <http://blog.m.ox.ac.uk/posts/2013/04/18/mobile-oxford-services/>`_).

`Slides from this presentation
<https://speakerdeck.com/ianbarber/how-google-builds-webservices>`__.

Bringing the Open Web and APIs to mobile devices with Firefox OS
----------------------------------------------------------------

Robert Nyman from Mozilla gave an introduction to `Firefox OS <https://marketplace.firefox.com/developers/>`_
and the possibilities for creating (web)apps on their platform.

It would be interesting to deploy the `new Mobile Oxford <http://new.m.ox.ac.uk>`_ on Firefox OS
(with our current setup it should be fairly easy, by adding a JSON manifest file to describe the application).
We are currently working on packaging `our JS app <http://blog.m.ox.ac.uk/posts/2013/04/24/js-client-thoughts/>`_
with `PhoneGap/Apache Cordova <http://cordova.apache.org/>`_, deploying on Firefox OS means that we do not need
to use any native container.

The "open marketplace" concept is interesting, and the ability to build your own marketplace could be interesting
for an institution such as the University which could potentially have (internal) apps promoted in one central place.

Identity, responsiveness and the future of the web
--------------------------------------------------

Ade Oshineye, developer advocate for Google Plus gave an interesting presentation, underlining that responsiveness
goes beyond responsive *design*, to responsive **context** (e.g. mobile vs tablet, portrait vs landscape...), and
being responsive server-side as well (providing nice degradation if the latency is too high for example).

Scaling applications with RabbitMQ
----------------------------------

Good introduction on messaging by Àlvaro Videla, we have been quite impressed by the `RabbitMQ Simulator <https://github.com/RabbitMQSimulator/RabbitMQSimulator>`_,
seems awesome for learning messaging... and also for publishing interactive documentation!

Building Better Developers
--------------------------

`Rowan Merewood <https://twitter.com/rowan_m>`_ from Inviqa presented on how we
can develop our own skills as developers and how your employer can enable your
personal growth. Using examples such as Valve's employee handbook which
describes their developers as T-shaped, meaning they have a deep expertise in
one area whilst being broad-generalists in others.

Other take-away comments/ideas from this talk for me were:

* Deliberate practice:

  * Coding Kata's -- repeated exercises to hone your abilities.

* Deliver bad news early.

* Attack ideas, not people.

* If you're the smartest person in the room, you're probably not learning
  anything.

`Slides from this presentation
<https://speakerdeck.com/rowan_m/building-better-developers>`__.

Coming Soon to a Browser Near You
---------------------------------

`Alan Greenblatt <http://blattchat.com/>`_ from Adobe gave a talk on some new
browser features. He discussed how Adobe want to see more powerful typesetting
features in browsers, to that end he showed us the ``shape-inside`` and
``shape-outside`` features of the `CSS Exclusions
<http://dev.w3.org/csswg/css-exclusions/>`_ specification which Adobe has
contributed to. Hopefully this will enable people express more creativity
designing magazine style layouts in HTML+CSS. On this same topic we were also
demonstrated the ``flow-into`` and ``flow-from`` properties from the `CSS
Regions <http://dev.w3.org/csswg/css-regions/>`_ specification. These flow
regions allows your content to flow through multiple regions and handles being
resized / responding to media-queries.

Other features discussed included the CSS Filters API which was demonstrated
through Adobe's `CSS FilterLab
<http://html.adobe.com/webplatform/graphics/customfilters/cssfilterlab/>`_.

HTTP and Your Angry Dog
-----------------------

Ross Tuck from Ibuildings delivered and excellent set of slides with some
particularly astute metaphors for HTTP such as "imagine the URL as your primary
key". Definitely recommend browsing the slides if you're unfamiliar with the
workings of HTTP.

`Slides from this presentation
<http://www.slideshare.net/rosstuck/http-and-your-angry-dog>`__.
