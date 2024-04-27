const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const router=require('./routes/user.js')
const cors = require('cors');
const app = express();
const port = 4000;
app.use(cors());
app.use(express.json());


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