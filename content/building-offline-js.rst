Building offline JavaScript applications
========================================

:date: 2013-05-29 10:20
:tags: JavaScript, phonegap, cordova
:category: JavaScript
:slug: preloading-javascript-applications
:author: Dave King
:summary: Adding a step to your build process to preload an initial server
          response and caching images.

Recently we've been working on a JavaScript application for the University
Museums here in Oxford. The application presents the user with the top 10
objects at each of the museums and will be released later in the year.

There are 3 key components to the project, a JS client frontend, a
"back-office" for adding and editing the content in the application and
finally a simple HTTP API which `serves JSON
<https://gist.github.com/davbo/5670378>`__ to the clients describing each of
the museums and the objects themselves.

Unfortunately mobile network connectivity within the museums isn't always
great. Whilst there are some plans to improve this situation it was clear to
us that we couldn't depend on all of our users having a stable network
connection, we needed the application to be fully functional offline.

"Bootstrapping" an initial pageload is common for JavaScript applications,
it's recommended as good practice within the `Backbone.js documentation
<http://backbonejs.org/#FAQ-bootstrap>`__. Whereby your application server
embeds JSON directly into your rendered HTML.

This was our initial approach, however since our application is to be
installed within a "native application container" (Phonegap / Apache Cordova),
we can't embed JSON when building a HTML response we can however do it as part
of a build process. Our initial solution for this would simply ``curl`` the API and
pipe that response through ``sed`` to embed the JSON into our html.

.. image:: |filename|/images/prm-objects.png
   :class: right

Not the most elegant solution but it does the job at embedding the JSON
response. Unfortunately however it doesn't meet our requirement of having the
application work offline, since a large portion of this application means
having users browse images of the exhibits. So not only do we need to preload
JSON, we should also cache images of all the items.

Enter Python, thanks to being "batteries included" we're able to load the
JSON, parse it, find all the images we want to preload and download them all
into the build folder. We're also able to use the `string.Template
<http://docs.python.org/2/library/string.html?highlight=string.template#string.Template>`__
class instead of using a ``sed`` substitution. The Python code which does this
preloading is `available as a gist <https://gist.github.com/davbo/5670421>`__.

The output from this process is an index.html with 2 blocks of embedded JSON,
one being the raw output from the API and the second is a mapping between
external image paths and the locally cached file path. Some `simple
JavaScript <https://gist.github.com/davbo/5670438>`__
handles looking up images in this mapping and favours the local
images where possible.

With this build process in place all our packages include the latest
representations and images from the API. Of course it isn't without drawbacks,
now our build process depends on the API being available and the time to build
has increased by a few seconds.

Unfortunately this project isn't (currently) open source however, if you do
have any questions about it or the build process described here ask away in
the comments and we'll do our best to answer.
