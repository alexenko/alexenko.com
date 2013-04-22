#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'alexenko'
SITENAME = u'alexenko.com'
SITESUBTITLE = u'Forking the way we do education'
SITEURL = ''

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 3

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/alexenko'),
)

# Use RSS
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/rss'
CATEGORY_FEED_RSS = 'feeds/category.%s.rss'
TAG_FEED_RSS = None
FEED_MAX_ITEMS = 30

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#Theme
THEME = "./themes/pelican-chunk"
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_DATE_FORMAT = ('%b %d %Y')
#TYPOGRIFY = True

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Cleaner Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
