#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = "Python Sul"

SITENAME = "Python Sul 2022"
SITEYEAR = 2022

SITEURL = config("SITE_URL", default="/")

PATH = "content"

PLUGIN_PATHS = [
    "plugins/",
]
PLUGINS = [
    "sitemap",
]

SITEMAP = {
    "format": "xml",
    "exclude": ["tags.html", "categories.html", "authors.html", "archives.html"],
}
ARTICLE_ORDER_BY = "date"
TIMEZONE = "America/Sao_Paulo"

DEFAULT_LANG = "pt-br"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# OLD_EVENTS
OLD_EVENTS = (
    ("2014", "/2014"),
    ("2015", "/2015"),
    ("2016", "/2016"),
    ("2018", "/2018"),
    ("2020", "/2020"),
)
# OLD_EVENTS
MENU = (
    ("#intro", "Início", True),
    ("#about", "Sobre", False),
    # ("#schedule", "Agenda", False),
    ("#inscricao", "Inscrição", False),
    ("#supporters", "Patrocinadores", False),
    ("#contact", "Contato", False),
)

INSCRICAO_LINK = "https://www.sympla.com.br/python-sul-2022__1610633"

# Social widget
SOCIAL = {
    "instagram": "https://www.instagram.com/pythonsul",
    "twitter": "https://www.twitter.com/pythonsul",
}

DEFAULT_PAGINATION = False
SITE_META_KEYWORDS = "Python Sul 2022, evento python, jaraguá do sul, evento jaraguá do sul, python, python sul, comunidade python jaraguá do sul, python santa catarina, comunidade"
SITE_META_DESCRIPTION = "Evento da comunidade Python da região sul do Brasil, com intuito de popularizar e disseminar o conhecimento da linguagem de programação Python"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
