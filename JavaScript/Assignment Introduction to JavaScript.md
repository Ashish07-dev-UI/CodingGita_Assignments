# Assignment: Introduction to JavaScript









#### Section A: Short Answer Questions (1 Mark each)







##### Q1. What is JavaScript?



=> JavaScript is a high-level, dynamically typed programming language used to create interactive websites and applications.







##### Q2. Who created JavaScript and in which year?



=> Created in 1995 by Brendan Eich at Netscape.







##### Q3. What was the original name of JavaScript?



=> Mocha is the original name of JavaScript.





##### Q4. Is JavaScript the same as Java? Give one major difference.



=> JavaScript and Java are different programming languages. JS is a Dynamically typed type \& Java is a Statically type>





##### Q5. What does it mean when we say JavaScript is a high-level programming language?



=> when we say JavaScript is a high-level programming language we mean  that JavaScript is simple, human readable language.





##### Q6. Is JavaScript a compiled language or an interpreted language? Explain briefly.



=> JavaScript is a interpreted. JavaScript code is executed by a JavaScript engine while the program runs,





##### Q7. Name the JavaScript engines used by the following browsers:

##### 

Google Chrome   -->  v8 Engine

Mozilla Firefox -->  SpiderMonkey

Apple Safari    -->  JavaScriptCore





##### Q8. What is Dynamic Typing in JavaScript?



=> It means you do not need to declare the data type of a variable; JavaScript automatically identifies the type while the program is running.





##### Q9. What is the main difference between a static website and a dynamic website?



=>  can make website through 'HTML' and 'CSS' but it will be just a static website. In another word we are making a structure of car through HTML and designing through CSS. For making the car work we need engines and this is were JavaScript is valuable it adds logic in the static website and a dynamic website can be made by HTML, CSS \& JS.We





##### Q10. Name the three pillars of Front-end Web Development and write one line about each.



=> The Three pillars of Front-end Web Development are HTML, CSS \& JavaScript. 

HTML :- Its used to make the structure of wwe





##### Q11. What is the difference between Frontend and Backend?



=> 



Points	Fronted (Client-side)	Backend (Server-side)

• Runs on	• User's browser	•  Remote server

• Main technologies	• HTML, CSS, JS	• Node.js, Express.js, databases

• Responsibility	•What the user sees and interacts with 	• Business logic, data storage, security







##### Q12. What is Node.js?



=> Node.js is a runtime environment for JS that allows JS to run outside the browser. With Node.js, developers can create servers using JS, so JS can also be used for backend web development.





##### Q13. Explain ECMAScript. What is its relation with JavaScript?



=> ECMAScript is not a programming language like JS. It is a standard or rulebook that defines how the JS language should work. JS is a programming language that follows the ECMAScript standard. JS engines use this standard to understand and execute JS code. 

&#x20;





\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#### 

#### 

#### Section B: True or False (Write True or False. If False, correct the statement)







##### • JavaScript is a statically typed language.   



=> False (JavaScript is a dynamically typed language.)





##### • JavaScript can only run inside the browser.



=> False (JS can run outside the browser using Node.js.)





##### • HTML is responsible for the behaviour of a webpage.



=> False (JS is responsible for behaviour; HTML creates structure.)





##### • Node.js allows JavaScript to run outside the browser.



=> True





##### • JavaScript is case-insensitive.



=> False (JS is case-sensitive.)





##### • let name and let Name are the same variable.



=> False  (They are different variables becoz JS is case-sensitive.)





##### • ECMAScript is a programming language.



=> False  (ECMAScript is a standard, not a programming language.)





##### • React, Angular, and Vue.js are used for Backend development.



=> False  (They are used for front-end development.)









\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#### Section C: Fill in the Blanks









1. JavaScript was created by '**Brenden** **Eich**' in the year '**1995**'.


   ---
2. The three technologies used in Front-end development are '**HTML**, **CSS**, and **JavaScript**'.

   ---

###### 

###### 3\. JavaScript engines: Chrome uses '**V8** **Engine**', Firefox uses '**SpiderMonkey**'.

###### 

###### 

###### 4\. In the restaurant analogy: Customer = '**User**', Waiter = '**Server**', Chef = '**Database**'.

###### 

###### 

###### 5\. JavaScript file extension is '.js'.









\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------









#### Section D: Conceptual Questions (2 Marks each)









##### Q14. Differentiate between a static website and a dynamic website. Give one real-world example of each.



=> • Static Website: Displays fixed content that remains the same for every visitor. Example: A personal resume or portfolio page.



&#x20;  • Dynamic Website: Interactive, changes content based on user input or real-time data. Example: YouTube or Instagram.





##### Q15. Explain any two features of JavaScript that make it suitable for creating interactive web pages.



