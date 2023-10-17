-- Create a new database if not exists
CREATE DATABASE IF NOT EXISTS mydb;

-- Switch to the new database
USE mydb;

-- Create a table for users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Insert sample data
INSERT INTO users (username, password) VALUES
    ('john_doe', 'password123'),
    ('jane_doe', 'secret456');
