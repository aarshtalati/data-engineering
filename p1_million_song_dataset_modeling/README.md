# Purpose
 
The purpose of this database is to perform Online Analytical Processing (OLAP). The company could be trying to find anwers to questions like:

1. What are the most played artists?
1. What are the most played songs?
1. Which user likes and disklikes which songs?
1. How many users are on the paid vs free plan?
1. How are users navigating the application and exploring songs?
1. Which demographics have the highest amount of application usage?
1. What are the most popular times when the application is being used?
1. What are the most used web browsers or clients where the users access the application from?

Execute the following SQL command to find the most popular song:

    %sql SELECT s.title, a.name
    FROM songplays sp
    INNER JOIN songs s ON s.song_id = sp.song_id
    INNER JOIN artists a ON a.artist_id = sp.artist_id
    GROUP BY s.title, a.name
    ORDER BY 1 DESC;

# Database Schema

This design uses star schema. Hence, the schema design is denormalized. It has fact table (songplays) and dimension tables (users, songs, artists, time). Each table has a primary key. Which could be used to reference with the other relative table(s). Execute the following command to set up the database schema:

    $ python create_tables.py

# Extract, Transform, Load Pipeline

In principle, the ETL process reads the two different kinds of logs available, loads the data into Pandas DataFrame and stores it into a PostgreSQL database. The insert statements have casting built-in to convert the data to better suite OLAP needs. Execute the following command to initiate ETL process.

    $ python etl.py

# Citations

Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011.

“How to Install and Configuration PostgreSQL on Ubuntu Linux.” YouTube, uploaded by ProgrammingKnowledge, 27 Jan. 2017, www.youtube.com/watch?v=-LwI4HMR_Eg.

Amigoscode. “PostgreSQL: How to Connect to Databases | Course | 2019.” YouTube, uploaded by Amigoscode, 19 Mar. 2019, www.youtube.com/watch?v=bE9h6aAky4s&feature=youtu.be.

Hule, Vishal. “Python PostgreSQL Tutorial Using Psycopg2.” Https://Pynative.Com/Python-Postgresql-Tutorial/, PYnative, 8 Dec. 2020, pynative.com/python-postgresql-tutorial.

The PostgreSQL Global Development Group. “Data Types.” PostgreSQL Documentation, 12 Nov. 2020, www.postgresql.org/docs/9.5/datatype.html.

EdChum. “Pandas Converting Row With Unix Timestamp (in Milliseconds) to Datetime.” Stack Overflow, 19 Jan. 2016, stackoverflow.com/questions/34883101/pandas-converting-row-with-unix-timestamp-in-milliseconds-to-datetime/34883876#34883876.

“Million Song Dataset.” Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere, 2011, http://millionsongdataset.com.