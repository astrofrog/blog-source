#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Thomas Robitaille'
SITENAME = '.py in the sky'
SITESUBTITLE = 'Musings on Python, Astronomy, and Open Science'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Professional page at the MPIA', 'http://www.mpia.de/~robitaille'),
          ('Astropython', 'http://www.astropython.org'),
          ('AstroBetter', 'http://www.astrobetter.com'),
          ('Astropy', 'http://www.astropy.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set URL structure to match octopress
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'octopress-theme')

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'plugins')
PLUGINS = ['summary']

SUMMARY_END_MARKER = '<!-- more -->'

# RSS/Atom feeds
FEED_RSS = 'rss.xml'
FEED_ATOM = 'atom.xml'

LOCALE = 'C'

SITEURL = 'http://astrofrog.github.com'
DISQUS_SITENAME = "pyinthesky"
GOOGLE_ANALYTICS = "UA-37635519-1"
