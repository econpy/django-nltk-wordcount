Django Bootstrap NLTK Word Counter
==================================

Sample [django](http://github.com/django/django) app that uses [nltk](http://github.com/nltk/nltk) to count the number of occurrences of a given word in a selected text file, all wrapped up with a simple [Twitter Bootstrap](http://github.com/twitter/bootstrap) layout.

Demo
----

See if a live demo of this app at [words.economics.io](http://words.economics.io).


Dependencies
------------

The following libraries are dependencies:

* [Django](https://github.com/django/django)
* [NLTK](https://github.com/nltk/nltk)
* [Twitter Bootstrap](https://github.com/twitter/bootstrap)


Usage
-----

After installing the dependencies, run the app by issuing the following commands:

    git clone git://github.com/econpy/django-nltk-wordcount.git
    cd django-nltk-wordcount/project
    python manage.py syncdb
    python manage.py runserver
