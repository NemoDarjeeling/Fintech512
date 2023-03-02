### How many customers are in the database?
59; SELECT * FROM customers
### As measured by number of tracks sold, what is the most popular genre?
本质上是tracks.genreid和invoice_items.trackid数的两列(track中每一条记录是一个唱片的销售记录)即可，但是需要genres.name对应id,需要tracks.trackid将tracks.genreid和invoice_items.trackid对应起来
SELECT 
    genres.name,
    tracks.genreid,
    COUNT(invoice_items.trackid)
FROM 
    genres,
    invoice_items,
    tracks
WHERE
    genres.genreid = tracks.genreid AND
    invoice_items.trackid = tracks.trackid
GROUP BY
    tracks.genreid
ORDER BY
    COUNT(invoice_items.trackid) DESC;
 
### As measured by number of tracks sold, what is the least popular genre?
SELECT 
    genres.name,
    tracks.genreid,
    COUNT(invoice_items.trackid)
FROM 
    genres,
    invoice_items,
    tracks
WHERE
    genres.genreid = tracks.genreid AND
    invoice_items.trackid = tracks.trackid
GROUP BY
    tracks.genreid
ORDER BY
    COUNT(invoice_items.trackid);

### Who is the most popular artist, as measured by number of tracks sold?
NAME-artistid-albumid-trackid 
SELECT 
    artists.name,
    COUNT(invoice_items.trackid)
FROM
    artists,
    albums,
    tracks,
    invoice_items
WHERE
    artists.artistid = albums.artistid
    AND albums.albumid=tracks.albumid
    AND tracks.trackid=invoice_items.trackid
GROUP BY
    artists.artistid
ORDER BY
    COUNT(invoice_items.trackid) DESC LIMIT 3;

### How many albums by 'Miles Davis' are in the database?
artist_name-artist_id-album_title
SELECT
    artists.name,
    count(albums.albumid)
FROM 
    albums,
    artists
WHERE
    albums.artistid = artists.artistid
    AND artists.name = 'Miles Davis'
GROUP BY
    artists.name;

### What is the name of the longest song in the database?
tracks.milliseconds-tracks.albumid-tracks.name
SELECT
    tracks.name,
    tracks.milliseconds
FROM
    tracks
ORDER BY
    tracks.milliseconds DESC LIMIT 5;

### What is the title and length (in milliseconds) of the longest album in the database?
albums.title-albums.albumid-tracks.albumid-sum(tracks.milliseconds)
group by tracks.albumid
SELECT
    albums.title,
    tracks.albumid,
    sum(tracks.milliseconds) length
FROM
    albums,
    tracks
WHERE
    albums.albumid = tracks.albumid
GROUP BY
    tracks.albumid
ORDER BY
    length DESC LIMIT 5;

### What is the invoice id, amount, and customer name of the most expensive invoice?
customers.firstname, customers.lastname-customers.customerid-invoices.customerid-invoices.id-invoices.total
SELECT
    invoices.invoiceid,
    invoices.total,
    customers.firstname, 
    customers.lastname
FROM 
    customers,
    invoices
WHERE
    customers.customerid = invoices.customerid
ORDER BY
    invoices.total DESC LIMIT 10;   

### What is the name of the customer who has spent the most?
SELECT
    invoices.customerid,
    customers.firstname, 
    customers.lastname,
    SUM(invoices.total) total_spending
FROM 
    customers,
    invoices
WHERE
    customers.customerid = invoices.customerid
GROUP BY
    invoices.customerid
ORDER BY
    total_spending DESC LIMIT 10; 

