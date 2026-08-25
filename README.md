# Background

SQL sublanguage: DML (Data Manipulation Language)

Now that we can create and drop tables, we need to be able to insert records into a table.

The syntax for inserting a record is:

INSERT INTO table_name (col_1, col_2, ..., col_N)
VALUES (val_1, val_2, ..., val_N);

## Problem 1

Assume the following table already exists.

| title | artist |
|-------|--------|
| Let it be | Beatles |
| Hotel California | Eagles |
| Kashmir | Led Zeppelin |

Strings should be enclosed in single quotes.

Write an SQL statement in `problem1.sql` that inserts a new record into the `song` table.
