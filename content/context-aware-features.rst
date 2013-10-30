Context Aware Features
======================

:date: 2013-10-28 15:50
:category: Mobile Oxford
:slug: context-aware-features
:author: Dave King
:email: david.king@it.ox.ac.uk
:summary: We've recently added a couple of features to Mobile Oxford which
          react to the context in which they run.

Now we are packaging `Mobile Oxford <http://new.m.ox.ac.uk>`__ for iOS (coming
soon!) and `Android
<https://play.google.com/store/apps/details?id=uk.ac.ox.it.mobileoxford>`__ we
want to provide the best experience to all platforms. Sometimes this is a piece
of native functionality which can't be expressed through web APIs so we have
find ourselves having to adjust the feature slightly to keep feature parity
regardless of the user's context. This can consist of many things, platform,
device capabilities, form factor, are they a student or staff? Do they live
within the Oxford ring-road or further afield? All these factors are
interesting to us for our application.

For the purposes of these features the only factor currently impacting
behaviour is the platform the user is using. In our case, Web, iOS and Android.

Contact Search
--------------

`This feature <http://new.m.ox.ac.uk/#contacts/search>`__ allows users to
search the LDAP of the University to find phone or email contact information
for members of staff. Once the user has found the contact they are searching
for they can send an email or phone that individual.  This is done by directing
the user to URLs with have mailto and tel schemes respectively. Really we want
users to be able to save these contacts directly to their phonebook without
having to copy and paste numbers, emails and names.

Natively this is straightforward, through the `Cordova APIs
<http://cordova.apache.org/docs/en/3.1.0/cordova_contacts_contacts.md.html#Contacts>`__
we can update the user's phonebook on their behalf. However many users aren't
using the native applications, on the web how would this feature look? We
thought it would be analagous to download a `vCard
<http://tools.ietf.org/html/rfc6350>`__ for that contact. Now if the user has
an application installed which can process vCards such as Outlook, OS X Address
Book, they can add the vCard as a contact. In terms of implementation this
meant a bit of work as we needed to build the vCards on client and download
using HTML5 features.

University Events
-----------------

Within Mobile Oxford we `list many events <http://new.m.ox.ac.uk/#events/>`__
happening today and later in the week. We'd like for users to be able to simply
add an event to their calendar. Implementtion for the native functionality is a
straightforward couple of API calls and a callback with Phonegap.

For web users we thought the obvious solution here was to allow users to
download an `iCalendar file <http://tools.ietf.org/html/rfc5545>`__ for each
event. Unlike the vCards which we build on the client we decided to add
``text/calendar`` content negotiation to our API and direct users there to
download the .ics file. Something we couldn't do for contact search as we don't
have a unique handle on each contact.


Other Features
--------------

For these two features it seems quite straightforward to provide alternative
behaviours for the web. Other features may not be so simple to adjust based on
user context. As we target an increasingly broad-range of devices and platforms
as such keeping the user context in mind becomes more important. Now we adjust
features we have to update the help text which goes alongside that, perhaps
even change the icons and other UI elements.

At times making these kinds of branches in behaviour feels like a battle you
can never win. Earlier this year I attended a talk by `Ade Oshineye
<http://www.oshineye.com/>`__ who `spoke about user context
<https://speakerdeck.com/adewale/identity-responsiveness-and-the-future-of-the-web>`__
in a similar way to us and even went as far to suggest adjusting application
behaviour based on user bandwidth. Thankfully that doesn't seem necessary for
Mobile Oxford just yet.
