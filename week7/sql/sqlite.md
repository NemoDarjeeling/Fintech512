### select
select can be used to perform simple calculations;  
SELECT 
    column_list
FROM 
    table;(";" used to end the statement)  
SELECT * FROM tracks;("*" means all)  
### order by
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,(首先按c1升序排列，然后按c2降序排列)
    column_2 DESC;(if not specify, it will use ASC)  
SELECT
	name,
	milliseconds, 
	albumid
FROM
	tracks
ORDER BY
	3,2;(按照选择的数据第三列升序，然后第二列升序排列)  
ORDER BY 
    Composer NULLS LAST;（按composer一列升序排列，但是将所有NULL置于最后）  
### select distinct
an optional clause of the  SELECT statement. The DISTINCT clause allows you to remove the duplicate rows in the result set.  
SQLite considers NULL values as duplicates. If you use theDISTINCT clause with a column that has NULL values, SQLite will keep one row of a NULL value.  
## where
In SQLite, the WHERE clause is used in a SQL statement to filter the result set based on a specified condition. It allows you to retrieve specific records from a table that meet certain criteria.  
SELECT 
    name 
FROM 
    employees 
WHERE 
    age > 30;  
### limit
In SQLite, the LIMIT clause is used to restrict the number of rows returned by a SELECT statement. It specifies the maximum number of rows to return in the result set.  
SELECT 
    * 
FROM 
    customers 
LIMIT 
    5;(return only first 5 rows)
### between
In SQLite, the BETWEEN operator is used to select values that are within a specified range of values. It is used in a WHERE clause to filter the result set based on a specific range of values.  
SELECT 
    name 
FROM 
    employees 
WHERE 
    age (NOT) BETWEEN 30 AND 40;
### in
In SQLite, the IN operator is used to specify multiple values in a WHERE clause. It allows you to match a column value against a set of values.  
SELECT 
    name 
FROM 
    employees 
WHERE 
    department IN ('Sales', 'Marketing');
### like
In SQLite, the LIKE operator is used to match a string value against a pattern. It is used in a WHERE clause to filter the result set based on a specific pattern.  
SELECT 
    name 
FROM 
    customers 
WHERE 
    email LIKE '%gmail.com';
### is null
This returns all entries in column Composer that is not null  
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY 
    Name;  
### join
#### inner join
It matches each row from the albums table with every row from the artists table based on the join condition (artists.ArtistId = albums.ArtistId) specified after the ON keyword. If the join condition evaluates to true (or 1), the columns of rows from both albums and artists tables are included in the result set.（交集）  
SELECT 
    Title,(a column in 'albums')
    Name(a column in 'artists')
FROM 
    albums
INNER JOIN artists 
    ON artists.ArtistId = albums.ArtistId;  
*aliases*:  
SELECT
    l.Title, 
    r.Name
FROM
    albums l
INNER JOIN artists r ON
    r.ArtistId = l.ArtistId;  
*same column name*:  
SELECT
   Title, 
   Name
FROM
   albums
INNER JOIN artists USING(ArtistId);
#### left join
The LEFT JOIN clause selects data starting from the left table (artists) and matching rows in the right table (albums) based on the join condition (artists.ArtistId = albums.ArtistId). The left join returns all rows from the artists table (or left table) and the matching rows from the albums table (or right table).
SELECT
    Name, 
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
ORDER BY Name;
**inner join vs. left join:** The main difference between INNER JOIN and LEFT JOIN is that INNER JOIN only returns matching rows from both tables, while LEFT JOIN returns all rows from the left table and the matching rows from the right table, with NULL values for the columns from the right table if there is no match.  
#### cross join
The CROSS JOIN combines every row from the first table (table1) with every row from the second table (table2) to form the result set. If the first table has N rows, the second table has M rows, the final result will have NxM rows. A practical example of the CROSS JOIN clause is to combine two sets of data for forming an initial data set for further processing.  
SELECT
    select_list
