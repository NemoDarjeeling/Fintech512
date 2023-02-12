DROP TABLE IF EXISTS user;
--This line is used to delete the user table from the database if it already exists.
DROP TABLE IF EXISTS post;
--This line is used to delete the post table from the database if it already exists.

CREATE TABLE user (
--This line is used to create a new table named user in the database.
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  --This line is used to create a column named id in the user table. The data type is integer and it will automatically increment every time a new user is inserted into the table. The PRIMARY KEY constraint is used to indicate that this column is a unique identifier for each row in the table.
  username TEXT UNIQUE NOT NULL,
  --This line is used to create a column named username in the user table. The data type is text and the UNIQUE constraint is used to ensure that no two users have the same username. The NOT NULL constraint is used to indicate that this column must contain a value.
  password TEXT NOT NULL
  --This line is used to create a column named password in the user table. The data type is text and the NOT NULL constraint is used to indicate that this column must contain a value.
);

CREATE TABLE post (
--This line is used to create a new table named post in the database.
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  --This line is used to create a column named id in the post table. The data type is integer and it will automatically increment every time a new post is inserted into the table. The PRIMARY KEY constraint is used to indicate that this column is a unique identifier for each row in the table.
  author_id INTEGER NOT NULL,
  --This line is used to create a column named author_id in the post table. The data type is integer and the NOT NULL constraint is used to indicate that this column must contain a value. This column will store the id of the user who created the post.
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  --This line is used to create a column named created in the post table. The data type is timestamp and the NOT NULL constraint is used to indicate that this column must contain a value. The DEFAULT CURRENT_TIMESTAMP is used to automatically insert the current timestamp when a new post is inserted into the table.
  title TEXT NOT NULL,
  --This line is used to create a column named title in the post table. The data type is text and the NOT NULL constraint is used to indicate that this column must contain a value.
  body TEXT NOT NULL,
  --This line is used to create a column named body in the post table. The data type is text and the NOT NULL constraint is used to indicate that this column must contain a value.
  FOREIGN KEY (author_id) REFERENCES user (id)
  --line specifies that the "author_id" column in the "post" table references the "id" column in the "user" table. This creates a relationship between the two tables, ensuring that each post is associated with a valid user.
);

