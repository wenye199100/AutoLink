#encoding: utf-8
import jieba
import DBConnetion

if __name__ == "__main__":

    file = open('Data/file.txt')
    B = DBConnetion.connection('oil-companies','select company_id,name,website from company_data')
    dict_name_id = {}
    dict_id_web = {}
    for i in B:
        if i[1] and i[2]:
            dict_name_id[i[1]] = i[0]
            dict_id_web[i[0]] = i[2]
            print i[0], i[1], i[2]
    dict_id_web = sorted(dict_id_web.iteritems(), key=lambda d: d[0], reverse=False)
    print dict_id_web
       #print i[0].encode('gbk')
       # output2.write(i[0] + "\n")
    #file.close()
    #output.close()

    # for line in file:
    #     print("1" + line.decode("gbk"))
    # string = "在如今越来越追求效率的作业环境下，整个行业都在想方设法提高操作安全的同时不断降低总体作业成本。DynaStage是DynaEnergetics公司推出的关于射孔的一个全新概念，它开创性的将编址技术和选择性技术同改良的机械设计进行整合，可以完全消除潜在的人为错误。该系统比传统的射孔枪作业效率更高，由于搭载额外的安全设计，在射孔期间还允许同时进行其他作业，这种设计可以提高射孔的质量和作业性能可靠性，减少入井失败的次数并降低库存量。DynaStage系统已经成功地在多个盆地完成了作业，该新系统针对三个主要方面来提高作业效率和降低作业成本：安全、可靠性、库存和成本控制。"
    #
    # seg_list = jieba.cut(string, cut_all=False)
    #
    # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

