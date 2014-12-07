Title: The Acknowledgment Generator
Date: 2014-12-07
Category: Coding
Tags: dotastro
Author: Thomas Robitaille
Slug: acknowledgment-generator

This week, the 6th installment of the [.Astronomy](http://dotastronomy.com/)
conference series will be taking place in Chicago. I will unfortunately not be
attending this year, but I was nevertheless motivated today to try and finish
up a hack that started as a result of discussions with
[Niall Deacon](https://twitter.com/nialldeacon) before and at
[.Astronomy 5](http://dotastronomy.com/events/five/) in Boston!

The idea is simple: as I described in a [blog post](http://astrofrog.github.io/blog/2013/10/02/acknowledging-tools-services-in-papers/)
last year, we are not doing good job at acknowledging the tools
that we use for our research, which in turn means that many people who spend
time developing tools for the community are not getting the credit they deserve.
(how to give credit to people for non-traditional work in academia is a
recurring theme of .Astronomy meetings).

<!-- more -->

Enter the [Acknowledgment Generator](http://astrofrog.github.io/acknowledgment-generator/),
a new tool to make it easier for the laziest of us to generate in just a few
clicks the list of acknowledgments that should go at the end of a paper or on a
website! This includes options to show LaTeX-friendly output and BiBTeX
references. At this point, this is a proof of concept, and only very few
examples of codes, facilities, or resources are included...

... and this is where I need *your* help: we can crowd-source the collection of
the information needed for the database of entries! The website and the
database of entries are kept in a
[GitHub repository](https://github.com/astrofrog/acknowledgment-generator)
so anyone can go and make changes to the website, and add or modify entries.
Any contribution helps, and your name will of course be listed as a contributor :)

In fact, no [git](http://git-scm.com/) expertise is required to help. Take a
look at the instructions I have written
[here](https://github.com/astrofrog/acknowledgment-generator#i-want-to-help)
which describe how you can add a new entries with just a few clicks, and also
gives details of how you can send me entries if all else fails.
If you have ideas of how to make this website better, you can also comment on
this blog post, or even better, open an issue
[here](https://github.com/astrofrog/acknowledgment-generator/issues)!

Finally, I would also very much welcome any help in implementing new features
into the website itself. I am still a javascript newbie, so there are a lot of
low-hanging fruit if you are interested in helping out! The full list of issues
is available [here](https://github.com/astrofrog/acknowledgment-generator/issues).


