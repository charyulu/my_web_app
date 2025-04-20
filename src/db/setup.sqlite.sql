-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    photo_url TEXT
);

-- Insert a sample user (for testing purposes)
-- Note: Replace 'hashed_password_here' with the actual hashed password.
INSERT INTO users (username, password_hash, photo_url)
VALUES ('charyulu', '$2b$12$dGc0E13a/2b4QTaReE0XVu5YoArDXeaWVTa1mxjz6o0p.qTS6Ch7u', '/static/images/ReceptionInvitePhoto_01.jpg');