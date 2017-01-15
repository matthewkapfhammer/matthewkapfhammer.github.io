#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time


AUTHOR = u'Matthew Kapfhammer'
SITENAME = u'Matthew Kapfhammer'
SITEURL = ''
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
COPYRIGHT_YEAR = time.strftime("%Y")


PATH = 'content'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('About', '/about'),
    ('Blog', '/'),
)
DEFAULT_PAGINATION = 10


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
	('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/matthewkapfhammer'),
    ('IMDB', 'http://www.imdb.com/name/nm2768452/'),
    ('GitHub', 'https://github.com/matthewkapfhammer'),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
