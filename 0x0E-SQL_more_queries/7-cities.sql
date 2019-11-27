-- create database and new table.
CREATE database IF NOT EXISTS hbtn_0d_usa; 
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id int NOT NULL UNIQUE AUTO_INCREMENT, 
    state_id int NOT NULL,
    name VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
