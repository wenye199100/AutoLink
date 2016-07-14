#encoding: utf-8
import jieba
import jieba.posseg as pseg
import re

def cut(string):
    seg_list = jieba.cut(string, cut_all=False)
    print(','.join(seg_list))

def poosseg(string):
    words = pseg.cut(string)
    for word, flag in words:
        pattern = re.compile(r'^nw?')
        pattern2 = re.compile(r'eng')
        match = pattern.match(flag)
        match2 = pattern2.match(flag)
        if match or match2:
            print('%s %s' % (word, flag))


if __name__ == "__main__":

    #file = open('Data/file.txt')
    string = "在如今越来越追求效率的作业环境下，整个行业都在想方设法提高操作安全的同时不断降低总体作业成本。DynaStage是DynaEnergetics公司推出的关于射孔的一个全新概念，它开创性的将编址技术和选择性技术同改良的机械设计进行整合，可以完全消除潜在的人为错误。该系统比传统的射孔枪作业效率更高，由于搭载额外的安全设计，在射孔期间还允许同时进行其他作业，这种设计可以提高射孔的质量和作业性能可靠性，减少入井失败的次数并降低库存量。DynaStage系统已经成功地在多个盆地完成了作业，该新系统针对三个主要方面来提高作业效率和降低作业成本：安全、可靠性、库存和成本控制。"
    #seg_list = jieba.cut_for_search(string)  # 搜索引擎模式
    cut(string)
    poosseg(string)



