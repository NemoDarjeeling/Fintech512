### How many customers are in the database?
select count(*) from customers;

59
 
### As measured by number of tracks sold, what is the most popular genre?
select g.name, count(i.trackid)
from tracks t, genres g, invoice_items i
where t.genreid=g.genreid and t.trackid=i.trackid
group by t.genreid order by count(i.trackid) desc limit 1;
 
Rock|835
 
### As measured by number of tracks sold, what is the least popular genre?
select g.name, count(i.trackid)
from tracks t, genres g, invoice_items i
where t.genreid=g.genreid and t.trackid=i.trackid
group by t.genreid order by count(i.trackid) limit 1;
 
Tie:
Rock And Roll|6
Science Fiction|6
 
### Who is the most popular artist, as measured by number of tracks sold?
select ar.name, count(i.trackid)
from
artists ar,
albums al,
tracks t,
invoice_items i
where ar.artistid=al.artistid
and al.albumid=t.albumid
and t.trackid=i.trackid
group by ar.artistid order by count(t.trackid) desc limit 1;
 
Iron Maiden|140
 
### How many albums by 'Miles Davis' are in the database?
select ar.name, count(al.Title)
from
artists ar,
albums al
where ar.artistid=al.artistid and ar.name='Miles Davis'
group by ar.artistid;
 
Miles Davis|3
 
### What is the name of the longest song in the database?
select t.name, t.milliseconds from tracks t order by t.milliseconds desc limit 1;
 
Occupation / Precipice|5286953
 
### What is the title and length (in milliseconds) of the longest album in the database?
select al.title, sum(t.milliseconds) length
from albums al, tracks t
where al.albumid=t.albumid
group by al.title
order by sum(t.milliseconds) desc limit 1;
 
Lost, Season 3|70665582

### What is the invoice id, amount, and customer name of the most expensive invoice? What is the name of the customer who has spent the most?
select i.invoiceid, i.total, c.FirstName, c.LastName
from invoices i, customers c
where i.customerid=c.customerid
and i.total = (select max(total) from invoices);
 
404|25.86|Helena|Holý
 
### What is the name of the customer who has spent the most?
select c.FirstName, c.LastName, sum (i.total)
from invoices i, customers c
where i.customerid=c.customerid
group by c.customerid
order by sum(i.total) desc limit 1;
 
Helena|Holý|49.62