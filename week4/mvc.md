"Model-View-Controller" is a widely used design pattern in software engineering, which separates different concerns into three distinct componets. 
In the design of the Flask tutorial application, the "Model" refers to the SQlite database (in other words, data model) which is responsible for storing and retreiving data. 
"View" refers to all rendered html pages returned with responses. 
Unlike the "Model" which is hidden from customers, "View" faces customers and can be used to get responses from customers for further processing. 
"Controller" in this tutorial application is functions in blog.py and auth.py, they act as a connection between the "View" and "Model". 
"Controller" can process the data get from the customers via "View" and change the data stored in the "Model" or fetch data stored in the "Model" accordingly.
