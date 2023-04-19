from constants import REGEX_SENTENCES
import task1
import re

def test_non_declarative1():
    res = task1.non_declarative([".", "!", "?"])
    assert res == 2

def test_non_declarative2():
    res = task1.non_declarative([".", "."])
    assert res == 0

def test_average_len1():
    words =["hello", "world", "how", "are", "you"]
    assert task1.average_len(words) == 3.8

def test_average_len2():
    words =["one", "four"]
    assert task1.average_len(words) == 3.5

def test_delete_abbreviations1():
    text = "Mrs. Gbjkds i.e. njklw."
    sentences = re.findall(REGEX_SENTENCES, text)
    assert task1.delete_abbreviations(text, sentences) == 1

def test_delete_abbreviations2():
    text = "Ghk, hoas, jika etc."
    sentences = re.findall(REGEX_SENTENCES, text)
    assert task1.delete_abbreviations(text, sentences) == 1

def test_find_ngrams():
    words = ["what", "do", "you", "do", "you", "do"]
    assert  task1.find_ngrams(words, 2, 2) == [('do you', 2), ('you do', 2), ('what do', 1)]