FROM table1
CROSS JOIN table2;
#### self join
SELECT m.firstname || ' ' || m.lastname AS 'Manager',
       e.firstname || ' ' || e.lastname AS 'Direct report' 
FROM employees e
INNER JOIN employees m ON m.employeeid = e.reportsto
ORDER BY manager;  
The concatenation operator || concatenates multiple strings into a single string. In the example, we use the concatenation operator to from the full names of the employees by concatenating the first name, space, and last name.  
#### full outer join
In theory, the result of the FULL OUTER JOIN is a combination of  a LEFT JOIN and a RIGHT JOIN. The result set of the full outer join has NULL values for every column of the table that does not have a matching row in the other table. For the matching rows, the FULL OUTER JOIN produces a single row with values from columns of the rows in both tables.(并集)  
SELECT *
FROM dogs 
FULL OUTER JOIN cats
    ON dogs.color = cats.color;  
### group by
The GROUP BY clause is an optional clause of the SELECT statement. The GROUP BY clause a selected group of rows into summary rows by values of one or more columns.  
SELECT 
    column_1,
    aggregate_function(column_2) 
FROM 
    table
GROUP BY 
    column_1,
    column_2;  
SQLite allows you to group rows by multiple columns.  
SELECT
   MediaTypeId, 
   GenreId, 
   COUNT(TrackId)
FROM
   tracks
GROUP BY
   MediaTypeId, 
   GenreId;  
(the result will be like a tree as numpy: 1-1, 1-2, 1-3, 2-1...)
Group by data example:  
SELECT
   STRFTIME('%Y', InvoiceDate) InvoiceYear, (Invoice - InvoiceDate - %Y; STRFTIME is a SQLite function that formats a date and time value based on a specified format string. The function takes two arguments: the first is the format string, and the second is the date and time value to be formatted.)
   COUNT(InvoiceId) InvoiceCount
FROM
   invoices
GROUP BY
   STRFTIME('%Y', InvoiceDate)
ORDER BY
   InvoiceYear;  
### having
To filter groups, you use the GROUP BY with HAVING clause. For example, to get the albums that have more than 15 tracks, you use the following statement:  
SELECT
	tracks.albumid,
	title,
	COUNT(trackid)(this create a new column that counts number of appearance of this trackid)
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
GROUP BY
	tracks.albumid
HAVING COUNT(trackid) > 15;  
### sum, max, min, avg
You can use the SUM function to calculate total *per group*.(after GROUP BY)
SELECT
	albumid,
	SUM(milliseconds) length,
	SUM(bytes) size
FROM
	tracks
GROUP BY
	albumid;  
same for max, min, and avg  
SELECT
	tracks.albumid,
	title,
	min(milliseconds) minimum,
	max(milliseconds) maximum,
	round(avg(milliseconds),2) average
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
GROUP BY
	tracks.albumid;
### union
To combine rows(not columns!) from two or more queries into a single result set, you use SQLite UNION/UNION ALL operator. UNION delete duplicate rows, UNION ALL does not.  
"CREATE TABLE t1(
    v1 INT
);
 
INSERT INTO t1(v1)
VALUES(1),(2),(3);
 
CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);"  
SELECT v1
  FROM t1
UNION
SELECT v2
  FROM t2;  
