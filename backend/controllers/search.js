const sqlite3 = require('sqlite3').verbose();

// Create a database connection
const db = new sqlite3.Database('../../product_sample1.db');
const searchFunction=require('../runPy')
function search(req, res)
 {
    searchFunction(req.body.search)
    
    // const sql = 'SELECT * FROM grouping'; // Modify 'your_table' to your actual table name
  
    // db.all(sql, [], (err, rows) => {
    //   if (err) {
    //     res.status(500).json({ error: err.message });
    //     return;
    //   }
    //   res.json(rows);
    // });
  }
  module.exports={search}