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
It matches each row from the albums table with every row from the artists table based on the join condition (artists.ArtistId = albums.ArtistId) specified after the ON keyword. If the join condition evaluates to true (or 1), the columns of rows from both albums and artists tables are included in the result set.  
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

#### full outer join