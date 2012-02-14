===============
Django NextPage
===============

``django-nextpage`` is modified from django-pagination, but only previous and next page is provided.

Since SQL COUNT statement on large table has poor performance, lots of website turns to show just next  and previous page link or button.


How it works?
=========================

``django-nextpage`` only execute one SQL statement, no count, no next page determine query.

For example:

If you want to pagiante by 20, django-nextpage will query for 21 items, if queryset length is 21, then we have next page; if queryset length is 20 or less, then we don't have next page. 


Installation
============

Add ``nextpage`` to ``INSTALLED_APPS``, like:

    .. code:: python

    INSTALLED_APPS = (
       # ...
       'nextpage',
    )


and ``TEMPLATE_CONTEXT_PROCESSORS`` should have ``django.core.context_processors.request``, like:

    .. code:: python

    ("django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request")



Usage
=====

Just like ``django-pagination``, in fact it designed as a drop-in replacement. just load ``nextpage`` templatetag 

    {% load nextpage %}

    {% autopaginate object_list 20 %}

    {% paginate %}
