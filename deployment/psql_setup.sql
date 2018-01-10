-- Creates role, database, and table
CREATE ROLE redditor WITH LOGIN PASSWORD 'TempPa55';
ALTER ROLE redditor CREATEDB;
CREATE DATABASE reddit_info OWNER redditor;
GRANT ALL PRIVILEGES ON DATABASE reddit_info TO redditor;
