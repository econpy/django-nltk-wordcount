import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from glob import glob
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from os.path import abspath,basename,dirname

corpus_root = os.path.join(abspath(dirname(__file__)), '../../reviews')
androidcorpus = PlaintextCorpusReader(corpus_root, '.*')


def cleanfile(filepath):
    return basename(filepath).replace('.txt', '')


def androidapp(appid):
    appid = '%s.txt' % appid
    return Text(androidcorpus.words(appid), name=appid)


def home(request):
    txtfiles = [cleanfile(i) for i in glob('%s/*.txt' % corpus_root)]
    RC = RequestContext(request, {'texts': txtfiles})
    return render_to_response('home.html', RC)


def count(request):
    if request.method == "POST":
        corpus = androidapp(request.POST['corpus'])
        word = request.POST['word']
        context = {
                   'mpn': unicode(corpus.name)[:-4],
                   'count': unicode(corpus.count(word)),
                   'word': unicode(word),
                  }
        RC = RequestContext(request, context)
        return render_to_response('results.html', RC)
