# Your paper and video summaries go here.

# Rubric:
* Write a short summary of the paper/video, as follows:
* First line: Paper Title, citation source
* Keywords: List keywords from paper, or select 4-8 most relevant terms from the paper
* First paragraph: describe the main points of the paper/video.
* Second paragraph: Present the paper/video's strengths and weaknesses from your point of view.

### Title: JavaScript Fundamentals; https://info340.github.io/javascript.html  
**Keywords:** Client-side; Web Development; Variables; Data Types; Functions; Control Structures; Arrays; Objects  
**Summary:** In this chapter, the author introduced JavaScript, a high-level, interpreted, and general-purpose programming language. It is possible for user to run JavaScript in the browser or on the command line, but whichever way we choose, the author suggests using strict mode. Variables in JS are dynamically typed, and its data types are numbers, strings and booleans. Java also supports arrays and objects, though nothing related to OOP. Type coercion is a useful feature of JS, as the computer can help you decide how to reconcile the type conflict. Control structures are similar to that of Java, but JS has ternary conditional operator to make things easier. JS also have functions.  
**Opinion:** The strength of this chapter might be it provides an introduction to the fundamental concepts of programming with JavaScript, and includes practical examples and exercises to reinforce the learning process. The weakness might be it may require additional resources to gain a deeper understanding of JavaScript programming.

functionally scoped:  
"
function exampleFunction() {
  var message = "Hello, world!"; // message is only accessible within this function
  console.log(message);
  
  function nestedFunction() {
    console.log(message); // message is also accessible within this nested function
  }
  
  nestedFunction();
}
exampleFunction(); // output: "Hello, world!"
"  

join()
"
const fruits = ['apple', 'banana', 'cherry'];
const joinedFruits = fruits.join(', ');
console.log(joinedFruits); // "apple, banana, cherry"
"  

for...in not recommended in js:  
"
const arr = [1, 2, 3];
arr[10] = 10;
for (let i in arr) {
  console.log(i); // logs "0", "1", "2", "10"
}
"  

### Title: Chapter 1 of 'Refactoring'; https://learning.oreilly.com/library/view/refactoring-improving-the/9780134757681/ch01.xhtml#ch01lev1sec1
**Keywords:** 
**Summary:**
**Opinion:**

### Title: 'Automated Testing with Mocha'; https://javascript.info/testing-mocha 
**Keywords:** 
**Summary:**
**Opinion:**

### Title: 'Getting Started in JavaScript'; https://plotly.com/javascript/getting-started/
**Keywords:** 
**Summary:**
**Opinion:**

### Extra Work: Chapter 1, The Pragmatic Programmer: your journey to mastery, 20th Anniversary Edition, 2nd Edition
**Excerpts:** Good Design Is Easier to Change Than Bad Design; DRY—Don't Repeat Yourself; Make It Easy to Reuse; Eliminate Effects Between Unrelated Things; There Are No Final Decisions; Forgo Following Fads;Use Tracer Bullets to Find the Target; Prototype to Learn; Program Close to the Problem Domain; Estimate to Avoid Surprises; Iterate the Schedule with the Code
**Summary:** The chapter presents several tips and techniques to help programmers become more effective, such as adopting a "tracer bullet" approach to prototyping and building software incrementally, using automation to reduce the amount of manual work, and continuously improving code through refactoring. The authors also stress the importance of communication, teamwork, and a focus on creating software that meets the needs of users. Overall, the chapter serves as a practical guide to help programmers become more skilled and successful in their work.
