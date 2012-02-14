===============
Django NextPage
===============

django-nextpage is modified from django-pagination, but only previous and next page is provided.


Installation
============

Add `nextpage` to `INSTALLED_APPS`, like:

    INSTALLED_APPS = (
       # ...
       'nextpage',
    )


and `TEMPLATE_CONTEXT_PROCESSORS` should have `django.core.context_processors.request`, like:

    ("django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request")



Usage
=====

Just like `django-pagination`, in fact it designed as a drop-in replacement. just load `next` templatetag 

    {% load nextpage %}

    {% autopaginate object_list 20 %}

    {% paginate %}
