#encoding: utf-8

def compare(text ,dict_name, dict_id):
    tt = text
    added = 0
    for (name, id) in dict_name:
        pos = text.find(name)
        if pos != -1:
            tt = tt[:pos+added] + dict_id[id] + tt[pos+added:]
            added = len(dict_id[id])








