### estimations for the steps are here:  

1. Create a new Flask application;  
2. Define the invoice and plays dictionaries that will be used in the statement function;  
3. Import the Blueprint class from Flask and create a new blueprint called "examples";  
4. Create a new route in the blueprint called "statement" that returns an HTML version of the invoice statement. You can use the render_template function from Flask to render an HTML template that displays the invoice statement;  
5. Create a new HTML template called statement.html in a folder called templates. This template should display the invoice statement, along with the total amount owed and the volume credits earned;  
6. Copy index.html and index.js + data folder into template directory
7. add route('/stockchart') and render_template('index.html')