Title: Scientific Python Users: Python 2 vs Python 3
Date: 2015-05-09
Category: Coding
Tags: 
Author: Thomas Robitaille
Slug: 2015-survey-results

Back in 2012, I carried out a survey to find out which Python, NumPy, and
SciPy versions scientists are currently using for their daily work, in order
to better understand which versions should be supported. I published the
results in a
[blog post](http://astrofrog.github.io/blog/2013/01/13/what-python-installations-are-scientists-using/), and the main finding was that a large fraction of people have
reasonably up-to-date Python installations, although virtually no-one was
using Python 3 for daily work.

Two years later, I decided to repeat the experiment, in order to measure
changes over time, as well as collect a wider variety of information about Python installations and Scientific Python users. In
January this year I advertised a survey which asked users to provide
information about their Python installation(s) for research/production work,
as well as more general information about their Python experience, which
packages they used regularly, why they are not using Python 3 if they were
still using Python 2, and so on.

There is a *lot* to be learned from this data, and there is no way that I can
cover all results in a single blog post, so instead I will focus only on a
few points in this post, and will write several more posts over the next
couple of weeks to highlight various other results. For this post, I thought
it would be fun to take a look specifically at what Python versions the
scientific Python community is using. Let's dive in!


<!-- more -->

The survey
----------

Before I go ahead, just a few details about the survey. To start with, I asked respondents to provide information about their primary Python
installation for research/production work, gave the option to provide
information about a second and third installation they use regularly, also
for research/production work (not for development). The information collected
about the different Python installations was:

* Their operating system
* The full version numbers for Python, NumPy, SciPy, and Matplotlib
* Their regularly used installation method/manager (e.g. pip, conda, etc.)

In addition, I asked general questions (not specific to a given Python installation), for example:

* What scientific Python packages do they use?
* How long have they been using Python for?
* If they are not using Python 3, why not?
* How did they find out about the survey?
* Did they take the 2012 survey?

In total, there were 786 responses to the survey, far more than I had
anticipated, and more than twice the number of respondents in 2012 (313)!

Now for the results!

Python versions
---------------

Let's start off by taking a look at what fraction of users are using different Python versions and see where that takes us:

![python versions]({filename}/images/survey_plots/python.svg)

There are a few interesting things to notice here. Firstly, **most users are using either Python 2.7 or 3.4**, very few users are
using Python 2.6 and 3.3, and virtually no one uses Python 3.1, and 3.2. This
has clear implications for which Python versions package developers need to
support. Based on this, I would argue that only Python 2.7 and 3.4 really
need to be supported - Python 2.6 as well as 3.1 and 3.2 can essentially be
dropped (I think that Python 3.3 should still be supported because as a
fraction of Python 3 users, it's not negligeable, and it is a recent
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

This is not really unexpected, though it does show that almost 10% of
Scientific Python users are on Windows, which is not negligeable. Thankfully,
services like [AppVeyor](http://www.appveyor.com/) now make it easy to set up
continuous integration/testing for packages on Windows, so it's becoming
easier to support this community.

Now for an unexpected (at least for me) result relating to operating systems. The
following plot is normalized by rows to show, for each operating system, the
distribution of Python versions:


![python vs os]({filename}/images/survey_plots/os_vs_python.svg)

Yep, that's right, Windows users are the most up-to-date when it comes to Python
versions - almost 40% of Windows users are using Python 3! Mac users on the
other hand are the most conservative, with almost 90% sticking to Python 2.7.
At this point, I'm not sure what the difference is due to, but I'd be
interested in hearing your thoughts in the comments! There may be information in the
full dataset that can help us answer that - in particular, I have a suspicion
it could be related to installation methods for Python and default Python
versions available on Linux and MacOS X (whereas Windows users always have to
install Python themselves).

So **why** do some users not use Python 3? Here's the breakdown of the main
reasons, for users whose primary Python version is 2.6 or 2.7 (note that one
user can select several of these answers):


![python3]({filename}/images/survey_plots/why_not_python3.svg)

Almost half of users who are still using Python 2 do not have any motivation
to update to Python 3. Now I can certainly understand this argument, and I always
find it difficult to give concrete features in Python 3 that will benefit
users directly - of course, in non-native English-speaking countries, having
the unicode support by default in strings is a nice feature, but
pragmatically, for users that don't need unicode, it's a harder sell. In my view, one of
the mistakes of the Python 3 transition was that the Python
developers backported many new and very nice features of Python 3 back to
Python 2, making Python 3 a harder sell. Examples of backported features include
[ordered dictionaries](https://docs.python.org/3/library/collections.html#collections.OrderedDict) and [dictionary comprehensions](https://docs.python.org/3.4/tutorial/datastructures.html#dictionaries).

At this point, we are stuck in a loop - while developers keep supporting
Python 2, and make sure that most features are available in Python 2, users
will have no motivation to update to Python 3. Therefore, many users will
keep using Python 2, so developers will continue to support it. And this is
where I think we are doing it wrong. **We should not wait for the majority of
users to use Python 3 before developing Python 3-only features**. To be clear, I'm not saying we drop all support for Python 2. But at some point, I
think we are going to have to say that any future **major** release of
packages will be Python 3-only, and only bug fix releases will be done for
Python 2. Yes, this will mean supporting two parallel branches, but many
packages do this anyway - we often support both a bug-fix branch for the last
stable release, and a developer branch where we implement new features. It's
now time we start developing some features that we can point users to as a clear
benefit of switching to Python 3!

This is only part of the solution however. Now that the Scientific Python ecosystem for Python 3, there really is no reason we
shouldn't be *teaching* Python 3 by default. We can still tell them about Python 2 in case they encounter it, but only as an aside. Is that the case? Are new users being taught Python 3?

![python vs experience]({filename}/images/survey_plots/python_vs_experience.svg)

Um, no.... Actually, 6% of the newest users (<1 year) are using Python 2.6
(the most compared to other users!) and only 13% are using Python 3, **less**
than any other users. I suspect this is because new users just use whatever
Python versions are available and aren't yet aware of which versions are the
latest. Furthermore, I suspect most Python courses/workshops still use Python 2. But this is all wrong - we should be teaching Python 3 to new users!
I teach a [Python course](http://mpia.de/~robitaille/PY4SCI_SS_2015) at the University of Heidelberg, and as part of that
we use only Python 3.4, and everything has gone smoothly. Based on my experience, I would strongly
encourage any of you involved in teaching Python to switch now to using
Python 3, even if you don't use it yourself!

Summary
-------

We've only scratched the surface of the data from this survey, and already, we can see several interesting things:

* It's pretty safe to say that developers can now drop support for Python
  2.6, 3.1, and 3.2! This means that we can start using Python 2.7+ only
  features such as dictionary comprehensions and other fun constructs :)

* We should not under-estimate the fraction of Windows users in the
  Scientific Python community (almost 10%). Supporting these users is now
  made easier by online continuous integration services running Windows.

* Python 3 is catching on, with over 17% of people using it as their primary
  installation, and over 20% if we include people who use it as a secondary
  installation.

* The main reason for Python 2 users to not switch to Python 3 is the lack of
  motivation/killer features. We need to therefore be more proactive in
  encouraging people to switch to Python 3, by (a) providing features that
  are available only in Python 3 and that would be useful for many users (not
  just advanced features), and (b) making sure that any new users are always
  directed to the latest Python 3 version.

Let me know if you have any thoughts on these results so far in the comment section below!