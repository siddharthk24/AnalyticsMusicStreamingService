#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:39:26 2019

@author: siddharth_k
"""
import sqlqueries

import mysql.connector as connector

def create_database ():
    
    try:
        conn = connector.connect(user = "admin24",password="Believe*24" \
                         ,host = "mysqldb.c3taloxqgznp.us-east-2.rds.amazonaws.com" \
                         ,port = 3306, database = "MusicMania")
    
        cursor = conn.cursor()

    except Exception as e:
        print(e)
    
    return conn,cursor

def drop_tables(cursor):    
    try:
        for query in sqlqueries.drop_queries:
            cursor.execute(query)
    
    except Exception as e : 
        print(e)

def create_tables(cursor):
    try:
        for query in sqlqueries.create_queries:
            cursor.execute(query)
    except Exception as e:
            print(e)            
 
def main():
   conn,cursor= create_database()
   drop_tables(cursor)
   create_tables(cursor)      

if __name__== "__main__" :
    main()
