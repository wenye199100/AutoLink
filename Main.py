#encoding: utf-8
# import Segmentation as Seg
import CompanyInfo as CI
import FileOpreation as FO
import AddLink as AL

if __name__ == "__main__":
    # FO.write(CI.update()) #更新公司名称
    # (a,b) = CI.update()
    # print b

    # file = open('Data/file.txt')
    string = "在如今越来越追求效率的作业环境下，整个行业都在想方设法提高操作安全的同时不断降低总体作业成本。DynaStage是DynaEnergetics公司推出的关于射孔的一个全新概念，它开创性的将编址技术和选择性技术同改良的机械设计进行整合，可以完全消除潜在的人为错误。该系统比传统的射孔枪作业效率更高，由于搭载额外的安全设计，在射孔期间还允许同时进行其他作业，这种设计可以提高射孔的质量和作业性能可靠性，减少入井失败的次数并降低库存量。DynaStage系统已经成功地在多个盆地完成了作业，该新系统针对三个主要方面来提高作业效率和降低作业成本：安全、可靠性、库存和成本控制。"
    # cut(string)
    text = "李小福是创新办主任也是云计算方面的专家; Dunlop Oil & Marine你知道吗"
    ss = "是"
    print AL.test(ss)
    print ss
    # Seg.poosseg(text)
    # Seg.tokenize(text)