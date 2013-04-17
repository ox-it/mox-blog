News Section Re-skin
####################
:date: 2010-11-30 14:48

The initial problem was that the news section design didn't sit well
with other sections like Podcasts. The layout of elements and the use of
colour was not felt to be making the best use of the possibilities and I
began to look at how the design could be made more unified and
consistant and at what quick wins could be implemented to give the
design a bit more visual impact.

The First, and relatively trivial task was to amend the page templates
involved in the news section so that they used the same CSS for section
title and article text as the equivalent elements in the Podcast
section. I did this and pushed the changes to git as part of the
Bigcleanup branch. These changes have already been merged to the live
site and the section now at least looks more like it belongs with the
others.

Surveying other news and news-like sites though suggests that we may be
missing a trick or two. Some example of mobile news sites are the BBC
News native iPhone app, The mobile version of iPlayer. Google Reader's
mobile version, and IMDB.

These sites all give a positive and usable mobile experience and have
some common features which we could learn from. With the exception of
the Google Reader site they all reserve a small amount of space at the
top of the page to display the title and nothing else (the BBC News site
does also use this space to display a couple of controls, but, as a
native app rather than a mobile site it is able to do this more easily).
They all make use of colour to a greater or lesser extent, to highlight
important navigational or functional aspects of the current page (see
particularly the iPlayer's somewhat eye-popping pink and how well that
highlights important info against the dark/black background). The all
make full use of the screen real estate, particularly the page width, to
display content.

I think we could quite easily add a little more colour to the site -
judicious, but subtle accent colours - to not only make the design a
little more lively, but to draw the eye to important page elements. I
think where the current news section design lets itself down somewhat is
in not making use of the entire screen width. I can see that the nice,
rounded corner boxes have a certain aesthetic appeal, but those few
pixels they lose to either side are more valuable perhaps than they
would be in an equivalent desktop site. Pushing the width out like this
though, would have a knock on effect on the design of the section
headers which would lose their rounded corners and drop shadows. I would
propose either switching the section title with the subsequent links to
give a dark blue title with white/pale grey links beneath or (or
possibly and) a subtle gradienton the section title to bring it forward
a bit.

On the subject of colour, I have a couple of examples of its effective
use from non-news mobile sites.

The basic scheme  of the Mobile Oxford site is a rather monochromatic
blue and grey-blue and the brown accent colour (which is actually
slightly off in terms of where the natural compliment to the main blue
would fall on a colour wheel) is used in a way which dissipates it's
impact as an accent, and it becomes a seemingly rather odd choice of
alternate background colour. While I appreciate that monochrome colour
schemes translate better to a range of devices and degrade more
gracefully to greyscale, I think that we can learn from how others have
used colour in the same context.

The BrightKite, Meebo, Mailchimp and Viget sites all use a similar
palette to ours. Meebo and Viget have the overall blue being highlighted
by a lively orange. At the sub-page level they drop back, wisely I feel,
to a plain white background. The orange used by Meebo and Viget is the
bog standard complimentary colour to the dominant blue. BrightKite have
gone a slightly different route and used one of the accent colours from
an analogic triad - in this case a rather lurid (in isolation) green.
The Mailchimp site uses a similar palette, but reverses main and
highlight colours.

