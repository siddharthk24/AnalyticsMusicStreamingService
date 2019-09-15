#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:40:39 2019

@author: siddharth_k
"""
import pandas as pd
import glob
from sqlqueries import *
import mysql.connector as connector

def process_song_data(conn,cursor,path):
    
    Song_Data_file_pathArray=glob.glob(path + '/*.json')
    DataList=[]

# Reads song data from each individual file and processes it to generate songs and artists data    
    for val in Song_Data_file_pathArray:
        tempDataFrame = pd.read_json(val ,lines = True)
        DataList.append(tempDataFrame)

    SongsData = pd.concat(DataList)
    
    Songs = SongsData[['song_id','title','duration','year','artist_id']]
    Artists = SongsData[['artist_id','artist_name','artist_longitude','artist_latitude','artist_location']]
    Artists = Artists.fillna(-1)

# execute sql queries to insert data into database tables 
   
    try:
        for row in Songs.iterrows():
            cursor.execute(song_insert,tuple(row[1]))
        
            for row in Artists.iterrows():
                cursor.execute(artist_insert,tuple(row[1]))
        
        conn.commit()
    except Exception as e :
        print(e)

def process_log_data(connector,cursor,path):
    
    Log_data_File_pathArray = glob.glob(path + '/*.json')
    
# Reads log data from each individual file and processes it to generate users and timestamps for individual song plays        
    
    DataframeList = []

    for path in Log_data_File_pathArray:
        
        tempDataframe = pd.read_json(path,lines = True)
        DataframeList.append(tempDataframe)
    

    logsData = pd.concat(DataframeList)
    # fetches user data from the logs dataframe
    users = logsData[['firstName','lastName','gender','level','location']]

    # insert users data into user table in the database 
    
    try:
    
        for row in users.iterrows():
            cursor.execute(users_insert,tuple(row[1]))
        
    except Exception as e:
        print(e)
    
    # converts time and date column from dataframe to time stamp format
    t= pd.to_datetime(logsData['ts'], unit= 'ms')

    time_data = (t.dt.time, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('timestamp', 'hour', 'day', 'week of year', 'month', 'year', 'weekday')
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels,time_data)))
    
    # inserts time data into  database
    try:
            
        for row in time_df.iterrows():
            cursor.execute(time_insert,tuple(row[1]))
        
    except Exception as e:
            print(e)
    
    try:
        songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
        
        #fetches song id and artist it for each songplay in log data
        for row in logsData.iterrows():
            
            song_select = """select song_id,artist_id from songs left join artists on songs.artistid = artists.artistid \
            where name = %s and artist_name = %s """
            
            cursor.execute(song_select,[row[1][1],row[1][1]])
            
            result = cursor.fetchone()
            
            if result:
                songid,artistid = result
            else:
            
                songid,artistid = None
                
        #Enters record for song play in songplay table in database        
            songplay_data = (0, pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
           
            cursor.execute(songplay_table_insert,songplay_data) 
                
    except Exception as e :
        print(e)


def main():
    
    conn = connector.connect(user = "admin24",password="Believe*24"
                         ,host = "mysqldb.c3taloxqgznp.us-east-2.rds.amazonaws.com"
                         ,port = 3306, database = "MusicMania")
    
    cursor = conn.cursor()

    process_song_data(conn,cursor,path = "data/song_data")
    process_log_data(conn,cursor,path = "data/song_data")
    

                
if __name__  == "__main__" :
    main()