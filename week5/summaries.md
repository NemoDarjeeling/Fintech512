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
<pre><code>
function exampleFunction() {
  var message = "Hello, world!"; // message is only accessible within this function
  console.log(message);
  
  function nestedFunction() {
    console.log(message); // message is also accessible within this nested function
  }
  
  nestedFunction();
}
exampleFunction(); // output: "Hello, world!"
</code></pre>  

join()
<pre><code>
const fruits = ['apple', 'banana', 'cherry'];
const joinedFruits = fruits.join(', ');
console.log(joinedFruits); // "apple, banana, cherry"
</code></pre>

for...in not recommended in js:  
<pre><code>
const arr = [1, 2, 3];
arr[10] = 10;
for (let i in arr) {
  console.log(i); // logs "0", "1", "2", "10"
}
</code></pre>

### Title: Chapter 1 of 'Refactoring'; https://learning.oreilly.com/library/view/refactoring-improving-the/9780134757681/ch01.xhtml#ch01lev1sec1
**Keywords:** 
**Summary:**
**Opinion:**

code before refactoring:  
<pre><code>
function statement (invoice, plays) {
  let totalAmount = 0;
  let volumeCredits = 0;
  let result = `Statement for ${invoice.customer}\n`;
  const format = new Intl.NumberFormat("en-US",
                        { style: "currency", currency: "USD",
                          minimumFractionDigits: 2 }).format;
  for (let perf of invoice.performances) {
    const play = plays[perf.playID];
    let thisAmount = 0;

    switch (play.type) {
    case "tragedy":
      thisAmount = 40000;
      if (perf.audience > 30) {
        thisAmount += 1000 * (perf.audience - 30);
      }
      break;
    case "comedy":
      thisAmount = 30000;
      if (perf.audience > 20) {
        thisAmount += 10000 + 500 * (perf.audience - 20);
      }
      thisAmount += 300 * perf.audience;
      break;
    default:
        throw new Error(`unknown type: ${play.type}`);
    }

    // add volume credits
    volumeCredits += Math.max(perf.audience - 30, 0);
    // add extra credit for every ten comedy attendees
    if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);

    // print line for this order
    result += `  ${play.name}: ${format(thisAmount/100)} (${perf.audience} seats)\n`;
    totalAmount += thisAmount;
  }
  result += `Amount owed is ${format(totalAmount/100)}\n`;
  result += `You earned ${volumeCredits} credits\n`;
  return result;
}
</code></pre>

code after first stage refactoring:  
<pre><code>
function statement (invoice, plays) {
  let result = `Statement for ${invoice.customer}\n`;
  for (let perf of invoice.performances) {
    result += `  ${playFor(perf).name}: ${usd(amountFor(perf))} (${perf.audience} seats)\n`;
  }
  result += `Amount owed is ${usd(totalAmount())}\n`;
  result += `You earned ${totalVolumeCredits()} credits\n`;
  return result;

  function totalAmount() {
    let result = 0;
    for (let perf of invoice.performances) {
      result += amountFor(perf);
    }
    return result;
  }

  function totalVolumeCredits() {
    let result = 0;
    for (let perf of invoice.performances) {
      result += volumeCreditsFor(perf);
    }
    return result;
  }
  function usd(aNumber) {
    return new Intl.NumberFormat("en-US",
                        { style: "currency", currency: "USD",
                          minimumFractionDigits: 2 }).format(aNumber/100);
  }
  function volumeCreditsFor(aPerformance) {
    let result = 0;
    result += Math.max(aPerformance.audience - 30, 0);
    if ("comedy" === playFor(aPerformance).type) result += Math.floor(aPerformance.audience / 5);
    return result;
  }
  function playFor(aPerformance) {
    return plays[aPerformance.playID];
  }
  function amountFor(aPerformance) {
    let result = 0;
    switch (playFor(aPerformance).type) {
    case "tragedy":
      result = 40000;
      if (aPerformance.audience > 30) {
        result += 1000 * (aPerformance.audience - 30);
      }
      break;
    case "comedy":
      result = 30000;
      if (aPerformance.audience > 20) {
        result += 10000 + 500 * (aPerformance.audience - 20);
      }
      result += 300 * aPerformance.audience;
      break;
    default:
        throw new Error(`unknown type: ${playFor(aPerformance).type}`);
    }
    return result;
  }
}
</code></pre>

from nested functions to object attributes:  
<code><pre>
function statement (invoice, plays) {
  return renderPlainText(createStatementData(invoice, plays));
}

function createStatementData(invoice, plays) {
  const statementData = {};
  statementData.customer = invoice.customer;
  statementData.performances = invoice.performances.map(enrichPerformance);
  statementData.totalAmount = totalAmount(statementData);
  statementData.totalVolumeCredits = totalVolumeCredits(statementData);
  return statementData;
</code></pre>

polymorphism:  
<code><pre>
export default function createStatementData(invoice, plays) {
  const result = {};
  result.customer = invoice.customer;
  result.performances = invoice.performances.map(enrichPerformance);
  result.totalAmount = totalAmount(result);
  result.totalVolumeCredits = totalVolumeCredits(result);
  return result;

  function enrichPerformance(aPerformance) {
    const calculator = createPerformanceCalculator(aPerformance, playFor(aPerformance));
    const result = Object.assign({}, aPerformance);
    result.play = calculator.play;
    result.amount = calculator.amount;
    result.volumeCredits = calculator.volumeCredits;
    return result;
  }
  function playFor(aPerformance) {
    return plays[aPerformance.playID]
  }
  function totalAmount(data) {
    return data.performances
      .reduce((total, p) => total + p.amount, 0);
  }
  function totalVolumeCredits(data) {
    return data.performances
      .reduce((total, p) => total + p.volumeCredits, 0);
  }
}

function createPerformanceCalculator(aPerformance, aPlay) {
    switch(aPlay.type) {
    case "tragedy": return new TragedyCalculator(aPerformance, aPlay);
    case "comedy" : return new ComedyCalculator(aPerformance, aPlay);
    default:
        throw new Error(`unknown type: ${aPlay.type}`);
    }
}
class PerformanceCalculator {
  constructor(aPerformance, aPlay) {
    this.performance = aPerformance;
    this.play = aPlay;
  }
  get amount() {
    throw new Error('subclass responsibility');}
  get volumeCredits() {
    return Math.max(this.performance.audience - 30, 0);
  }
}
class TragedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = 40000;
    if (this.performance.audience > 30) {
      result += 1000 * (this.performance.audience - 30);
    }
    return result;
  }
}
class ComedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = 30000;
    if (this.performance.audience > 20) {
      result += 10000 + 500 * (this.performance.audience - 20);
    }
    result += 300 * this.performance.audience;
    return result;
  }
  get volumeCredits() {
    return super.volumeCredits + Math.floor(this.performance.audience / 5);
  }
}
</code></pre>

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
