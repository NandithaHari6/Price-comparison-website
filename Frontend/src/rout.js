import React from 'react'
import { Routes, Route} from 'react-router-dom'
import Home from './home'
import Cart from './cart'
import Product from './product'
import Login from './Login'
import Contact from './contact'

const Rout = ({isLoggedIn,setIsLoggedIn , detail, view, close, setClose, cart, setCart, addtocart}) => {
  return (
    <>
    <Routes>
        <Route path='/' element={<Home detail={detail} view={view} close={close} setClose={setClose} addtocart={addtocart}/>}/>
        {/* <Route path='/product' element={<Product product={product} setProduct={setProduct} detail={detail} view={view} close={close} setClose={setClose} addtocart={addtocart}/>} /> */}
        <Route path='/product' element={<Product isLoggedIn={isLoggedIn}/>} />
        <Route path='/cart' element={<Cart cart={cart} setCart={setCart} />} />
        <Route path='/contact' element={<Contact />} />
        <Route path='/login' element={<Login isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/>} />

    </Routes>
    </>
  )
}

export default Rout