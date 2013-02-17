Django Bootstrap NLTK Word Counter
==================================

Sample [Django](http://github.com/django/django) app that uses [NLTK](http://github.com/nltk/nltk) to count the number of occurrences of a given word in a selected text file, all wrapped up with a simple [Twitter Bootstrap](http://github.com/twitter/bootstrap) layout.

Demo
----

Check out a live demo: [http://words.economics.io](http://words.economics.io)


Dependencies
------------

The following libraries are dependencies:

* [Django](https://github.com/django/django) + [django-debug-toolbar](http://pypi.python.org/pypi/django-staticfiles/) + [django-staticfiles](http://pypi.python.org/pypi/django-staticfiles/)
* [NLTK](https://github.com/nltk/nltk)


Usage
-----

After installing the dependencies, run the app by issuing the following commands:

    git clone git://github.com/econpy/django-nltk-wordcount.git
    cd django-nltk-wordcount/project
    python manage.py syncdb
    python manage.py runserver
