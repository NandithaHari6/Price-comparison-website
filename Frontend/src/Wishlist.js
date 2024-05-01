import React, { useState, useEffect } from 'react';
import './wishlist.css'
import { useNavigate } from 'react-router-dom';
function Wishlist() {
  const [wishlist, setWishlist] = useState([]);
  const accessToken = localStorage.getItem('accessToken');
  const navigate=useNavigate()
 const deleteWish=async(productId)=>{
  try {
    const response = await fetch('http://127.0.0.1:8000/delete_wishlist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`
      },
      body: JSON.stringify({ productId})
    });
    const data = await response.json();
      if (data.message === "Success") {
        navigate('/cart')
      } else {
        (<div> Cannot Delete </div>)
      }
    
  } catch (error) {
    console.error(error);
  }
 }
  useEffect(() => {
    const fetchWishlist = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/show_wishlist', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
          },
        });
        const data = await response.json();
        setWishlist(data);
      } catch (error) {
        console.error(error);
      }
    };

    if (accessToken) {
      fetchWishlist();
    } else {
      // Handle case when accessToken is not available
      console.error('Access token not available');
    }
  }, [accessToken,wishlist]);

  return (
    <div className="wishlist">
      <h1>Wishlist</h1>
      <ul>
        {wishlist.map(product => (
          <div className="product">
          <li key={product.productId}>
            <img src={product.image} alt={product.title} />
            <h3>{product.title}</h3>
            <p>Target Price: {product.targetPrice}</p>
            
              {product.a_link && <a href={product.a_link} target="_blank">Amazon</a>}
              {product.a_price && <p>Amazon Price: {product.a_price}</p>}
              {product.f_link && <a href={product.f_link} target="_blank">Flipkart</a>}
              {product.f_price && <p>Flipkart Price: {product.f_price}</p>}
              {product.c_link && <a href={product.c_link} target="_blank">Croma</a>}
              {product.c_price && <p>Croma Price: {product.c_price}</p>}
              <button onClick={()=>{deleteWish(product.productId)}}> Delete from WishList</button>
          </li>
          </div> ))}
      </ul>
    </div>
  );
}

export default Wishlist;
