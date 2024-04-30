const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Construct an absolute path using path.join()
const parent=path.resolve(__dirname, '../../')
const absoluteFilePath = path.join(parent, 'product_sample.db');
// Create a database connection
<<<<<<< HEAD
<<<<<<< HEAD
const db = new sqlite3.Database('C:\Users\Rinu Joseph\Price-comparison-website\product_sample.db');
=======
const db = new sqlite3.Database(absoluteFilePath);
>>>>>>> 8b132d3833515654f3add6f915851c4a778d5480
=======
const db = new sqlite3.Database(absoluteFilePath);
>>>>>>> f91a40051ec59b2a316e30bb5cc360219aa72ad6

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
db.run(`CREATE TABLE  IF NOT EXISTS WishlistEntry (
    email TEXT,
    productId INTEGER,
    targetPrice REAL,
    FOREIGN KEY (productId) REFERENCES WishlistProduct(productId)
)`);
 function callback(row,title,image,email,targetPrice,res){
    
    db.run(`insert into WishlistProduct(amazonLink,flipkartLink,cromaLink,amazonPrice,flipkartPrice,cromaPrice,title,image) values(?,?,?,?,?,?,?,?);`,[row.a_url||null,row.f_url,row.c_url,row.a_price,row.f_price,row.c_price,title,image],function(err) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(this.lastID);
        addToUser(this.lastID,email,targetPrice,res);
    
});

}
// Function to add a product to the wishlist
function addToWishlist(req,res) {

            a_link=req.body.a_link;
            f_link=req.body.f_link;
            c_link=req.body.c_link;
            email=req.body.email;
            productId=req.body.productId;
            targetPrice=req.body.targetPrice;

            if(f_link!=null){
                const sql = 'SELECT  *  FROM grouping1 WHERE f_url = ?';
                const params = [f_link];
                 db.get(sql, params, (err, row) => {
                        if (err) {
                            throw err;
                        }
                        title=row.f_title;
                        image=row.f_image;
                        callback(row,title,image,email,targetPrice,res);
                        });
                        
            }else if(a_link!=null){
                const sql = 'SELECT * FROM grouping1 WHERE a_url = ?';
                const params = [a_link];
                 db.get(sql, params, (err, row) => {
                        if (err) {
                            throw err;
                        }
                        title=row.a_title;
                        image=row.a_image;
                        callback(row,title,image,email,targetPrice,res);
                        });
            }else{
                
                const sql = 'SELECT * FROM grouping1 WHERE c_url = ?';
                const params = [c_link];
                 db.get(sql, params, (err, row) => {
                        if (err) {
                            throw err;
                        }
                        title=row.c_title;
                        image=row.c_image;
                        
                        callback(row,title,image,email,targetPrice,res);
                       
                        
                        });}
                        

            

            }

function addToUser(productId,email,targetPrice,res){
    db.run(`INSERT INTO WishlistEntry (email, productId, targetPrice) VALUES (?, ?, ?)`, 
                [email, productId, targetPrice], 
                function(err) {
                    if (err) {
                        console.error('Error adding entry to WishlistEntry:', err);
                        res.status(500).json({ error: 'cannot add to wishlist' });
                        return;
                    }
                    console.log('Product added to WishlistEntry table for email:', email);
                    res.status(201).json({ message: 'Added to WishList' });
                });
}
process.on('exit', () => db.close()); // Ensure database connection is closed when the script exits
module.exports={ addToWishlist}