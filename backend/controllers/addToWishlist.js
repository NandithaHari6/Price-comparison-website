const sqlite3 = require('sqlite3').verbose();

// Create a database connection
const db = new sqlite3.Database('C:\Users\Rinu Joseph\Price-comparison-website\product_sample.db');

// Create WishlistProduct table
db.run(`CREATE TABLE IF NOT EXISTS WishlistProduct (
    productId INTEGER PRIMARY KEY,
    amazonLink TEXT,
    flipkartLink TEXT,
    cromaLink TEXT,
    amazonPrice REAL,
    flipkartPrice REAL,
    cromaPrice REAL,
    title TEXT,
    image TEXT
)`);

// Create WishlistEntry table
db.run(`CREATE TABLE IF NOT EXISTS WishlistEntry (
    email TEXT,
    productId INTEGER,
    targetPrice REAL,
    FOREIGN KEY (productId) REFERENCES WishlistProduct(productId)
)`);

// Function to add a product to the wishlist
function addToWishlist(req,res) {
    // Check if the product already exists in any of the three columns
    // db.get(`SELECT productId FROM WishlistProduct WHERE productId = ? OR amazonLink = ? OR flipkartLink = ? OR cromaLink = ?`, 
    //     [productId, productId, productId, productId], 
    //     function(err, row) {
    //         if (err) {
    //             console.error('Error checking product:', err);
    //             return;
    //         }
            // if (!row) { // Product does not exist, insert it
            //     db.run(`INSERT INTO WishlistProduct (productId) VALUES (?)`, [productId], function(err) {
            //         if (err) {
            //             console.error('Error adding product:', err);
            //             return;
            //         }
            //         console.log('Product added to WishlistProduct table with ID:', productId);
            //     });
            // }
            // Insert into WishlistEntry table
            email=req.body.email;
            productId=req.body.productId;
            targetPrice=req.body.targetPrice;

            db.run(`INSERT INTO WishlistEntry (email, productId, targetPrice) VALUES (?, ?, ?)`, 
                [email, productId, targetPrice], 
                function(err) {
                    if (err) {
                        console.error('Error adding entry to WishlistEntry:', err);
                        return;
                    }
                    console.log('Product added to WishlistEntry table for email:', email);
                    res.send("sucess")
                });

            }


// Example usage:

// Close the database connection
process.on('exit', () => db.close()); // Ensure database connection is closed when the script exits
module.exports={ addToWishlist}