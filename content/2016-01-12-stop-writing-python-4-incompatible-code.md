Title: Stop writing code that will break on Python 4!
Date: 2016-01-12
Tags: Python
Author: Thomas Robitaille
Slug: stop-writing-python-4-incompatible-code

With the end of support for Python 2 on the horizon
([in 2020](https://www.python.org/dev/peps/pep-0373/)), many package developers
have made their packages compatible with both Python 2 and Python 3 by using
constructs such as:

    if sys.version_info[0] == 2:
        # Python 2 code
    else:
        # Python 3 code

in places where things have changed between Python 2 and 3.

<!-- more -->

The [six](https://pythonhosted.org/six/) package simplifies many of the
differences by providing wrappers that behave the same on Python 2 and 3. For
instance, iterating over dictionary keys is normally done with:

    for item in dictionary.iteritems():
        # code here
        
in Python 2 and:

    for item in dictionary.items():
        # code here
        
in Python 3. With [six](https://pythonhosted.org/six/), one can simply do:

    import six

    for item in six.iteritems(dictionary):
        # code here

and this will work seamlessly both with Python 2 and 3. However, there are some
more complex cases where one has to resort to the type of ``if`` statement shown at
the top of this post. The [six](https://pythonhosted.org/six/) package again
makes this slightly easier by providing ``PY2`` and ``PY3`` boolean constants:

    if six.PY2:
        # Python 2 code
    else:
        # Python 3 code
        
So far so good.

This brings me to the main point of this post. We don't
really know yet what Python 4 will look like, but we can be pretty sure that
the transition from Python 3 to Python 4 will be a lot smoother and will likely
[not be backward-incompatible in the same way as Python 3 was](https://opensource.com/life/14/9/why-python-4-wont-be-python-3). If that's
the case, we should be able to use packages developed for Python 2 and 3
seamlessly with Python 4. Right?...

Nope! By searching on GitHub, I found ~200,000 matches for the
following kind of syntax:

    if six.PY3:
        # Python 3 code
    else:
        # Python 2 code

See the problem? In ``six``, ``PY3`` is defined as:

    PY3 = sys.version_info[0] == 3
    
so that once Python 4 is out, both ``PY2`` and ``PY3`` will be (correctly)
``False`` and the above if statement will execute the ``else`` statement for
Python 2 code. Oops!

To avoid this, it's critical that we avoid treating Python 3 as the special
case in these kinds of ``if`` statements:

    if six.PY3:
        # Python 3 code
    else:
        # Python 2 code

and instead treat Python **2** as the special case, and default to Python 3
code otherwise:

    if six.PY2:
        # Python 2 code
    else:
        # Python 3 code

It's a small change, but it will save a lot of headaches down the road. So if
you develop a Python package, please check now to make sure that your code will
be Python 4-compatible!
