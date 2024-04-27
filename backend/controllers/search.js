const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Construct an absolute path using path.join()
const parent=path.resolve(__dirname, '../../')
const absoluteFilePath = path.join(parent, 'product_sample.db');
// Create a database connection
const db = new sqlite3.Database(absoluteFilePath);

function search(req, res)
 {
    
    
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