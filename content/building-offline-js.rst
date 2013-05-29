Building offline JavaScript applications
========================================

:date: 2013-05-29 10:20
:tags: JavaScript, phonegap, cordova
:category: JavaScript
:slug: preloading-javascript-applications
:author: Dave King
:summary: Adding a step to your build process to preload an initial server
          response an caching images.

Recently we've been working on a JavaScript application for the University
Museums here in Oxford. The application presents the user with the top 10
objects at each of the museums and will be released later in the year.

There are 3 key components to the project, the JS client frontend, a
"back-office" for adding and editing the content in the application and
finally a simple HTTP API which serves JSON to the clients describing each of
the museums and the top 10 objects. Here's a snippet of the JSON:

TODO: Include an example Museum and Object representation

Unfortunately mobile network connectivity within the museums isn't the best in
Oxford. Whilst there are some plans to improve this situation it was clear to
us that we couldn't depend on all our users having a network connection, we
needed the application to be fully functional offline.

Preloading a JSON response is common in JavaScript applications, the
documentation for Backbone.js recommends you serve clients an initial pageload
embedding an initial JSON response in the page itself.

This was our initial approach, however since our application is to be
installed within a "native application container" in our case Apache Cordova.
As such we can't embed JSON when building a HTML response we can however do it
as part of a build process. Our initial solution here would simply `curl` the
API and pipe that response through `sed` to embed the JSON into the page
something like this:

    TODO: GET THE CORRECT COMMAND FOR THIS
    curl <Museum API URL> | sed s/{{ JSON GOES HERE }}/

Not the most elegent solution but it does the job at embedding the JSON
response. Unfortunately it doesn't meet our requirement of having the
application work offline, as large portion of this application means having
users browse images of the exhibits. So not only do we need to preload JSON,
we should also cache images of all the items.

    TODO: include an image of the "browse items" view in the app

Enter Python, thanks to the "batteries included" nature of Python we're able
to load the JSON, parse it, find all the images we want to preload and
download them all into the build folder. We're also able to use the new[ish]
string.Template class instead of using a `sed` substitution. Here's our Python
preloader:

    TODO: INSERT the preloader.py code

The output from this process is an index.html with 2 blocks of embedded JSON,
one being the raw output from the API and the second is a mapping between
external image paths and the locally cached file path. Our JavaScript
application handles looking up images in this mapping and favours the local
images where possible. Here's the code which handles this mapping:

    TODO: INSERT the preloader.js code

    We're maintaining a mapping here so that the representation can update
    from the API but we continue to favour locally cached files.

With this build process in place all our packages include the latest
representations and images from the API. Of course it's not all perfect, now
our build process depends on the API being available and the time to build has
increased by a few seconds.

