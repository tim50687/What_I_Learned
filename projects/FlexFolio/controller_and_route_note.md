# Express.js: Routes, Controllers, and HTTP Methods

## Express.js and Web Development

Express.js is a Node.js framework widely used for developing web applications and APIs. It simplifies the server creation process in Node.js, offering robust features for routing, middleware integration, and more. Understanding its core components like routes, controllers, and HTTP methods is vital for efficient web development.

## Routes in Express.js

- **Definition**: Routes in Express.js define how the server responds to client requests at specific endpoints, identified by URIs and HTTP methods.
- **Example**:
  ```javascript
  app.get('/users', (req, res) => res.send('Retrieve users'));
  app.post('/users', (req, res) => res.send('Create user'));
  ```
  Here, `app.get` and `app.post` define routes for retrieving and creating users, respectively.

## Controllers in Express.js

- **Definition**: Controllers handle the logic for processing requests and generating responses. They act as an intermediary between the model (data) and the view (presentation).
- **Example**: In `userController.js`, functions like `getAllUsers` and `addUser` manage the operations for respective routes.

## HTTP Methods and Their Usage

- **GET**: Fetches data. Idempotent, often used for retrieving resources.
- **POST**: Submits data for processing. Not idempotent, commonly used for creating resources.
- **PUT**: Updates existing resources or creates new ones if they don't exist. Idempotent.
- **DELETE**: Removes resources. Idempotent.
- **PATCH**: Partially updates resources. Not strictly idempotent.
- **HEAD**: Similar to GET but only retrieves headers.
- **OPTIONS**: Describes communication options for a resource.
- **CONNECT**: Establishes a tunnel to the server.
- **TRACE**: Performs a message loop-back test.

## Implementing Routes and Controllers in Express.js

### `routes/userRoutes.js`

```javascript
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

router.post('/register', userController.register);
router.post('/login', userController.login);

module.exports = router;
```

- **Router Creation**: `express.Router()` creates a new router instance.
- **Controller Import**: The `userController` module, containing functions for each route, is imported.
- **Route Definition**: Routes for user registration and login are defined, delegating the request handling to the respective controller functions.
- **Exporting Router**: The configured router is exported for use in the main server file.

### `controllers/userController.js`

```javascript
exports.register = async (req, res) => {
  // Registration logic
};

exports.login = async (req, res) => {
  // Login logic
};
```

- **Controller Functions**: Each function in `userController.js` corresponds to a route, handling the request and sending the response.

## Conclusion

In Express.js development, routes determine the server's response to different endpoints, while controllers handle the logic for these routes. Understanding HTTP methods is crucial for defining the actions performed by these routes. This structure promotes organized, maintainable, and efficient web development practices.