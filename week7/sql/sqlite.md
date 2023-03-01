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
NULL | NULL values mean missing information or unknown.
INTEGER | Integer values are whole numbers (either positive or negative). An integer can have variable sizes such as 1, 2,3, 4, or 8 bytes.
REAL | Real values are real numbers with decimal values that use 8-byte floats.
TEXT | TEXT is used to store character data. The maximum length of TEXT is unlimited. SQLite supports various character encodings.
BLOB | BLOB stands for a binary large object that can store any kind of data. The maximum size of BLOB is, theoretically, unlimited.