现在我们有列名为v1的，数据为1，2，3，4的一列；如果是UNION ALL那就是1，2，3，2，3，4
SELECT FirstName, LastName, 'Employee' AS Type (AS用来给列名起别名)
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers
ORDER BY FirstName, LastName;  
### except
SQLite EXCEPT operator compares the result sets of two queries and returns distinct rows from the left query that are not output by the right query.  
SELECT select_list1
FROM table1
EXCEPT
SELECT select_list2
FROM table2  
### intersect
SQLite INTERSECT operator compares the result sets of two queries and returns distinct rows that are output by both queries.  
SELECT select_list1
FROM table1
INTERSECT
SELECT select_list2
FROM table2  
INNER JOIN is used to combine rows from two or more tables based on a matching condition, while INTERSECT is used to combine the results of two or more SELECT statements and return only the common rows between them.  
### subquery
A subquery is a SELECT statement nested in another statement.  
SELECT column_1
FROM table_1
WHERE column_1 = (
   SELECT column_1 
   FROM table_2
);  
### exists
The EXISTS operator is a logical operator that checks whether a subquery returns any row.  
EXISTS(subquery)  
NOT EXISTS (subquery)  
  
SELECT
    CustomerId,
    FirstName,
    LastName,
    Company
FROM
    Customers c
WHERE
    EXISTS (
        SELECT 
            1 
        FROM 
            Invoices
        WHERE 
            CustomerId = c.CustomerId
    )
ORDER BY
    FirstName,
    LastName;  
### case
The SQLite CASE expression evaluates a list of conditions and returns an expression based on the result of the evaluation.  
SELECT customerid,
       firstname,
       lastname,
       CASE country 
           WHEN 'USA' 
               THEN 'Domestic' 
           ELSE 'Foreign' 
       END CustomerGroup
FROM 
    customers
ORDER BY 
    LastName,
    FirstName;  
  
SELECT
	trackid,
	name,
	CASE
		WHEN milliseconds < 60000 THEN
			'short'
		WHEN milliseconds > 60000 AND milliseconds < 300000 THEN 'medium'
		ELSE
			'long'
		END category
FROM
	tracks;  
### insert
To insert data into a table, you use the INSERT statement. 
insert a single row:  
INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);  
  
insert multiple rows:  
INSERT INTO table1 (column1,column2 ,..)
VALUES 
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);
  
insert default values:  
INSERT INTO artists DEFAULT VALUES;
  
insert new rows with data provided by a SELECT statement:  
INSERT INTO artists_backup 
SELECT ArtistId, Name
FROM artists;  
### update
First, specify the table where you want to update after the UPDATE clause.  
Second, set new value for each column of the table in the SET clause.  
Third, specify rows to update using a condition in the WHERE clause. The WHERE clause is optional. If you skip it, the UPDATE statement will update data in all rows of the table.  
Finally, use the ORDER BY and LIMIT clauses in the UPDATE statement to specify the number of rows to update.  
  
UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition 
ORDER BY column_or_expression
LIMIT row_count OFFSET offset;  
### delete
DELETE FROM table
WHERE search_condition;
### replace
The idea of the REPLACE statement is that when a UNIQUE or PRIMARY KEY constraint violation occurs, it does the following: First, delete the existing row that causes a constraint violation. Second, insert a new row.  
REPLACE INTO table(column_list)
VALUES(value_list);  
if there is no value_list in column_list, REPLACE is like INSERT; if there is, REPLACE really replace.  
### transaction
In SQL, a transaction is a sequence of one or more SQL statements that are executed as a single, atomic unit of work. A transaction is a fundamental concept in database management systems (DBMS), which allows multiple users to access and manipulate the same data concurrently while maintaining the consistency, isolation, and durability of the data.  
BEGIN TRANSACTION;
  
UPDATE accounts SET balance = balance - 100 WHERE account_id = 123;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 456;
COMMIT;  
  
