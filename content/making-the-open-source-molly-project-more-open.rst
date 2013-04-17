Making the open source Molly Project more 'open'
################################################
:date: 2010-11-30 11:41
:author: Tim Fernando

Recently we've been thinking hard about how to develop the Molly project
into a true community open source project. 

Moving away from SourceForge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Molly Project has been hosted on sourceforge.net for a while now.
And whilst sourceforge gave us a wide range of tools on paper, the lack
of structure, multiple passwords and general mismatch of tools set the
bar to contributing rather high. Even we as primary contributors found
it hard to use their issue tracker.

.. image:: |filename|/images/SourceForge.net_Molly_Feature_Settings.png.scaled1000.png

So we set out to look for alternatives and the first that came to mind
was Github. After a quick analysis of alternatives we decided to settle
down there not least due to its large community of users, enhancing the
chances of our code being forked (`why forking is a good thing`_). It
also provided team and organisation tools which let us easily set up
different types of members in a project and a great lightweight issue
tracker and multi-markup wiki. Even simple things like adding READMEs in
supported markup languages means that Github will display them inline to
the project page.

.. image:: |filename|/images/Issues_-_mollyproject_mollyproject_-_GitHub.png.scaled1000.png

Of course by moving to Github, we would be losing one of the primary
reasons for going with sourceforge in the first place - mailing lists.
So we kept our three mailing lists on sourceforge but moved everything
else over.

But the longer I think about it the less I think mailing lists are
entirely necessary. We have three lists, 'users', 'developers' and
'commits'. The users' list has had all of two posts to it, the 'commits'
list has had automated commits which can now be subscribed to on github
(even in an `Atom feed`_). This left the developer list, which although
has had various ongoing discussions the chatter hasn't been as strong as
we would have liked. Of course we'll continue to keep the developer
mailing list running for the foreseeable future and it will be
interesting to see which means of sharing turns out best. 

Mailing Lists, Forum, a Knowledge Base, E-Mails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Something that rather surprised us was that some developers seem to be a
bit hesitant in using IRC or mailing lists. Perhaps these methods are
now too 'old hat'? We would often get direct email queries but very few
directed to the mailing lists which were supposed to harness the spirit
of open source.

Enter `'Tender'`_ as used by various organisations including Github
themselves. We had identified Tender as part of our on going analysis on
service management tools for Mobile Oxford. In essence it provides an
integrated support system, including email ticketing, FAQs, public
discussions (not dissimilar to forums, but with some subtle differences)
and even more excitingly, provides free accounts for open source
projects.

.. image:: |filename|/images/save_image.png.scaled595.png

In the next few days we will be launching our 'tender' at
`http://support.mollyproject.org <http://support.mollyproject.org>`_ and the aim is the have as much
developer (and perhaps management?) discussion as possible out here on
the web, where hopefully it's less scary.


Why not use your host institution's tools?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We could indeed have used the extensive tools supplied by our own
institution, but we felt it important that the Molly Project tried to
keep its own identity and reduce the chances of the project being seen
as entirely 'owned' by Oxford University. After all, we are trying to
create a true open community project.

Cleaning up code
~~~~~~~~~~~~~~~~

Mobile Oxford's initial iterations were not intended for production
service and thus the code base has evolved organically. There has been
much cruft left over from failed experiments, old systems integration
and so on. Earlier this year we set up a project with Oxford Brookes to
deploy a version of Molly for them. This proved a little hard at first,
but we made significant changes to the structure of the project to
improve portability. Now, we're making another bash at it in earnest.  

Taking from the excellent lead of a project named `Mobile Web OSP`_
(which provides similar functionality to the Molly Project but is
written in PHP) we're now working on really 'opening up' the code with
the following steps:

#. Remove as much redundant old code (cruft) as possible.
#. Reduce code dependencies.
#. Improve install scripts and reduce the entry barrier to use.

With a few hours work we managed to remove a fair bit of old and
confusing code, a few more hours and we managed to remove five Python
dependencies including one that had given several people problems in the
past (PyCairo). Whilst we carry on trimming the code, we're also writing
install scripts iteratively and will soon be making this part of a
continuous integration server.

.. image:: |filename|/images/The_mollyproject_Network_-_GitHub.png.scaled1000.png

We're aiming for two major releases in the next two months, the first
being version 0.4 which will bring a new transport application and a
number of major tweaks. Next in January 2011, we will launch version 0.9
which is currently being developed as part of the '`the big cleanup`_\ '
branch on github.

.. _why forking is a good thing: http://zef.me/3369/how-git-encourages-open-source-contribution
.. _Atom feed: https://github.com/mollyproject/mollyproject/commits/master.atom
.. _'Tender': http://tenderapp
.. _Mobile Web OSP: http://mobilewebosp.pbworks.com/
.. _the big cleanup: https://github.com/mollyproject/mollyproject/tree/thebigcleanup
