-- create database and new table.
CREATE database IF NOT EXISTS hbtn_0d_usa; 
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id int NOT NULL UNIQUE AUTO_INCREMENT, name VARCHAR(255), PRIMARY KEY (id));