=> • Dynamic Typing: Automatically detects data types at runtime, making variable declaration flexible.



&#x20;  • Event-Driven: Can instantly respond to user actions such as click, keydown, or submit.







##### Q16. List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).



=> Backend: Node.js / Express.js



Mobile Apps: React Native



Desktop Apps: Electron



Games: Phaser / Three.js





##### Q17. What is the difference between writing JavaScript code:



###### &#x20;Inside an HTML file using <script> tag, and In an external .js file?

###### &#x20;Mention two advantages of using an external JavaScript file.





=> 1. Inline scripts are embedded directly inside HTML FILES, whiles external scripts are kept in separate ".js" files and linked via <script src="...">. 



&#x20;  2. Two advantages: 

&#x09;• Separation of concerns (Keeps HTML clean and readable).

&#x09;• Code reusability across multiple pages and better browser caching.





##### Q18. Explain the difference between Frontend and Backend using the restaurant analogy in your own words.



=> The Fronted is like the customer sitting at the table who views the menu and places an order on a screen. The Backend acts like the waiter who takes the order to the kitchen, where the chef (Database) prepares and stores the ingredients (data). 





##### Q19. Why should a beginner learn JavaScript? Write at least 4 points.



=> • It makes static websites interactive and alive.



&#x20;  • It works across both client-side (browsers) and server-side (Node.js).



&#x20;  • Beginners can instantly test and see results directly in the browser console.



&#x20;  • It features a massive global developer community with abundant learning resources.













\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------















#### Section E: Code-Based Questions (3 Marks each)







##### 

##### Q20. Predict the output of the following code and explain why:

##### 

###### let value = 25;

###### console.log(typeof value);

###### value = "JavaScript";

###### console.log(typeof value);

###### value = false;

###### console.log(typeof value);





=>  number



&#x20;   string	



&#x20;   boolean





**Explanation**: JavaScript is dynamically typed, meaning the type of a variable is determined at runtime based on its current value*.*







##### Q21. Write a simple HTML + JavaScript program that displays an alert box with the message "Welcome to JavaScript!" when a button is clicked.



=> <!DOCTYPE html>

<html>

<head>

&#x20; <title>Alert Box</title>

</head>

<body>

&#x20; <button onclick="alert('Welcome to JavaScript!')">Click Me</button>

</body>

</html>





##### 

##### Q22. Write JavaScript code to demonstrate event-driven programming.

##### When a user clicks a button with id "myBtn", the text of a paragraph with id "demo" should change to "Button was clicked!".





=>  <p id="demo">Original Text</p>

<button id="myBtn">Click Me</button>



<script>

&#x20; const btn = document.getElementById("myBtn");

&#x20; const demoText = document.getElementById("demo");



&#x20; btn.addEventListener("click", function() {

&#x20;   demoText.textContent = "Button was clicked!";

&#x20; });

</script>









\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#### 

#### 

#### Section F: Practical / Application Based (5 Marks)













##### Q23. Create a complete web page (HTML + JavaScript) that includes the following:



###### A heading: "My First JavaScript Page"

###### A button labeled "Click Me"

###### When the button is clicked:

###### Show an alert: "Hello, B.Tech Student!"

###### Change the background color of the page to light blue

###### Also print "JavaScript is running successfully!" in the browser console.

###### Write the complete code (you can use Inline or External JavaScript).







=>  <!DOCTYPE html>

<html lang="en">

<head>

&#x20; <meta charset="UTF-8">

&#x20; <title>My First JavaScript Page</title>

</head>

<body>



&#x20; <h1>My First JavaScript Page</h1>

&#x20; <button id="clickBtn">Click Me</button>



&#x20; <script>

&#x20;   // Print message to the browser console

&#x20;   console.log("JavaScript is running successfully!");



&#x20;   // Add event listener to the button

&#x20;   const button = document.getElementById("clickBtn");

&#x20;   button.addEventListener("click", function() {

&#x20;     alert("Hello, B.Tech Student!");

&#x20;     document.body.style.backgroundColor = "lightblue";

&#x20;   });

&#x20; </script>



</body>

</html>







\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#### 

#### Section G: Higher Order Thinking (Bonus - 3 Marks)







##### Q24. JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML. In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of Node.js and ECMAScript updates in this growth.





*=>  JavaScript achieved universal adoption because it was built directly into every modern web browser. Its growth into a multipurpose language was heavily propelled by Node.js, which liberated JavaScript from the browser and allowed developers to build server-side applications using the exact same language. Furthermore, regular ECMAScript updates (such as ES6 features like let, const, arrow functions, and classes) modernized the syntax, empowering developers to build scalable enterprise apps, mobile applications via React Native, and desktop software via Electron.*

