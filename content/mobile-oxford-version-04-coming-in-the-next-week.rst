Mobile Oxford version 0.4 coming in the next week!
##################################################
:date: 2010-12-16 11:39

We'll soon be releasing a new major release of Mobile Oxford, this will
bring in many new features, bug fixes and changes in code structure to
improve quality and sustainability of the Molly Project.

Quick list of improvements:

Changes to Mobile Oxford in version 0.4
---------------------------------------

Weblearn
~~~~~~~~

Polls
^^^^^

-  Public Polls now votable without authentication
-  Polls which allow multiple responses will now work
-  Polls which you are not allowed to see the results of will now work

Authentication
^^^^^^^^^^^^^^

-  Fixed a bug where oAuth authentication occasionally looped around
   from external service (weblearn) a random number of times
-  Better handling of Weblearn errors and privileges

New Transport Page
~~~~~~~~~~~~~~~~~~

-  We're launching a new transport page which will aggregate a bunch of
   useful travel information including Oxford live rail departures, the
   number of free spaces in each of the five Park and Rides, real time
   bus info from the five nearest bus stops (or your favourite bus
   stops) and BBC Road Travel Alerts.

Podcasts
~~~~~~~~

-  ePubs are now detected and downloadable

Favourites Feature
~~~~~~~~~~~~~~~~~~

-  You can now add favourite places which are displayed on the front
   page and if bus stops will be displayed on the transport page

Search
~~~~~~

-  Fixed a silent bug which missed a couple of search results
-  Search now allows use of Unicode (which used to cause a 500 error)
-  Library search now accepts Unicode characters

Places
~~~~~~

-  Minor restyling to match Podcasts
-  Park and Ride spaces now shown on Park and Ride POI page
-  Railway Stations for the whole country are now visible and their real
   time departure boards
-  You can now click on a train service and see where it stops in text
   and on a map
-  You can now choose favourite places which show up on the front page
-  Points of interest can have 'associated' entries, e.g. a Park and
   Ride will have associated bus stops
-  Oxontime bus stop numbers are now displayed bus stop pages

Front Page
~~~~~~~~~~

-  Favourite places now displayed on front page
-  River status no longer displays misleading 'Correct as of X min ago'

Backend Improvements
~~~~~~~~~~~~~~~~~~~~

-  Caching header improvements should improve responsiveness of site
-  Opera Mini users get a warning not to use 'Mobile' view as it is the
   spawn of the devil (makes silly assumptions about HTML)
-  Feature phones now get slimmed down HTML again
-  More robust handling of certain race conditions
-  Various improvements to adhere to HTML standards

Check out a full list of improvements on the Mollyproject wiki at:
https://github.com/mollyproject/mollyproject/wiki/Changelog-0.4
