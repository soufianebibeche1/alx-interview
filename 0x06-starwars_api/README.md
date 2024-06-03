# 0x06. Star Wars API

## Overview
This project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. The goal is to demonstrate the ability to work with external APIs and manage asynchronous code in JavaScript.

## Concepts Needed
To complete this project, you need to be familiar with the following concepts:

1. **HTTP Requests in JavaScript**
   - Making HTTP requests to external services using modules like `request` or `fetch` in Node.js.
   - [A Complete Guide to Making HTTP Requests in Node.js](https://www.digitalocean.com/community/tutorials/how-to-make-http-requests-in-node-js)

2. **Working with APIs**
   - Understanding RESTful APIs and how to interact with them.
   - Parsing JSON data returned by APIs.
   - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

3. **Asynchronous Programming**
   - Managing asynchronous operations with callbacks, promises, and async/await syntax.
   - Handling API response data asynchronously.
   - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

4. **Command Line Arguments in Node.js**
   - Using `process.argv` array to access command-line arguments passed to a Node.js script.
   - [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/en/learn/nodejs-command-line-arguments/)

5. **Array Manipulation and Iteration**
   - Iterating over arrays and manipulating data structures to format and display character names.
   - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Requirements
- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/node`
  - A `README.md` file at the root of the project folder is mandatory
  - Code should be semistandard compliant (Standard + semicolons on top, also reference AirBnB style)
  - All files must be executable
  - The length of files will be tested using `wc`
  - Usage of `var` is not allowed; use `let` or `const` instead

## Project Instructions
1. **Fetch Data from Star Wars API**
   - Make an HTTP request to the Star Wars API to fetch information about characters.
   - Base the fetch on the movie ID provided as a command-line argument.

2. **Process and Display Data**
   - Parse the JSON response from the API.
   - Extract and display the names of characters from the specified movie.

3. **Handle Asynchronous Operations**
   - Use callbacks, promises, or async/await to manage asynchronous API requests.
   - Ensure that data is correctly handled and displayed after the API call completes.

4. **Command Line Arguments**
   - Access the movie ID from the command-line arguments using `process.argv`.

5. **Array Manipulation**
   - Iterate over the array of character URLs returned by the API.
   - Make additional API requests to fetch each character's name.
   - Display the names in the correct order.

## Additional Resources
- [Mock Technical Interview](https://www.pramp.com/)
  
## Example Usage
