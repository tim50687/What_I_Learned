## Backend Setup - Flexfolio Group Fitness Tracker

### **1. Project Initialization & Directory Setup**

1. **Create Project Directory:**
   - Open the terminal.
   - Navigate to the desired location.
   - Run:
     ```bash
     mkdir Flexfolio && cd Flexfolio
     ```

2. **Initialize Node.js Project:**
   - Run:
     ```bash
     npm init -y
     ```
   - This creates a `package.json` file.

3. **Install Development Dependencies:**
   - Install Nodemon for automatic server reloading:
     ```bash
     npm i --save-dev nodemon
     ```

### **2. Backend Development with Express.js**

1. **Install Express:**
   - Run:
     ```bash
     npm install express
     ```

2. **Create Express Server:**
   - Create `server.js`.
   - Add the basic Express server setup:
     ```javascript
     const express = require('express');
     const app = express();
     const PORT = 3000;

     app.get('/', (req, res) => res.send('Hello, Flexfolio!'));

     app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
     ```

3. **Run the Server:**
   - Use Nodemon to start the server:
     ```bash
     npm run devStart
     ```

### **3. Database Connection with MySQL**

1. **Install Sequelize and MySQL Driver:**
   - Run:
     ```bash
     npm install sequelize mysql2
     ```

2. **Initialize Sequelize:**
   - Run:
     ```bash
     npx sequelize-cli init
     ```

3. **Configure Database Credentials:**
   - Create a `.env` file.
   - Install dotenv for environment variable management:
     ```bash
     npm install dotenv
     ```
   - Add database credentials to `.env`:
     ```plaintext
     DB_HOST='localhost'
     DB_USERNAME='root'
     DB_PASSWORD='your_password'
     DB_DATABASE='flexfolio'
     ```

4. **Database Connection Test:**
   - Modify `server.js` to include Sequelize connection:
     ```javascript
     // Additional code for Sequelize database connection
     const { Sequelize } = require('sequelize');
     const sequelize = new Sequelize(process.env.DB_DATABASE, process.env.DB_USERNAME, process.env.DB_PASSWORD, {
       host: process.env.DB_HOST,
       dialect: 'mysql',
     });

     sequelize.authenticate()
       .then(() => console.log('Database connected...'))
       .catch(err => console.log('Error: ' + err));
     ```

5. **Run Your Server:**
   - Test the connection:
     ```bash
     npm run devStart
     ```

### **4. Further Development**

- **Routes & Controllers:** Set up Express routes and controllers for user registration, login, etc.

- **Middleware & Authentication:** Implement middleware for authentication using bcrypt for password hashing and JWT for token-based authentication.

- **Image Upload & Storage:** Decide on a storage solution (like AWS S3) for image uploading.

- **Frontend Development:** Start developing the React frontend and integrating it with the backend API.

- **Testing:** Regularly test routes and functionalities for reliability.

- **Deployment:** Plan for deploying the application to a hosting platform once completed.

- **Documentation & Presentation:** Prepare comprehensive documentation and a presentation to showcase your application.