In this transaction, two UPDATE statements are executed to subtract $100 from account 123 and add $100 to account 456. If both statements complete successfully, the changes are committed to the database using the COMMIT statement. If any of the statements fail, the transaction is rolled back using the ROLLBACK statement, and the database is returned to its previous state.  
### data type
Storage Class | Meaning
--- | --- 
NULL | NULL values mean missing information or unknown.
INTEGER | Integer values are whole numbers (either positive or negative). An integer can have variable sizes such as 1, 2,3, 4, or 8 bytes.
REAL | Real values are real numbers with decimal values that use 8-byte floats.
TEXT | TEXT is used to store character data. The maximum length of TEXT is unlimited. SQLite supports various character encodings.
BLOB | BLOB stands for a binary large object that can store any kind of data. The maximum size of BLOB is, theoretically, unlimited.
### create table
CREATE TABLE (如果需要给表命名，在这里命名)[IF NOT EXISTS]（如果不存在，创建新表格；如果存在，则不操作） [schema_name]（隶属于哪一个schema.sql）.table_name (
	column_1 data_type PRIMARY KEY,（a primary key is a column or set of columns that uniquely identifies each row in a table. It is used to enforce the entity integrity constraint, which requires that each row in a table be uniquely identifiable.）
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	table_constraints
) [WITHOUT ROWID];（每行不会显示默认行数id）  
### alter table
*rename a table*  
ALTER TABLE existing_table
RENAME TO new_table;  
*add a new column*  
ALTER TABLE table_name
ADD COLUMN column_definition;  
*rename a column*
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;  
### drop table
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;  
### vacuum
In SQL, VACUUM is a command used to reclaim unused space and defragment the database file, reducing the file size and improving performance. It is used to free up space from deleted records and rows, which are marked as unused but not physically removed from the database file.  
VACUUM;
or  
PRAGMA auto_vacuum = FULL;  
### primary key
A primary key is a column or group of columns used to identify the uniqueness of rows in a table. Each table has one and only one primary key.  
one primary key:  
CREATE TABLE table_name(
   column_1 INTEGER NOT NULL PRIMARY KEY,
   ...
);  
multiple primary key:  
CREATE TABLE table_name(
   column_1 INTEGER NOT NULL,
   column_2 INTEGER NOT NULL,
   ...
   PRIMARY KEY(column_1,column_2,...)
);  
*If a table has the primary key that consists of one column, and that column is defined as INTEGER then this primary key column becomes an alias for the rowid column.*  
*if you declare a column with the INTEGER type and PRIMARY KEY DESC clause, this column will not become an alias for the rowid column*
### not null constraint
By default, all columns in a table accept NULL values except you explicitly use NOT NULL constraints.  
CREATE TABLE table_name (
    ...,
    column_name type_name NOT NULL,
    ...
);  
### unique constraint
A UNIQUE constraint ensures all values in a column or a group of columns are distinct from one another or unique.  
column level:  
CREATE TABLE table_name(
    ...,
    column_name type UNIQUE,
    ...
);  
table level:  
CREATE TABLE table_name(
    ...,
    UNIQUE(column_name)
);  
### check constraint
SQLite CHECK constraints allow you to define expressions to test values whenever they are inserted into or updated within a column.  
*check at column level:*  
CREATE TABLE table_name(
    ...,
    column_name data_type CHECK(expression),
    ...
);   
CREATE TABLE contacts (
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL,
    email      TEXT,
    phone      TEXT    NOT NULL
                    CHECK (length(phone) >= 10) 
);  
*check at table level:*  
CREATE TABLE table_name(
    ...,
    CHECK(expression)
);  
CREATE TABLE products (
    product_id   INTEGER         PRIMARY KEY,
    product_name TEXT            NOT NULL,
    list_price   DECIMAL (10, 2) NOT NULL,
    discount     DECIMAL (10, 2) NOT NULL
                                DEFAULT 0,
    CHECK (list_price >= discount AND 
        discount >= 0 AND 
        list_price >= 0) 
);  
### autoincrement  
SQLite recommends that you should not use AUTOINCREMENT attribute because:
The AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.
In addition, the way SQLite assigns a value for the AUTOINCREMENT column slightly different from the way it does for the rowid column.  
### create view
In database theory, a view is a result set of a stored query. A view is the way to pack a query into a named object stored in the database. （符合条件的一组查询，可以理解为编程中的method，之后就照名字call就可以了）  
CREATE [TEMP] (使用TEMP表示你希望这个view只与当前数据库有联系，当前数据库关闭，这玩意也就没了) VIEW [IF NOT EXISTS] view_name[(column-name-list)] (This is useful when you want to create a view that contains only a subset of the columns from the underlying tables. 如果不说明，那就是符合select条件的整个表)
AS 
   select-statement;  
