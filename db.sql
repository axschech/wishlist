
CREATE DATABASE wishlist;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE games (

);

CREATE TABLE users_games (

);

CREATE TABLE prices (

);

CREATE TABLE platforms (

);
