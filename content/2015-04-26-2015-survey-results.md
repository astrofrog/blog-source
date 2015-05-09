Title: Python 3 in Science: the great migration has begun!
Date: 2015-05-09
Category: Coding
Tags: Python
Author: Thomas Robitaille
Slug: 2015-survey-results

Back in 2012, [I carried out a survey](http://astrofrog.github.io/blog/2013/01/13/what-python-installations-are-scientists-using/) to find out which Python, NumPy, and
SciPy versions scientists are currently using for their daily work, in order
to better understand which versions should be supported. The main finding was that a large fraction of people have
reasonably up-to-date Python installations, although virtually no-one was
using Python 3 for daily work.

This year, I decided to repeat the experiment: last January
I advertised a survey which asked users to provide information
about their Python installation(s) for research/production work, as well as
more general information about their Python experience, which packages they
used regularly, why they are not using Python 3 if they were still using
Python 2, and so on.

There is a *lot* to be learned from this data, and there is no way that I can
cover all results in a single blog post, so instead I will focus only on a
few points in this post, and will write several more posts over the next
couple of weeks to highlight various other results.

For this post, I thought it would be fun to take a look specifically at what
Python versions users in the scientific Python community are using, and in
particular, the state of Python 3 adoption.  I am making an anonymized
and cleaned-up version of the subset of the data used in this post in [this](https://github.com/astrofrog/scientific-python-survey-2015) GitHub repository, and will add to the data over time with future blog posts.


<!-- more -->

The survey
----------

Before I go ahead, just a few details about the survey. To start with, I
asked respondents to provide information about their primary Python
installation for research/production work, gave the option to provide
information about a second and third installation they use regularly, also
for research/production work (not for development). The information collected
about the different Python installations was:

* Their operating system
* The full version numbers for Python, NumPy, SciPy, and Matplotlib
* Their regularly used installation method/manager (e.g. pip, conda, etc.)

In addition, I asked general questions (not specific to a given Python
installation), for example:

* What scientific Python packages do they use?
* How long have they been using Python for?
* If they are not using Python 3, why not?
* How did they find out about the survey?
* Did they take the 2012 survey?

In total, there were 786 responses to the survey, far more than I had
anticipated, and more than twice the number of respondents in 2012 (313)! The
results below include 781 responses, because 5 of the responses were partially
invalid or problematic.

Let's now dive in and take a look at some of the results!

Demographics
------------

We can start off by taking a quick look at the demographics of surveyed
users, and in particular the field of work:

![field]({filename}/images/survey_plots/fields.svg)

Note that one respondent could select multiple fields, so the percentages add up to more than 100%. In addition, I clearly left out several important branches (such as Computer Science and Mathematics) which explains the 19% of 'Other' respondents. I did my best to advertise the survey beyond Astronomy, but there were some very effective advertising channels for Astronomers (for instance, there is a Facebook group with over 8,000 professional Astronomers, a significant fraction of all Astronomers worldwide!) which explains the bias.

Another piece of information we have is how long people have been using Python for:

![field]({filename}/images/survey_plots/experience.svg)

The bins are not all the same width, but this shows that we have a nice mix, ranging from very experienced to very new users. This information will come in handy in the next section :)

Python versions
---------------

Now let's get to the main point of this post which is to look at what fraction of users are using different Python versions for their *primary* installation:

![python versions]({filename}/images/survey_plots/python.svg)

There are a few interesting things to notice here. Firstly, **most users are using either Python 2.7 or 3.4**, very few users are
using Python 2.6 and 3.3, and virtually no one uses Python 3.1, and 3.2. This
has clear implications for which Python versions package developers need to
support. Based on this, I would argue that only Python 2.7 and 3.4 really
need to be supported - Python 2.6 as well as 3.1 and 3.2 can essentially be
dropped (I think that Python 3.3 should still be supported because as a
fraction of Python 3 users, it's not negligible, and it is a recent
enough release, but I think that once Python 3.5 is out, we can already consider no longer supporting 3.3)

Secondly, over 17% of respondents use Python 3 as their **primary** Python
installation. In fact, if we
look at the exact statistics from the data, we find that 17.4% of users use
Python 3 as their primary installation, and 2.8% use it as a secondary
installation, which means that around 20.2% of users are now actively using
Python 3 on a regular basis.  While this is a little low, remember that in the 2012 survey,
virtually no one used Python 3 as their primary installation, which is not too surprising because at the time, not all of the core Scientific Python packages were fully functional in Python 3. Now that all core packages support Python 3 fully, it's nice to see that we've gone from essentially 0% to 20% in only a couple of years.

Let's now take a quick look at operating systems:

![os]({filename}/images/survey_plots/os.svg)

The Linux/Mac split is not surprising, but this shows that almost 10% of
Scientific Python users are on Windows, which is not negligible. Thankfully,
services like [AppVeyor](http://www.appveyor.com/) now make it easy to set up
continuous integration/testing for packages on Windows, so it's becoming
easier to support this community.

Now for an unexpected (at least for me) result relating to operating systems. The
following plot is normalized by rows (i.e. the sum of each row is 100%) to show, for each operating system, the
distribution of Python versions:


![python vs os]({filename}/images/survey_plots/os_vs_python.svg)

Yes, that's right, Windows users are the most up-to-date when it comes to Python
versions – almost 40% of Windows users are using Python 3! Mac users on the
other hand are the most conservative, with almost 90% sticking to Python 2.7.
At this point, I'm not sure what the difference is due to, but I'd be
interested in hearing your thoughts in the comments! There may be information in the
full dataset that can help us answer that – in particular, I have a suspicion
it could be related to installation methods for Python and default Python
versions available on Linux and MacOS X (whereas Windows users always have to
install Python themselves).

So **why** do some users not use Python 3? Here's the breakdown of the main
reasons, for the 80% or so of users whose primary Python version is 2.6 or
2.7 (note that one user can select several of these answers):

![python3]({filename}/images/survey_plots/why_not_python3.svg)

Almost two thirds of users who are still using Python 2 do not have any
motivation to update to Python 3. This is essentially what Jake Vanderplas
[wrote about](https://jakevdp.github.io/blog/2013/01/03/will-scientists-ever-move-to-
python-3/) two years ago – to quote him in that blog post, *I'd do it myself
[switch to Python 3], but I'm too much of a pragmatist: python 2.7 is more
than sufficient for my own research*.

Now I can certainly understand this argument, and I always
find it difficult to give concrete features in Python 3 that will benefit
users directly – of course, idealistically, unicode support by default is great because there's no reason that strings should be limited to the ASCII alphabet, but for users that don't need this, it's a harder sell. Personally, I switched to using Python 3 for a very pragmatic reason, which is the following: Python 3 is the future and we are going to have to switch to it sooner or later – **the more we put it off, the harder the transition will be!** To me, that is a good enough motivation to switch as soon as possible now that the Scientific Python ecosystem supports this.

Whether or not you agree with me that this is a good enough reason, at the very least, there really is no reason we shouldn't be *teaching*
Python 3 by default. We can still tell new users about Python 2 in case they
encounter it, but only as an aside. So let's see whether new users are preferentially using Python 3? (note: the following plot is normalized by
columns):

![python vs experience]({filename}/images/survey_plots/python_vs_experience.svg)

Hmm, no.... Actually, 6% of the newest users (<1 year) are using Python 2.6
(the most compared to other users!) and only 13% are using Python 3, **less**
than any other users. I suspect this is because new users just use whatever
Python versions are available and aren't yet aware of which versions are the
latest. Furthermore, I suspect most Python courses/workshops still use Python 2. But this is all wrong – we should be teaching new users to use Python 3! New users won't thank you if you teach them Python 2 and they have to migrate all their scripts to Python 3 in a few years... I would strongly encourage any
of you involved in teaching Python to switch now to using Python 3, *even if
you don't use it yourself* (I teach a [Python course](http://mpia.de/~robitaille/PY4SCI_SS_2015) which uses Python 3.4 at the University of Heidelberg, and everything has gone very
smoothly!)

