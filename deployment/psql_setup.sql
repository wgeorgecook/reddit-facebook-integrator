-- Creates role, database, and table
CREATE ROLE redditor WITH LOGIN PASSWORD 'TempPa55';
ALTER ROLE redditor CREATEDB;
CREATE DATABASE reddit_info OWNER redditor;
GRANT ALL PRIVILEGES ON DATABASE reddit_info TO redditor;
\connect reddit_info;
CREATE TABLE RedditInfo(
    post_url varchar(255), 
    post_title varchar(255),
    post_id varchar(50),
    id varchar(10)
);
GRANT ALL PRIVILEGES ON TABLE RedditInfo TO redditor;