const jwt = require('jsonwebtoken');
function verifyToken(req, res, next) {
const token = req.header('Authorization');
if (!token) return res.status(401).json({ error: 'Access denied' });
try {
 const decoded = jwt.verify(token, 'your-secret-key');
 req.body.email = decoded.email;

 next();
 } catch (error) {
 res.status(401).json({ error: 'Invalid token' });
 }
 };

module.exports = {verifyToken};