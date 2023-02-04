# Your paper and video summaries go here.

# Rubric:
* Write a short summary of the paper/video, as follows:
* First line: Paper Title, citation source
* Keywords: List keywords from paper, or select 4-8 most relevant terms from the paper
* First paragraph: describe the main points of the paper/video.
* Second paragraph: Present the paper/video's strengths and weaknesses from your point of view.

Title: On the Criteria To Be Used in Decomposing Systems into Modules; https://sakai.duke.edu/access/content/group/FINTECH-512-02-Sp22/Papers/On%20the%20Criteria%20To%20Be%20Used%20in%20Decomposing%20Systems%20into%20Modules%20Parnas.pdf; https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/
Keywords: Decomposing systems; Modules; Criteria; Ease of change; Reusability; Interactions; Functionality
Summary: This article by David Parnass presents criteria that can be used when decomposing a system into smaller, more manageable components (called modules). The paper argues that the main criteria for decomposition should be the ease of changing the system and the ability to reuse components in other systems. It also states that interactions between components should be kept to a minimum and the function of each module should be clearly defined. The document also emphasises the importance of considering human factors in system design, such as developers' ability to understand and use the system.
Opinion: For the strength, it highlights the importance of considering human factors: The paper suggests that the human factors involved in system design, such as the ability of developers to understand and work with the system, should also be taken into account. For the weakness, it does not explain how the criteria should be implemented, which could make it difficult for readers to apply the concepts in practice.

Title: Rediscovering Simplicity; https://sandimetz.com/99bottles-sample-js#chapter-rediscovering-simplicity
Keywords: Simplicity; Software design; Complexity; DRY; Maintainability; Readability
Summary: This chapter on a sample implementation of "99 bottles of beer" came up with "incomprehensibly concise", "speculatively general", "concretely abstract" and "shameless green" codes, to tell us the value of simplicity in code, and how this simplicity can be lost as the complexity of software systems increases. The author introduced 3 ways to measure the complexity of codes, namely, source line of code, cyclomatic complexity, and assignment & branches & conditions metric. Later, a test driven development process for "shameless green" was conducted to show how we should start and remove duplication in codes. Also, the importance of staying focused on what is essential and avoiding over-engineering solutions was also emphasized in the chapter.
Opinion: For the strength, it emphasizes the importance of simplicity in software design and development, and how it can improve the maintainability and extensibility of a system. For the weakness, it may not provide comprehensive detail on how to implement the TDD for "99 bottles". 

Title: Modern Code Review; https://learning.oreilly.com/library/view/making-software/9780596808310/ch18.html
Keywords: Code review; Software development; Collaboration; Quality assurance; Pull requests; Continuous integration; Peer review; Constructive feedback
Summary: The chapter discusses the best practices and techniques for code review in modern software development. It covers the benefits of code review, such as improved code quality, better collaboration, and knowledge sharing among developers. The author pointed out the existence of focus fatigue and recommended a reasonable code review time and quantity. It also covers different code review methods, such as self inspection, pair programming, and formal group meeting. The author conclude from statistics that while external reviewers can discover more subtle problems, self inspection is more cost-efficiency. 
Opinion: For the strength, it covers how to handle common challenges that arise during code reviews, such as dealing with conflicting feedback, handling sensitive code and how to give and receive constructive feedback. For the weakness, it may not take into account the specific needs and constraints of different types of organizations or projects.

Title: Checklist in Greiler Code Review EBook; //unaccessible //

Title: SOLID Object-Oriented Design, Sandi Metz; https://www.youtube.com/watch?v=v-2yFMzxqwU
Keywords: OOD; SOLID; DRY; configuration; dependency; red, green and refactor
Summary: Prof. Metz started by pointing out several fallacies in OOP: rigid, fragile, immobile, viscous. Then she introduced SOLID principles in OOD, which stands for Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principle. She also implement those principles in the revision of an actual progam using TDD. Each time she went through the red-green-refactor process, she asked herself: Is it DRY? Does it have one responsibility? Does everything change at the same rate? Does it depend on things that change less than it does? She also introduced "Triangle of Responsibility" in refactoring: refactor; extract - Pull functionality out where necessary; inject - Inject that new dependency into place from which it was extracted. 
Opinion: The strength might be Prof. Metz provides concrete examples to illustrate each of the SOLID principles, making the content of the speech both easy to understand and useful for practical applications. The weakness might be the speech assumes that the audience is already familiar with object-oriented programming and especially, Ruby, which I am not, and it was a bit difficult for me when she went to those codes.
URL for speaker deck: https://speakerdeck.com/skmetz/solid-object-oriented-design?slide=141

Some extra work...
Title: Hints and Principles of Computer System Design
Summary:
This paper suggests the goals you might have for your system — Simple, Timely, Efficient, Adaptable, Dependable, Yummy (STEADY) — and techniques for achieving them — Approximate, Incremental, Divide & Conquer (AID). It also gives some principles for system design that are more than just hints, and many examples of how to apply the ideas.
− Keep it simple. Complexity kills.
− Write a spec. At least, write down the abstract state.
− Build with modules, parts of the system that people can work on independently
− Exploit the ABCs of efficiency: algorithms, approximate, batch, cache, concurrency.
− Treat the state as both being and becoming: map vs. log, pieces, checkpoints, indexes.
− Use eventual consistency to keep data available locally.

