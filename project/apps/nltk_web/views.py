import os
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from os.path import abspath,dirname

corpus_root = os.path.join(abspath(dirname(__file__)), '../../reviews')
androidcorpus = PlaintextCorpusReader(corpus_root, '.*')


def filelist(dir_name, sub_dir, *args):
    fl = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if len(args) == 0:
                fl.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fl.append(dirfile)
        elif os.path.isdir(dirfile) and sub_dir:
            fl += filelist(dirfile, sub_dir, *args)
    return fl


def androidapp(appid):
    appid = appid.split('/')[-1]
    return Text(androidcorpus.words(appid), name=appid.replace('.txt', ''))

texts = [androidapp(i) for i in filelist(corpus_root, False, 'txt')]


def home(request):
    RC = RequestContext(request, dict(texts=texts))
    return render_to_response('home.html', RC)


def count(request):
    if request.method == "POST":
        corpus = texts[int(request.POST['corpus'])]
        word = request.POST['word']
        context = {
                   'mpn': unicode(corpus.name),
                   'count': unicode(corpus.count(word)),
                   'word': unicode(word),
                  }
        RC = RequestContext(request, context)
        return render_to_response('results.html', RC)
