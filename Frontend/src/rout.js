import React from 'react'
import { Routes, Route} from 'react-router-dom'
import Home from './home'
import Wishlist from './Wishlist'
import Product from './product'
import Login from './Login'
import Contact from './contact'
import Signup from './Signup'
const Rout = ({isLoggedIn,setIsLoggedIn , detail, view, searchWord,close, setClose, cart, setCart, addtocart,searchResults,setSearchResults }) => {
  return (
    <>
    <Routes>
        <Route path='/' element={<Home detail={detail} view={view} close={close} setClose={setClose} addtocart={addtocart} />}/>
        {/* <Route path='/product' element={<Product product={product} setProduct={setProduct} detail={detail} view={view} close={close} setClose={setClose} addtocart={addtocart}/>} /> */}
        <Route path='/product' element={<Product isLoggedIn={isLoggedIn}searchResults ={searchResults} setSearchResults = {setSearchResults}searchWord={searchWord}/>} />
        <Route path='/cart' element={<Wishlist />} />
        <Route path='/contact' element={<Contact />} />
        <Route path='/login' element={<Login isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/>} />
        <Route path='/signup' element={<Signup/>} />

    </Routes>
    </>
  )
}

export default Rout