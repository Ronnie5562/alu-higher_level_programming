-- Write a script that creates the database hbtn_0d_usa and the table states on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (id INT AUTO_INCREMENTED NOT NULL PRIMARY KEY, name VARCHAR(256));
