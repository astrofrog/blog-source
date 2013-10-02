Title: Are we acknowledging tools and services enough in Astronomy papers?
Date: 2013-10-02 12:57
Category: Coding, Publications
Tags: Python, Data mining
Author: Thomas Robitaille
Slug: acknowledging-tools-services-in-papers

A couple of weeks ago, I attended the 5th
[.Astronomy](http://dotastronomy.com/) meeting, which took place in Boston. For
anyone not familiar with this series of conferences, the aim is to bring
together researchers, developers, and educators/outreach specialists who 
use or are interested in using the web as a tool for their work (I like to
think of it as an astro-hipster conference!).

One of the topics that comes up regularly at .Astronomy meetings is the
question of credit: how do we, as scientists, get credit for work that is not
considered 'traditional', such as (but not limited to) creating or contributing
to open source software, outreach activities, or refereeing?
[Sarah Kendrew](http://twitter.com/sarahkendrew) already summarized the
discussions on this topic in [her blog](http://sarahaskew.net/2013/10/01/astronomy-5-share-the-love/), so I won't
repeat them here. However, given that I contribute to a number of open source
projects (such as [Astropy](http://www.astropy.org),
[APLpy](http://aplpy.github.io), and many others) this got me wondering 
how often authors actually acknowledge the tools that they use in papers?

I previously played around with the [NASA/ADS](http://adsabs.harvard.edu/)
full-text search, but what I wanted was a way to be able to do this
automatically for any keyword/phrase, and be able to see the evolution of
acknowledgments over time. With the release of the [ADS developer API](https://github.com/adsabs/adsabs-dev-api) (which
[Alberto Accomazzi](http://twitter.com/aaccomazzi) presented on the Monday at
.Astronomy), I finally had the tool I needed to do this! This was a fun
post-dotastro hack, for which I now present the results below.

<!-- more -->

The code
--------

Since not everyone reading this will be interested in the code I used to do
this, I have placed it in a separate IPython notebook [that you can access here](http://nbviewer.ipython.org/urls/raw.github.com/astrofrog/mining_acknowled
gments/master/Mining%2520acknowledgments%2520in%2520ADS.ipynb). Please feel
free to fork and contribute to it!

The results
-----------

Let's start off by looking at how often [ADS](http://adsabs.harvard.edu/)
itself is acknowledged. The suggested acknowledgment phrase includes
*Astrophysics Data System*, so we will search for that:

![ADS]({filename}/images/mining_ack/ads_final.png)

This shows that more and more people are acknowledging ADS, but that even now
this represents less than 1% of all papers! Of course, many people, myself
included (until now), use ADS without thinking about acknowledging it, but this
illustrates to what extend we are under-acknowledging what we use to do our
research and write papers.

Let's move on to common online databases, such as
[Simbad](http://simbad.u-strasbg.fr/simbad/),
[Vizier](http://vizier.u-strasbg.fr/viz-bin/VizieR), and
[NED](http://ned.ipac.caltech.edu):

![online databases]({filename}/images/mining_ack/databases_final.png)

I want you to take a look at the y scale. At most **0.17%** of refereed papers
currently acknowledge using SIMBAD. Now I know there are quite a few theorists
out there, but this is a little on the low side... As was the case for ADS,
it's encouraging to see that the fraction is increasing over time, but if we
extrapolate the increase since the year 2000, it will take another **two
thousand years** before 10% of papers acknowledge the use of SIMBAD (and I'm
sure the real value should be higher).

Moving on to programming languages:

![programming languages]({filename}/images/mining_ack/programming_final.png)

The fractions are even smaller than the online databases above, although in all
fairness there is no requirement to acknowledge programming languages directly,
so I will not complain about this. What is interesting though are the trends.
IDL and Fortran both see a large drop in fraction of acknowledgments this year,
while mentions of Python have seen a sharp increase from almost none around
2005 to more than any of the other languages shown here. While this is a poor
metric of which languages people are actually using, it does show that the
uptake of Python over the last few years is very encouraging!

Finally, let's wrap up with a few common tools:

![tools]({filename}/images/mining_ack/tools_final.png)

Again, the fractions are far too low compared to the real usage, but the trends
are again very instructive. [IRAF](http://iraf.noao.edu/) and
[Starlink](http://starlink.jach.hawaii.edu/starlink) are now past their peak,
 while
[Ds9](http://hea-www.harvard.edu/RD/ds9/site/Home.html),
[Aladin](http://aladin.u-strasbg.fr/), and
[Topcat](http://www.star.bris.ac.uk/~mbt/topcat/) are all on the rise!

Take-home message
-----------------

Most of the services and tools I have shown results for above actually have
standard phrases that you can add to the acknowledgment section of your
latest paper, but it's clear that most papers are not following these
guidelines. This is a severe problem because for some of these projects,
funding may be dependent on the level of use, and for volunteers it may be the
only way they can get credit for their work.

People may ask where acknowledgments should stop - should also acknowledge
LaTeX, Apple, or the use of Fourier transforms? Of course not. In my view, the
line should be drawn at the point where we think that these acknowledgments
matter and will make a difference to projects in our community. All of the
examples above are ones that should be acknowledged, and it is also crucial
that you think of acknowledging smaller software packages that you use,
especially if the developers have provided a standard phrase. Yes, your
acknowledgment section may become quite long, but this is not about esthetics -
it is something that may make a real difference to some of these projects.

Of course, you don't want to spend hours searching around for all the possible
acknowledgments on the web, but fear not! AstroBetter now hosts an [acknowledgment wiki](http://www.astrobetter.com/wiki/tiki-index.php?page=Acknowledgements) on
which you will find many acknowledgments - this list is far from exhaustive, so
please add to it any acknowledgment you are aware of!

In the mean time, what do you think about the low fractions of acknowledgments?
How can we encourage more people in our community to fairly acknowledge the
tools and services we use?







