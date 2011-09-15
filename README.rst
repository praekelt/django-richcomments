Django Richcomments
===================
**Django app extending the builtin comments framework for AJAX style commenting.**

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-richcomments`` to your Python path.

#. Configure Django's comments framework as described `here <https://docs.djangoproject.com/en/dev/ref/contrib/comments/#quick-start-guide>`_.

#. Add richcomments url include to the project’s urls.py file::

    (r'^richcomments/', include('richcomments.urls')),

Usage
-----

