CREATE TABLE mention (
    mention_id SERIAL PRIMARY KEY,
    ticker VARCHAR (10) UNIQUE NOT NULL,
    mentions INT NOT NULL
);

