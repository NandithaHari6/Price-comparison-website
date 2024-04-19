import React, { useState } from "react";
import Nav from "./nav";
import Rout from "./rout";
import { BrowserRouter } from "react-router-dom";
import Footer from './footer';
import { useAuth0 } from "@auth0/auth0-react"; // Import useAuth0 hook
import './App.css';
import Productdetail from './productdetail';

const App = () => {
  // State for cart, product detail, and filter
  const [cart, setCart] = useState([]);
  const [close, setClose] = useState(false);
  const [detail, setDetail] = useState([]);
  const [product, setProduct] = useState(Productdetail);

  // Use useAuth0 hook to access authentication-related functions and state
  const { isAuthenticated, loginWithRedirect } = useAuth0();

  // Function to filter products
  const searchbtn = (product) => {
    const change = Productdetail.filter((x) => {
      return x.Cat === product;
    });
    setProduct(change);
  };

  // Function to view product details
  const view = (product) => {
    setDetail([{ ...product }]);
    setClose(true);
  };

  // Function to add product to cart
  const addtocart = (product) => {
    // Check if user is authenticated
    if (!isAuthenticated) {
      // If not authenticated, prompt user to sign in
      loginWithRedirect();
      return;
    }

    // Check if product is already in cart
    const exist = cart.find((x) => x.id === product.id);
    if (exist) {
      alert("This product is already added to cart");
    } else {
      setCart([...cart, { ...product, qty: 1 }]);
      alert("Product is added to cart");
    }
  };

  return (
    <>
      <BrowserRouter>
        <Nav searchbtn={searchbtn} />
        <Rout
          product={product}
          setProduct={setProduct}
          detail={detail}
          view={view}
          close={close}
          setClose={setClose}
          cart={cart}
          setCart={setCart}
          addtocart={addtocart}
        />
        <Footer />
      </BrowserRouter>
    </>
  );
};

export default App;
