
# MusicMania Mysql ETL
 This project consists on putting into practice the following concepts:

-   Data modeling with SQL
-   Database star schema created
-   ETL pipeline using Python 

## Context
A music app startup wants to analyse data that they have been generating in two log files. The analysts specifically wants to know the types of songs users have been listening to. The company wants to create an ETL pipeline based on this data and create a relational database model so that analyst can execute queries against this database model
## Schema
The schema used for this exercise is the Star Schema: There is one main fact table containing all the measures associated to each event (user song plays), and 4 dimentional tables, each with a primary key that is being referenced from the fact table.

![](https://raw.githubusercontent.com/siddharthk24/DataModelling_Mysql/master/Images/newDataSchema.png)
## Technologies 
the project is created with : 
 - MySQL 5.7.19
 - Python 3
 - Pandas Library
 - MySQL Connector

## Project Structure

`create_tables.py` - create the tables in the database.  
`etl.py` - implementation of the etl process.  
`sql_queries.py` - contains the queries that are used throughout the project

## Running the files

> 1.  run create_tables.py to create the database and tables
> 2.  run etl.py to load data into the database
> 3.  run test.ipynb to test if it works




