const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Construct an absolute path using path.join()
const parent=path.resolve(__dirname, '../../')
const absoluteFilePath = path.join(parent, 'product_sample.db');
// Create a database connection
const db = new sqlite3.Database(absoluteFilePath);

// Create user table if not exists
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT,
    phoneNo INTEGER,
    name TEXT
)`);

// User model object
const UserModel = {};

// Function to create a new user
UserModel.createUser = function(email, password,phoneNo,name, callback) {

    db.run('INSERT INTO users (email, password,phoneNo,name) VALUES (?, ?,?,?)', [email, password, phoneNo, name], function(err) {
        if (err) {
            return callback(err);
        }
        callback(null, this.lastID); // Return the ID of the newly inserted user
    });
};

// Function to find a user by email
UserModel.findByEmail = function(email, callback) {
    db.get('SELECT * FROM users WHERE email = ?', [email], function(err, row) {
        if (err) {
            return callback(err);
        }
        callback(null, row); // Return user object
    });

};

// Close the database connection
UserModel.closeConnection = function() {
    db.close();
};

// Export the UserModel object
module.exports = UserModel;