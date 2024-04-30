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
>>>>>>> f91a40051ec59b2a316e30bb5cc360219aa72ad6

function search(req, res)
 {
    
<<<<<<< HEAD
=======
const db = new sqlite3.Database(absoluteFilePath);

function search(req, res)
 {
>>>>>>> 8b132d3833515654f3add6f915851c4a778d5480
    
=======
>>>>>>> f91a40051ec59b2a316e30bb5cc360219aa72ad6
    
    const sql = 'SELECT * FROM grouping1'; // Modify 'your_table' to your actual table name
  
    db.all(sql, [], (err, rows) => {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.json(rows);
    });
  }
  module.exports={search}