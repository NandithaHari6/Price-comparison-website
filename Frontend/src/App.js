import React ,{useState}from "react";
import Nav from "./nav";
import Rout from "./rout";
import { BrowserRouter  } from "react-router-dom";
import Footer from './footer';
import './App.css';

import Productdetail from './productdetail';

const App = () => {
  // add to cart
  const [cart, setCart] = useState([])
  //product 
  const [searchResults, setSearchResults] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [close, setClose] = useState(false)
  const [detail, setDetail] = useState([])
  const [searchWord, setSearchWord] = useState('');
  const [product, setProduct] = useState(Productdetail)
  const searchbtn = (product) => 
  {
    const change = Productdetail.filter((x) => 
    {
      return x.Cat === product
    })
    setProduct(change)
  }
  //product detail
  const view = (product) => 
  {
    setDetail([{...product}])
    setClose(true)
  }

  // add to cart
  const addtocart = (product) => 
  {
    const exsit = cart.find((x) => 
    {
      return x.id === product.id
    })
    if(exsit)
    {
      alert("This Product is already added to cart")
    }
    else
    { 
      setCart([...cart, {...product, qty:1}])
      alert("product is added to cart")
    }
  } 
  console.log(cart)
  return (
    <>
    
    <BrowserRouter>
    <Nav searchbtn={searchbtn} setSearchResults = {setSearchResults} isLoggedIn={isLoggedIn} searchWord={searchWord} setSearchWord={setSearchWord} />
    <Rout product={product} setProduct={setProduct} detail={detail} view={view} searchWord={searchWord} close={close} setClose={setClose} cart={cart} setCart={setCart} addtocart={addtocart} 
    isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} searchResults ={searchResults} setSearchResults = {setSearchResults} />
    <Footer />
    </BrowserRouter>
    </>
  )
}

export default App