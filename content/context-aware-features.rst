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
want to make the best use of native functionality where it's available whilst
maintaining a high quality experience across all platforms.  Recently we've
been making use of some native features and thought it was worth writing a blog
post about how we tweak these features based upon the context of the user.

User context could consist of many things. Platform, device capabilities, form
factor, are they a student or staff? Do they live within the Oxford ring-road
or further afield? All these factors are interesting to us for our application.

For the purposes of these features the only factor currently impacting
behaviour is the platform the user is using. In our case, Web, iOS and Android.

Contact Search
--------------

This feature allows users to search the LDAP of the University to find phone or
email contact information for members of staff. Once the user has found the
contact they are searching for they can send an email or phone that individual.
This is done by directing the user to URLs with have mailto and tel schemes
respectively. Really we want users to be able to save these contacts directly
to their phonebook without having to copy and paste numbers, emails and names.

Natively this is straightforward, through the phonegap API's we can update the
user's phonebook on their behalf. However many users aren't using the native
applications, on the web how would this feature look? We thought it would be
analagous to download a vCard for that contact. Now if the user has an
application installed which can process vCards like Outlook, OSX Address Book
they can add the vCard as a contact. In terms of implementation this meant a
bit of work as we needed to build the vCards on client and download using HTML5
features.

University Events
-----------------

Within Mobile Oxford we list many events happening today and later in the week.
We'd like for users to be able to simply add an event to their calendar.
Implementtion for the native functionality is a straightforward couple of API
calls and a callback with Phonegap.

For web users we thought the obvious solution here was to allow users to
download an iCalendar file for each event. Unlike the vCards which we build on
the client we decided to add ``text/calendar`` content negotiation to our API
and direct users there to download the .ics file.
