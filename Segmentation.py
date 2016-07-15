#encoding: utf-8
import jieba
jieba.load_userdict("Data/dict.txt")
import jieba.posseg as pseg
import re



def cut(string):
    seg_list = jieba.cut(string, cut_all=False)
    print(','.join(seg_list))

def poosseg(string):
    words = pseg.cut(string)
    for word, flag in words:
        print('%s %s' % (word, flag))

def tokenize(string):
    result = jieba.tokenize(string.decode('utf-8'))
    for tk in result:
        # print tk
        print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))


