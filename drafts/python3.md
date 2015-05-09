Epilogue: What can developers do?
---------------------------------

In [Jake's blog post](https://jakevdp.github.io/blog/2013/01/03/will-scientists-ever-move-to-python-3/) two years ago, he mentioned that developers should be moving to developing in Python 3 and using a 3to2-type tool to support Python 2. Actually what we've seen is more promising, which is the appearence of code bases that are Python 2 and 3-compatible by default, using e.g. [six](https://pypi.python.org/pypi/six) to make things easier.

I can't help feel that we (as developers) should be doing more to encourage Python 3 adoption. In my view, one of
the mistakes of the Python 3 transition was that CPython
developers backported many new and very nice features of Python 3 back to
Python 2, making Python 3 a harder sell. Examples of backported features include
[ordered dictionaries](https://docs.python.org/3/library/collections.html#collections.OrderedDict) and [dictionary comprehensions](https://docs.python.org/3.4/tutorial/datastructures.html#dictionaries).

While developers keep supporting Python 2, and make sure that all features
are available in Python 2, users will have no motivation to update to Python
3. Therefore, many users will keep using Python 2, so developers will
continue to support it. Instead, I think that **we should not wait for the majority of users to use Python 3 before developing Python 3-only features**. To be clear, I'm not saying we drop all support for Python 2. But at some
point (and it doesn't *have* to be now, but it will have to happen),
we are going to have to say that any future **major** release of packages
will be Python 3-only, and only bug fix releases will be done for Python 2.
Yes, this will mean supporting two parallel branches, but many packages do
this anyway – we often support both a bug-fix branch for the last stable
release, and a developer branch where we implement new features.
