Context Aware Features
======================

:date: 2013-10-28 15:50
:category: Mobile Oxford
:slug: context-aware-features
:author: Dave King
:email: david.king@it.ox.ac.uk
:summary: We've recently added a couple of features to Mobile Oxford which
          react to the context in which they run.

Since we target the Web as well as Android and (soon) iOS with Mobile Oxford we
want to make the best use of native functionality where it's available. However
we don't want to make Web users second class citizens. Recently we've been
making use of some native features (through Phonegap) and thought it was worth
writing a blog post about how we're gracefully adjusting the features depending
on the user context.

Firstly we've been improving the contact search function. This allows users to
search the LDAP of the University to find phone or email contact information
for members of staff. Once the user has found the contact they are searching
for they can send an email or phone that individual. Obviously on the web we
have mailto and tel URL schemes for this which works across most platforms.

