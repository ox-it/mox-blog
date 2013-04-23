Whisky Web conference
#####################

:date: 2013-04-15 09:40
:slug: whisky-web-conference
:author: Martin Filliau
:summary: Some notes on what we have seen at the Whisky Web Conference

We have been to the `Whisky Web conference <http://whiskyweb.co.uk>`_ last week, held in Edinburgh and had a very enjoyable experience with very good speakers. Below are a few notes.

How Google Builds Web Services
------------------------------

Ian Barber, developer advocate for Google Plus made a very good presentation about web services at Google,
it was very relevant to us regarding what we are doing with the new Mobile Oxford.

They usually build a "private" API for internal use, not released to the general public and a "public" API. This separation allow them to publish less/differently data from their private API, and they can also change their private API more easily to fit their needs (the public API has to be stable). He also raised the question of which customers for your API; how do you get to know them and what they want (+ cost vs. benefit when building an API).
   
They, of course, need their API to be easily usable, they have built an "API for APIs" to help `discovery <https://developers.google.com/discovery/>`_, in addition to use a "discovery document" (using `JSON Schema <http://json-schema.org/>`_) to describe methods availbale on their API and describe how the resources will look like (which fields are available etc).
This can be seen as a *light* version of `WSDL <http://en.wikipedia.org/wiki/Web_Services_Description_Language>`_ (generally used to descripe SOAP web services).
This "discovery document" is used to generate client libraries per language, which allow more advanced uses in addition to plain HTTP calls such as `RPC Batch <https://developers.google.com/api-client-library/javascript/features/rpcbatch>`_ (sending multiple requests at once), `CloudEndpoint <https://developers.google.com/appengine/docs/java/endpoints/overview>`_ (generating APIs) and `Protobuffers <https://developers.google.com/protocol-buffers/docs/overview>`_.

We have similar concerns about the discovery of our API

Bringing the Open Web and APIs to mobile devices with Firefox OS
----------------------------------------------------------------

Robert Nyman from Mozilla did an introduction of Firefox OS and the possibilities for creating (web)apps on their platform.

It would be interesting to (try to) deploy the new Mobile Oxford on Firefox OS (with our current setup it should just be a matter of adding one manifest file to describe the application).

Identity, responsiveness and the future of the web
--------------------------------------------------

Ade Oshineye, developer advocate for Google Plus

Scaling applications with RabbitMQ
----------------------------------

`RabbitMQ Simulator <https://github.com/RabbitMQSimulator/RabbitMQSimulator>`_