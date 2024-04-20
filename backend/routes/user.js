const express = require('express')
const router = express.Router()
const {signup}=require('../controllers/userLogin')
const {login}=require('../controllers/userLogin')
const {addToWishlist}=require('../controllers/addToWishlist')
const {verifyToken}=require('../controllers/authMiddleware')
// define the home page route
router.post('/signup',signup)
router.post('/login',login )
router.post('/addToWishlist',verifyToken,addToWishlist)
// router.get('/displayWishlist',displayWishlist)
// router.get('/logout',logout )

module.exports = router