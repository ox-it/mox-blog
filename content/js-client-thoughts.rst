Thoughts on JavaScript clients
==============================

.. put this into a summary and add a bit more 
tl;dr - Writing JavaScript clients
is about trading off application state for a good user experience.

In August last year we took the decision to rewrite Mobile Oxford. There were
many reasons for taking this decision which will be covered in other blog posts.
At the outset of any major project like this you tend to make many assumptions,
especially if you lack experience in the domain. This process of compromising on
your ideals to deliver a product is common in software development, hopefully
this post will provide a glimpse into one example of this.

Caveat: The rewrite of Mobile Oxford is an ongoing project and is currently in a
beta stage.

Our initial outlook on web applications (or more specifically, JavaScript
clients): initial page loads should *always* deliver a fully rendered page.
Browsing from this page should be a combination of AJAX requests and client-side
templating.

Aside: Twitter.com is a great example at providing this type of functionality.

What we ended up with: Static HTML response on all URLs which bootstraps the
page with a JavaScript framework. This framework routes the request to a view
capable of requesting additional resources and rendering a full page output.

The reasons for compromising on this initial vision are found somewhere between,
"it's too complex" and "that's a bad user experience".

Added complexity
----------------

In order to render an identical page from a "JavaScript client request" and a
good ol' fashioned HTTP Accept: "HTML please!" request, your display logic must
be shared by your client and server. This is *not* a simple task, also this
isn't the same as sharing your templates between both client and server it's all
business logic apart from requesting the data itself.

JavaScript templating tends to work by selecting an element in the page,
emptying it from the DOM and inserting the DOM elements generated from your
JavaScript templates. So a single page load could be made up of several
different templates being rendered. On the server you tend to get everything in
order and render a complete output hopefully in a template language which allows
template inheritance.

Despite all this added complexity it's always possible to provide both
fully-rendered HTML responses alongside a JavaScript client rendering data
fetched asynchronously.

User Experience
---------------

Not all data is created equal. Some can be accessed quickly, some can be cached
and some is even slow to request yet extremely time-sensitive. In our case the
last, slowly retrieved time sensitive data is a good description for the local
bus real-time information provider. Let me give a common m.ox usecase as an
example, "where is the nearest bus stop, and when is the next bus?" the first
part of this query can be answered almost immediately, however the real-time
information means a call to an external provider. Something we have no control
over, which could respond at any time or not at all. Obviously it would be crazy
to wait for this to respond before rendering a page to the user.

We find this pattern in many places in Mobile Oxford, a *potentially* fast
initial response followed up with slow to retrieve timely data. Library
availability is another example, "this book can be found in this library" can be
answered quickly, however "is the book currently checked out?" is much slower to
answer.

Native Application Containers
-----------------------------

There are many reasons why native applications are desirable, I won't be going
into those here. Perhaps if people are interested I (or another colleague) could
go provide more details why we decided we wanted a native application.

Having users install your JavaScript client essentially circumvents your
"initial page load" problem. Now the initial load is done locally on their device,
as such it should only be encumbered by JavaScript execution time, rendering and
any required AJAX requests.
