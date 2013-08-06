Flexible Masonry layout purely with CSS
=======================================

:date: 2013-08-2 18:00
:tags: m.ox, design, masonry, css
:category: Mobile Oxford
:slug: flexible-masonry-css
:author: Dave King
:email: david.king@it.ox.ac.uk
:summary: How to create a flexible masonry style layout with pure CSS.

So we (perhaps) all know about `masonry <http://masonry.desandro.com/>`__ an
immensely popular JavaScript library which allows us to style our pages into
a dynamic grid-layout.

With the new Today view in Mobile Oxford we wanted a dynamic grid-layout and
masonry was our first port of call. We weren't too happy with the idea of
bundling another stack of JavaScript libraries into Mobile Oxford. Especially
for users on a mobile connection this can be quite a large overhead, more so
since it's likely these users wouldn't even benefit from the grid style layout
due to screen proportions.

We tried a few masonry alternatives which have fewer dependencies but none of
them really impressed us. Our requirements were slightly different than what
these libraries catered for. We were happy for all our *tiles* to be the same
width. Most of the libraries we found calculated the whitespace and resized
your tiles to fit that area.

Finally we stumbled upon a blog post from `Radu Chelariu
<https://twitter.com/sickdesigner/>`__ titled `"Masonry in CSS"
<http://sickdesigner.com/masonry-css-getting-awesome-with-css3/>`__. Which
describes a dynamic grid-layout making use of CSS3's columns. Now CSS3 columns
aren't *that* widely supported, but we're targeting mobile where support is
quite good. This functionality was intended for styling blocks of text into a
magazine or journal style column layout. However it works just fine for styling
``inline-block``'s. Radu's solution didn't quite give us the effect we were
after but with a few changes we got something we're happy with.

.. image:: |filename|/images/today-columns.png

Our Solution
------------

See the `pertinent code in this jsFiddle <http://jsfiddle.net/J3UFY/6/>`__
(expand and contract the result to see the effect).

See it live on `Mobile Oxford <http://new.m.ox.ac.uk>`__.

Similar to the method shown by Radu's blog post we are also using CSS3 columns.
We're using a slightly different CSS declaration, rather than ``column-count``
(which specifies how many columns to render) we use ``column-width`` which
specifies a width for the columns and allows the browser to place as many
columns as will fill the containing element.  Giving a ``min-width`` as a % to
our ``inline-block``'s keeps the columns flexible and doesn't leave large
amounts of whitespace between them. Additionally if the device doesn't have
support for CSS3 columns the layout will fallback to a single column view,
which is generally OK for us as again, we're mostly dealing with phones.

We're quite happy with this solution for now, let us know what you think.
