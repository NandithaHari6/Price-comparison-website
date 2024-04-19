const express = require('express');
const sqlite3 = require('sqlite3').verbose();
// const { spawn}=require('child_process');
const searchFunction=require('./runPy.js')
const app = express();
const port = 3000;
app.use(express.json());
// Connect to SQLite database
const db = new sqlite3.Database('../product_sample.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the database.');
});
app.get('/search',(req, res) => {
searchFunction(req.body.search);
res.send({"msg":"success"})});
// app.get('/search', (req, res) => {
//   const pythonArgs = req.body.search;
// const childPy=spawn('python',['../webscraper.py',...pythonArgs]);
// childPy.stdout.on('data',(data)=>{
//     console.log(`${data}`);
// })
// childPy.stderr.on('data',(data)=>{console.log(data);});
// childPy.on('close',()=>{console.log('Closed');});
// res.json({"message":"sucess"});
// })
// Define a route to read data from the database
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