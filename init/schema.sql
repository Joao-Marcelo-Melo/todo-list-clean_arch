CREATE DATABASE todo_list

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    status BOOLEAN NOT NULL
);