One final suggestion I have is that we start holding Python 3 'migration clinics', where we can help users convert their code to be Python 3-compatible, and help them get set up with Python 3, either as a secondary installation, or a primary one. We can also teach users how to write code that is Python 2 and 3-compatible, using e.g. the ``__future__`` imports, as well as libraries like [six](https://pypi.python.org/pypi/six).

What can developers do?
-----------------------

I think that as developers, we can do more to encourage Python 3 adoption. In my view, one of
the mistakes of the Python 3 transition was that Python
developers backported many new and very nice features of Python 3 back to
Python 2, making Python 3 a harder sell. A couple of random examples of backported features include
[ordered dictionaries](https://docs.python.org/3/library/collections.html#collections.OrderedDict) and [dictionary comprehensions](https://docs.python.org/3.4/tutorial/datastructures.html#dictionaries). However, the Python developers have now stated that [there will be no Python 2.8 release](https://www.python.org/dev/peps/pep-0404/). Essentially, no new features are going to be added to Python 2. In fact, after 2020 (which is not *so* far in the future), Python 2 will no longer be supported.

At some point in the near future, I feel that other package developers should follow this example by having only bugfix releases on Python 2, and releasing new major versions of packages that only support Python 3. To be clear, Python 2 users will still be able to use packages for as long as they like, and no features would be taken away, but in order to get the latest and greatest, they would need to upgrade to Python 3.

Take-away points
----------------

We've only scratched the surface of the data from this survey, and already, we can see several interesting things:

* It's pretty safe to say that developers can now drop support for Python
  2.6, 3.1, and 3.2. Python 3.4 is far more popular than Python 2.6, and so it's much more important to make sure we support the former than the latter.

* We should not under-estimate the fraction of Windows users in the
  Scientific Python community (almost 10%). Supporting these users is now
  made easier by online continuous integration services running Windows.

* Python 3 is catching on, with over 17% of people using it as their primary
  installation, and over 20% if we include people who use it as a secondary
  installation, compared to essentially 0% a couple of years ago.

* The main reason for Python 2 users to not switch to Python 3 is the lack of
  motivation/killer features. We need to therefore be more proactive in
  encouraging people to switch to Python 3 (a) by making sure that any new users are always directed to the latest Python 3 version, and (b) by releasing, in the near future, new major versions of packages for Python 3 only, while maintaining long term bugfix support for Python 2 versions.

Let me know if you have any thoughts on these results so far in the comment section below!

