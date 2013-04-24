Thoughts on JavaScript clients
##############################

:date: 2013-04-24 11:16
:tags: javascript, client, api
:category: JavaScript
:slug: js-client-thoughts
:author: David King
:email: david.king@it.ox.ac.uk
:summary: How we started viewing writing JavaScript clients as a tradeoff
          between application state and user experience.

In August last year we took the decision to `rewrite Mobile Oxford
<http://new.m.ox.ac.uk>`_ as a JavaScript client backed by a `generic API
<http://blog.m.ox.ac.uk/posts/2013/04/18/mobile-oxford-services/>`_. There were
many reasons for taking this decision which will be covered in other blog
posts.  After a short period of development on the JavaScript client we
realised some assumptions we'd made upfront were either incorrect or
infeasible. This process of compromising on your ideals to deliver a product is
common in software development, hopefully this post will provide a glimpse into
a couple of examples of this.

Our initial outlook on web applications (or more specifically, JavaScript
clients): initial page loads should *always* deliver a fully rendered page.
Browsing from this page should be a combination of AJAX requests and client-side
templating.

If you're interested in an example of this behaviour `Twitter
<http://twitter.com>`_ do a great job. This is easy to see if you browse with
the Webkit (or Firefox) developer tools network interface open.

What we ended up with: Static HTML response on all URLs which bootstraps the
page with a JavaScript model-view-controller (MVC) framework. This framework
routes the request to a view capable of requesting additional resources and
rendering a full page output.

The reasons for compromising on this initial vision are found somewhere between,
"it's too complex" and "that's a bad user experience".

Increasing Complexity
---------------------

In order to render an identical page from a "JavaScript client request" and a
good ol' fashioned HTTP Accept: "HTML please!" request, your display logic must
be shared by your client and server. Sharing templates on client/server is a
good start for this approach, but duplicating the logic which renders those
templates requires a *lot* of effort.

We progressed with a split code base across the client and server for a couple
of weeks before it proved to be untenable for us. Alternatives to splitting your
codebase exist in running a JavaScript runtime on the server, see `further
reading`_ for more information on this.

User Experience
---------------

Not all data is created equal. Some can be accessed quickly, some can be cached
and some can be slow to request yet extremely time-sensitive. In our case the
last, slowly retrieved time sensitive data is a good example of the local bus
real-time information provider. For example, "where is the nearest bus stop, and
when is the next bus?" we can answer the first part of this query almost
immediately, however the real-time information means a call to an external
provider. Something we have no control over, which could respond at any time or
not at all. Obviously it would be crazy to wait for this to respond before
rendering a page to the user.

.. image:: |filename|/images/new-mox-library.png
   :class: right

We find this pattern in many places in Mobile Oxford, a *potentially* fast
initial response followed up with slow to retrieve timely data. Library
availability is another example, "this book can be found in this library" can be
answered quickly, however "is the book currently checked out?" is much slower to
answer.

User contexts are clearly shifting so much from the simple "at desktop PC with
ethernet" it's important to consider what your application could offer in terms
of offline support. We're not doing much in this area for Mobile Oxford however
in another project we are `"bootstrapping" the client with some pre-loaded data
<http://backbonejs.org/#FAQ-bootstrap>`_.

Native Application Containers
-----------------------------

There are many reasons why native applications are desirable, I won't be going
into those here. If you are interested to hear more leave a comment and we'll
try to write a few words on this.

Having users install your JavaScript client essentially circumvents your
"initial page load" problem. Now the initial load is done locally on their
device, as such it should only be encumbered by JavaScript execution time,
rendering and any required AJAX requests. Of course this creates other problems
particularly with the lead time on making deployments and having users
*actually* install the updates.

Connectivity, errors and other issues
-------------------------------------

Beyond offering offline support your application should handle the case of
"partial connectivity" where the user might be in an area of flaky network
coverage. This might involve retrying requests (with exponential backoff) or
providing UI elements for users to retry themselves.

We have struggled, and continue to struggle with capturing errors in JavaScript
and relaying that information to users. When many services are being engaged to
produce a single page load this becomes a complex problem. With Mobile Oxford we
may be unable to access real-time library information but still be able to query
the holdings. This is still useful information for users and when developing the
UI it's important to pre-empt partial page loads such as this.

Further reading
---------------

The code and documentation for our JavaScript client is open source and
`available on github <https://github.com/ox-it/moxie-js-client>`_.

Writing shared client and server-side code is becoming a
major talking point recently. While it's clear nobody has "solved" the above
problems there are some interesting projects progressing in this area:

* `Rendr from Airbnb <http://nerds.airbnb.com/weve-open-sourced-rendr>`_, uses
  conventions in structuring your application to allow for a single code base to
  run in both the server and client environments.
* `backbone-serverside <https://github.com/SC5/backbone-serverside>`_, a recent
  `post to Mozilla Hacks
  <https://hacks.mozilla.org/2013/04/serving-backbone-for-robots-legacy-browsers/>`_
  on a different approach to Rendr. Instead of providing a way to structure your
  application this project seeks to "polyfill" specific client-side only API's
  allowing your application to run on the server.

This covers just a few of the challenges we've encountered building a robust
JavaScript client. Expect future posts to cover topics such as code quality,
testing and server-side JavaScript. Of course if you'd like to hear about
something in particular leave a comment or `send me an email
<mailto:david.king@it.ox.ac.uk>`_.
