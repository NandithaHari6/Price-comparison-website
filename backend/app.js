const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router=require('./routes/user.js')
<<<<<<< HEAD

=======
const cors = require('cors');
>>>>>>> 8b132d3833515654f3add6f915851c4a778d5480
const app = express();
const port = 4000;
app.use(cors());
app.use(express.json());
<<<<<<< HEAD
// Connect to SQLite database
const db = new sqlite3.Database('C:\Users\Rinu Joseph\Price-comparison-website\product_sample.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the database.');
});
=======


>>>>>>> 8b132d3833515654f3add6f915851c4a778d5480
app.use('/user',router);


app.get('/data', (req, res) => {
  const sql = 'SELECT * FROM amazon'; // Modify 'your_table' to your actual table name

  db.all(sql, [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});