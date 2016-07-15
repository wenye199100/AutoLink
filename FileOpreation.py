#encoding: utf-8

def write(dict):
    file = open('Data/dict.txt', 'w')
    tag = u'company'
    for (d, x) in dict.items():
        file.write((d+' '+tag).encode('utf-8') + "\n")
    file.close()
