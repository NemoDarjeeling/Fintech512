My code:
    SLOC: 46 lines;
    ABC Metric: 23
        Assignments: 15
        Branches: 0
        Conditions: 8

Sihan Wang's code:
    SLOC:49 lines;
    ABC Metric: 27
        Assignments: 15
        Branches: 4
        Conditions: 8    

code suggestions: now all of the code is clustered in one main() function and it is not OOP either; moreover it is so rigid that a small change in the user environment will require drastic change in the code. Haochen should make more methods to call / send messages, while looking for ways to make classes.

SOLID principle: 
The principle of single responsibility is violated, since all code and functions are clustered in main, where there should be at least these functions: read from an input, write to an output, store the wordlists, parse the wordlists, get the keywords, locate keywords in titles and capitalize keywords.
The principle of open-closed is violated, since the program is rigid. There can only be modifications on original code, rather than allowing for extensions.
It is difficult to say whether the program violate or stick with Liskov's substitution principle, as there is no classes, let alone subclasses.
The principle of interface segregation is yet a problem, but since the codes are all clustered in main function, it is reasonble to assume that if the user want to use some function, he/she has to run previous codes as well.
The principle of dependency inversion is also violated. In the code, everything is tangled and heavily relies on details rather than abstractions.

Q: Input format: What if, rather than a single input text file, there were separate 'ignore' and 'titles' files? What if the input format was JSON or XML? What if the input was stored in a database?
A: This is easy as my new program allows for more extensions. For instance, now I call stdIn() to read from standard input before I call other methods to actually parse the strings, I can write new methods and call it first, for instance fileIn() or dbIn(), and then I shall call all other methods as before to actually parse the strings. As long as I can make sure the input can be turned into ordinary strings, there is little change required for other methods.

Q: 'all lines stored in core (memory)' What would need to change if you had enough room to store the ignore words and keywords, but not enough room to store all of the titles, e.g. if the keywords were stock symbols and the code were being used to filter daily tweets for information about the stocks?
A: In this situation, I think other codes regarding "ig_words" and "key_words" need little change, but I may need to write new methods to store "sentences" and subsequent "all_words" elsewhere. A viable way might be still parsing information about titles within my program, but as soon as one title finished parsing, it will be send to another method, which stores the information in an external file. This way, we can save memory while executing, but still get a file with all parsed titles.

Q: Adding a 'rotate'/shift' feature to display the keywords in the same column of the output as in the problem description?
A: Since this "rotate/shift" action happens later than my program gets the answer and before I call stdOut(), I think inserting a rotate() method in between is possible. A viable way to implement this method might be: iterate though all lines of titles, track the index of the first upperclass character(word) for each line; compare the index to get the biggest one; for index in each line, if index_this_line != index_biggest, insert spaces at the head of this line until index_this_line == index_biggest, and we shall have what we want by now.

Q: Sort the keywords as they arrive rather than once they have all been collected?
A: It is possible to sort the keywords once they arrive, for my code, it would require calling strToList(), parseAW() and parseKW() multiple times to update keyword list to the newest version and sort it. But such task might be difficult to perform when we are using input from std::in, as 

Q: How easy/hard would it be to run your KWIC tests against your partner's code?
A: It is easier to read as each step is very clear, but more difficult to make changes or test smaller functions in the program, as my code is POP rather than OOP. It is rigid and fragile.

Explanation for CRC cards created for the Flask website:
Here are the CRC cards, modification in class included:
Name: Flask 
Responsibility: run .py programs, render template, reads configuration
Interaction: templates, webserver, WSGI

Name: APP
Responsibility: run.py and get result; generate contact based on the request
Interaction: flask, template, request

Name: Webserver
Responsibility: connects http; fill WSEI
Interaction: flask

Name: WSGI
Responsibility: receives incoming http; call the flask application; return response to web server
Interaction: server, flask, request

Name: Browser
Responsibility: send http request; receive http response; process file
Interaction: server

Name: Template
Responsibility: contain html structure
Interaction: flask

The system works like this: first, the Browser sends an HTTP request to the Webserver. Then the Webserver connects the HTTP request and fills the WSGI. The WSGI will receive the incoming HTTP request and calls the Flask application, while the Flask application will use the run.py file, generate a response based on the request and the configuration specified in the Flask instance. The Flask application also renders the template, which contains the HTML structure, and returns the response to the WSGI, which will return the response to the Webserver. At last, the Webserver sends the HTTP response to the Browser, and volia, the file will be processed and the result will be displayed to the user. 
In short, the Flask is a system that collectively processes HTTP requests from browsers, generates responses, and displays results to users. Different components of the system interact to achieve this goal, and the Flask application is the main component for processing requests and generating responses.