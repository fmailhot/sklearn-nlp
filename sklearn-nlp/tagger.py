""" Generic classifier-based sequence tagging.

This will eventually be what's in the first line of the docstring.
For the moment, though, it's going to be a very basic LR-based
POS-tagger.

First pass at this will draw inspiration from the POS-tagging
example in the sklearn docs. [add ref---fm]

Eventually, the classifiers available will be extended (and/or
user-specifiable), and the type of taggable data will also
be extended (e.g. chunk-IOB tagging, &c).
"""
import cPickle as pickle
from datetime import datetime
import logging
from time import time
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from .utils.data_utils import DataLoader
__authour__ = "fmailhot (fred.mailhot@gmail.com)"


#TODO(fmailhot): curate this list a bit more carefully
stopwords = ENGLISH_STOP_WORDS.union({"did", "does", "doing",
                                      "having", "just", "theirs"})


class LogisticRegressionPOSTagger(object):
    def __init__(self, model_file=None, data_files=None):
        try:
            self.model = pickle.load(open(model_file, "rb"))
        except IOError, io_e:
            logging.critical(str(io_e))
            raise(io_e)
    


