#encoding: utf-8
import pymysql


def build_conn(host_ip, user_name, password, database):
    conn = pymysql.connect(host=host_ip, user=user_name, passwd=password, db=database, charset='utf8')
    return conn

def connection(database , sql):
    #conn = pymysql.connect(host='192.168.1.10', user='root', passwd='Admin10', db='helpdesk',charset='utf8')
    conn = build_conn('127.0.0.1', 'wenye199100', '199100', database)
    #conn = build_conn('192.168.1.10', 'root', 'Admin10', database)
    
    cur = conn.cursor()
    cur.execute(sql)
    nRet = cur.fetchall()
    cur.close()
    conn.close()
    return  nRet
