#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:17:52 2019

@author: siddharth_k
"""

drop_table_songs = "drop table if exists songs "
drop_table_songplays = "drop table if exists songplays"
drop_table_artists = "drop table if exists artists"
drop_table_users = "drop table if exists users "
drop_table_time = "drop table if exists time "


#create table queries

create_table_songs = """create table if not exists songs (
	songid varchar(50),
	name text,
	duration float,
	year int, 
	artistid int,
	primary key ( songid )
);"""

create_table_artists = """ create table if not exists artists(
	artistid int auto_increment,
	artist_name text,
	artist_longitude text,
	artist_latitude text,
	artist_location text,
	primary key (artistid)
); """

create_table_users = """ create table users (
	userid int primary key,
	first_name text,
	last_name text,
	gender text,
	level text
	);
"""
create_table_songplays = """   CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id serial PRIMARY KEY , 
                                start_time DATE  NOT NULL, 
                                user_id int NOT NULL, 
                                level TEXT, 
                                song_id TEXT, 
                                artist_id TEXT, 
                                session_id TEXT, 
                                location TEXT, 
                                user_agent TEXT
); 
"""

create_table_time = """ CREATE TABLE IF NOT EXISTS time ( 
                            start_time time PRIMARY KEY, 
                            hour int, 
                            day int, 
                            week int, 
                            month int, 
                            year int, 
                            weekday int)
"""

create_queries = [create_table_artists,create_table_songplays,create_table_songs,create_table_time,create_table_users]
drop_queries = [drop_table_artists,drop_table_songplays,drop_table_songs,drop_table_time,drop_table_users]

 
