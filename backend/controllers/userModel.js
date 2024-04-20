const sqlite3 = require('sqlite3').verbose();

// Create a database connection
const db = new sqlite3.Database('../../product_sample1.db');

// Create user table if not exists
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)`);

// User model object
const UserModel = {};

// Function to create a new user
UserModel.createUser = function(email, password, callback) {

    db.run('INSERT INTO users (email, password) VALUES (?, ?)', [email, password], function(err) {
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