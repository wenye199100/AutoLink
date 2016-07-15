#encoding: utf-8
import DBConnetion

def update():
    db = DBConnetion.connection('oil-companies','select company_id,name,website from company_data')
    dict_name_id = {}
    dict_id_web = {}
    for i in db:
        if i[1] and i[2]:
            dict_name_id[i[1]] = i[0]
            dict_id_web[i[0]] = i[2]
            # print i[0], i[1], i[2]
    dict_id_web = sorted(dict_id_web.iteritems(), key=lambda d: d[0], reverse=False)
    return dict_name_id, dict_id_web

