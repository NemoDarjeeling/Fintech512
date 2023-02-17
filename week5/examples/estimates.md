Create a new Flask application;  
Define the invoice and plays dictionaries that will be used in the statement function;  
Import the Blueprint class from Flask and create a new blueprint called "examples";  
Create a new route in the blueprint called "statement" that returns an HTML version of the invoice statement. You can use the render_template function from Flask to render an HTML template that displays the invoice statement;  
Create a new HTML template called statement.html in a folder called templates. This template should display the invoice statement, along with the total amount owed and the volume credits earned;  
Copy index.html and index.js + data folder into template directory, add route('/stockchart') and render_template('index.html')