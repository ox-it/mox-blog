#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Mobile Oxford'
SITENAME = u'Mobile Oxford Blog'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
THEME = 'mox'

DEFAULT_PAGINATION = False


ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

PLUGINS = ['pelican.plugins.gravatar', 'pelican_gist']

SITEURL = 'http://blog.m.ox.ac.uk'
FEED_DOMAIN = SITEURL

SITEURL = 'http://blog.m.ox.ac.uk'
FEED_DOMAIN = SITEURL

DISQUS_SITENAME = 'mobileoxford'