### drop view
DROP VIEW [IF EXISTS] (不存在就啥都不干) [schema_name.]view_name;（在本地唯一的db上操作可以不说明schema_name）  
### index
an index is a data structure that provides quick access to data in a table based on the values in one or more columns. Each index must be associated with a specific table. An index consists of one or more columns, but all columns of an index must be in the same table. A table may have multiple indexes.  
*create:*  
CREATE [UNIQUE] INDEX index_name 
ON table_name(column_list);  
*drop:*  
DROP INDEX [IF EXISTS] index_name;
### expression-based index
CREATE INDEX name_index ON employees(first_name || ' ' || last_name);  
This creates an index on the concatenated string of the first and last names of each employee in the employees table. Same to use SELECT, FROM, WHERE, ORDER BY, just faster.  
### trigger
An SQLite trigger is a named database object that is executed automatically when an INSERT, UPDATE or DELETE statement is issued against the associated table. 
*create:*   
CREATE TRIGGER [IF NOT EXISTS] trigger_name 
   [BEFORE|AFTER|INSTEAD OF] (trigger在遇到命令的‘什么时候’应该被触发？) [INSERT|UPDATE|DELETE] （trigger遇到‘什么命令’的时候应该被触发？）
   ON table_name
   [WHEN condition]
BEGIN
 statements;
END;

real example:  
CREATE TRIGGER validate_email_before_insert_leads 
   BEFORE INSERT 
   ON leads
BEGIN
   SELECT
      CASE
	WHEN NEW.email NOT LIKE '%_@__%.__%' THEN (new用来指代新加的那一行，.email表示我们关注的是邮箱地址这一列)
   	  RAISE (ABORT,'Invalid email address') （To validate the email, we used the LIKE operator to determine whether the email is valid or not based on the email pattern. If the email is not valid, the RAISE function aborts the insert and issues an error message.）
       END;
END;  
  
*drop:*
DROP TRIGGER [IF EXISTS] trigger_name;  
### instead of triggers
In SQLite, an INSTEAD OF trigger can be only created based on a view, not a table: the INSTEAD OF triggers allow read-only views to become modifiable.  
CREATE TRIGGER [IF NOT EXISTS] schema_ame.trigger_name
    INSTEAD OF [DELETE | INSERT | UPDATE OF column_name]
    ON table_name
BEGIN
    -- insert code here
END;  
  
real example:  
CREATE TRIGGER insert_artist_album_trg
    INSTEAD OF INSERT ON AlbumArtists
BEGIN
    -- insert the new artist first
    INSERT INTO Artists(Name)
    VALUES(NEW.ArtistName);
    
    -- use the artist id to insert a new album
    INSERT INTO Albums(Title, ArtistId)
    VALUES(NEW.AlbumTitle, last_insert_rowid());
END;  
### full-text search
virtual table: when you access a virtual table, SQLite calls the custom code to get the data. The custom code can have specified logic to handle certain tasks such as getting data from multiple data sources.  
full-text search in SQL is a technique used to search for text within a large amount of unstructured or semi-structured data. It requires the creation of a full-text index and the use of specialized search functions such as CONTAINS or FREETEXT.(纯数据库技巧或许处理结构化的数据很有用，但是“用户-帖子”的twitter中找关键字就很不好使了)   
CREATE VIRTUAL TABLE table_name 
USING FTS5(column1,column2...);  
   
SELECT column_list
FROM table_name
WHERE CONTAINS(column_name, 'search_criteria');  
### SQLite commands
start:   
> sqlite3  








