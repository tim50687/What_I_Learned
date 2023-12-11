### Backend Setup for Flexfolio Group Fitness Tracker

#### 1. MySQL Connection Pool Setup in Server.js

**server.js Example:**
```javascript
const express = require('express');
const mysql = require('mysql2');
const dotenv = require('dotenv');
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Connection pool setup
const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USERNAME,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE
});

// Convert pool to use promises for async/await
const promisePool = pool.promise();

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

// Additional configurations...
```

#### 2. Dependency Injection of Pool into Routes and Controllers

**In userRoutes.js:**
```javascript
const express = require('express');
const userController = require('../controllers/userController');

module.exports = (pool) => {
    const router = express.Router();
    const userCtrl = userController(pool);
    router.post('/register', userCtrl.registerUser);
    return router;
};
```

**In userController.js:**
```javascript
module.exports = (pool) => {
    return {
        registerUser: async (req, res) => {
            // Database interaction using pool
            // ...
        }
        // Other methods...
    };
};
```

**Implementing in server.js:**
```javascript
const userRoutes = require('./routes/userRoutes')(promisePool);
app.use('/api/users', userRoutes);
```

### Summary
- Create a database connection pool in the main server file.
- Pass the pool to the routes and controllers.
- This approach ensures efficient and centralized database interaction.

## JWT Implementation

JWT is typically used after user login for authenticating subsequent requests. The server generates a JWT upon successful login, which the client then includes in the `Authorization` header for accessing protected routes.

### Middleware for JWT Authentication

To create `authenticateToken` middleware in Express:
```javascript
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if (!token) return res.sendStatus(401);

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};
```
This middleware validates the JWT and allows access to protected routes if the token is valid.

## S3 Image Upload from Node.js Backend

1. Install Multer for handling file uploads:
   ```bash
   npm install --save multer
   ```

2. Configure AWS S3 and Multer in your backend:
   ```javascript
   const AWS = require('aws-sdk');
   const multer = require('multer');
   const multerS3 = require('multer-s3');

   AWS.config.update({
       accessKeyId: process.env.AWS_ACCESS_KEY_ID,
       secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
       region: process.env.AWS_REGION
   });

   const s3 = new AWS.S3();

   const upload = multer({
       storage: multerS3({
           s3: s3,
           bucket: process.env.AWS_BUCKET_NAME,
           acl: 'public-read',
           key: function (req, file, cb) {
               cb(null, file.originalname); // Use file name as key
           }
       })
   });
   ```

3. API endpoint for image upload:
   ```javascript
   app.post("/upload", upload.single("image"), (req, res) => {
       res.json({ imageUrl: req.file.location });
   });
   ```

### Deleting a Post in UI

To implement post deletion:
1. Attach a delete button to each post with the post ID.
2. Use JavaScript to send a DELETE request to the backend.
3. Update the UI upon successful deletion.

Example Delete Function:
```javascript
function deletePost(postId) {
    if (confirm('Are you sure you want to delete this post?')) {
        fetch(`/api/posts/${postId}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Remove post from UI or refresh list
                }
            });
    }
}
```

### Backend Delete Endpoint

1. Create a route for deleting posts in your Express application.
2. Implement controller logic to handle the deletion in the database.

```javascript
app.delete('/api/posts/:postId', (req, res) => {
    const postId = req.params.postId;
    // Delete logic...
});
```

### Summary

- Implement JWT for secure API access after login.
- Set up image upload to AWS S3 using Multer.
- Provide frontend functionality for deleting posts and reflect changes in the UI.