ESXi on a GSA (or, installing ESXi from USB key)
################################################
:date: 2010-12-16 16:31
:author: Chris Northwood

Not really a Mobile Oxford or Molly post this time - but all good
services need servers to run off, and Mobile Oxford is no different.
We've recently freed up a server (a former Google Search Appliance,
which is a rebadged Dell PowerEdge 2950), however installing VMWare ESXi
server onto it wasn't so straight forward. First off, a GSA doesn't have
an optical media drive, and our initial attempts to install it off a USB
drive were for naught, mainly because we prepared the USB drive wrong.
So, these were the steps that worked for us:

-  Install Unetbootin (but not a recent version of it, something from
   the 3.x series will do)
-  If you're on Linux, make sure you have a 3.x version of SYSLINUX (4.x
   doesn't work)
-  Use Unetbootin to install the ESXi ISO onto your USB key
-  Go into your key, and `alter the syslinux.cfg file and add a ks.cfg
   as detailed in this blog post`_
-  You can also get an error relating to sectors, `this blog post
   describes how to solve it`_.
-  Check that virtualisation is all turned on in the BIOS, and it's set
   to boot from your USB key

And it's as simple as that!

.. _alter the syslinux.cfg file and add a ks.cfg as detailed in this blog post: http://benincosa.org/blog/?p=171
.. _this blog post describes how to solve it: http://www.ivobeerens.nl/?p=699
