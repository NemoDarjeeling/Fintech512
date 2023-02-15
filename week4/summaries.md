# Your paper and video summaries go here.

# Rubric:
* Write a short summary of the paper/video, as follows:
* First line: Paper Title, citation source
* Keywords: List keywords from paper, or select 4-8 most relevant terms from the paper
* First paragraph: describe the main points of the paper/video.
* Second paragraph: Present the paper/video's strengths and weaknesses from your point of view.

### Title: [Kevlin Henney - The SOLID Design Principles Deconstructed](https://www.youtube.com/watch?v=tMW08JkFrBA)  
**Keywords:** SOLID design principles, software development, purpose, benefits, limitations, practical examples  
**Summary:** Kevlin Henney provides a comprehensive overview and critique of the five SOLID design principles in software development. He explains the purpose, benefits, and limitations of each principle, and provides practical examples to illustrate his points. For SRP, there are many cases that it is violated, for instance, cost(cheaper for a clustered class), measure(3 normal classes vs. 3 2000-line classes), utility-reality(stdlib), change not usage. For ISP, he argued if one can faithfully implement SRP, he/she should have implemented ISP as well. For LSP, sometimes "inheritance" patterns are found in non-inheritance relationships, and B.L was just providing examples, not doctrine. For OCP, unchanged != compatible, so it is not really the right principle for OOP(it's actually more related to data framework); and publish != public, I can change whatever I want for latter but not for former. For DIP, it is useful.  
**Opinion:** The strength of this speech might be clear and concise explanations of each SOLID design principle, and critique of the limitations of each principle with very concrete examples. The weakness might be the speech may not have provided enough in-depth information or practical solutions: what should we rely on if SOLID has been somewhat disproven?  

### Extra Work: Chapter 1, The Pragmatic Programmer: your journey to mastery, 20th Anniversary Edition, 2nd Edition
**Excerpts:** You Have Agency; Provide Options, Don't Make Lame Excuses; Don't Live with Broken Windows; Be a Catalyst for Change; Remember the Big Picture; Make Quality a Requirements Issue; Invest Regularly in Your Knowledge Portfolio; Critically Analyze What You Read and Hear; English is Just Another Programming Language; It's Both What You Say and the Way You Say It; Build Documentation In, Don't Bolt It On  
**Summary:** Chapter 1 of "The Pragmatic Programmer" introduces the concept of pragmatic philosophy, which is a practical and problem-solving approach to software development. The authors argue that a programmer's mindset, attitude, and approach can have a significant impact on their work and the quality of the software they produce. The chapter outlines the core principles of a pragmatic philosophy, including the importance of flexibility, understanding the problem at hand, and always striving for excellence. The authors also emphasize the importance of continuously learning and adapting to new technologies and trends in the field. Overall, the chapter sets the stage for the rest of the book and provides a foundation for the reader to become a more effective and efficient software developer.
  
**The difference between session and g:** While both sessions and global variables can be used to store data in web development, they serve different purposes. Sessions are primarily used for storing user-specific data that needs to persist across multiple requests, while global variables are used for storing data that needs to be accessible from multiple parts of a program.
