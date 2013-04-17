#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Mobile Oxford'
SITENAME = u'Mobile Oxford Blog'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%d/%m/%Y'
THEME = 'mox'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'documents']

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

SITEURL = 'http://blog.m.ox.ac.uk'
FEED_DOMAIN = SITEURL

PLUGINS=['pelican.plugins.sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly'
    }
}