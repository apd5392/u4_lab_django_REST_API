-- settings.sql
CREATE DATABASE nba;
CREATE USER nbauser WITH PASSWORD 'tunr';
GRANT ALL PRIVILEGES ON DATABASE nba TO nbauser;