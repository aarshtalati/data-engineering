# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE;"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE;"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE;"
artist_table_drop = "DROP TABLE IF EXISTS artist CASCADE;"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
        songplay_id serial PRIMARY KEY,
        start_time TIMESTAMP,
        user_id SMALLINT NOT NULL,
        level VARCHAR(20),
        song_id VARCHAR(20),
        artist_id VARCHAR(20),
        session_id SMALLINT,
        location VARCHAR(5000),
        user_agent VARCHAR(1000)
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
        user_id SMALLINT PRIMARY KEY,
        first_name VARCHAR(200),
        last_name VARCHAR(200),
        gender CHAR(1),
        level VARCHAR(5) 
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
        song_id VARCHAR(20) PRIMARY KEY,
        title VARCHAR(5000),
        artist_id VARCHAR(20),
        year SMALLINT,
        duration INTERVAL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist(
        artist_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(500),
        location VARCHAR(5000),
        latitude DECIMAL,
        longitude DECIMAL
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
        start_time TIMESTAMP PRIMARY KEY,
        hour SMALLINT,
        day SMALLINT,
        week SMALLINT,
        month SMALLINT,
        year SMALLINT,
        weekday VARCHAR(10)
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]