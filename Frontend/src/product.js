import React, { useState, useEffect } from 'react';
import './product.css';

function ProductPage({ isLoggedIn, searchWord, searchResults, setSearchResults }) {

  const [loading, setLoading] = useState(true);
  const [showPopup, setShowPopup] = useState(0);
  const [targetPrice, setTargetPrice] = useState('');
  const accessToken = localStorage.getItem('accessToken');
 
  useEffect(() => {

    if (searchResults.length > 0) {
      setLoading(false); // Set loading to false once search results are available
    }
  }, [searchResults]);

 const handlePopupClose = () => {
    setShowPopup(0);
    setTargetPrice('');
  };

  const handleAddClick = (productId) => {
    setShowPopup(productId);
  };

  const handleAddToWishlistClick = (productId) => {
    handleAddToWishlist(productId, targetPrice);
    setShowPopup(0);
    setTargetPrice('');
  };
  const handleAddToWishlist = async (productId, targetPrice) => {
    if (!isLoggedIn) {
      return;
    }
    try {
      const response = await fetch('http://127.0.0.1:8000/add_to_wishlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify({ productId, targetPrice }),
      });
      const data = await response.json();
      console.log(data);
      // Show success message or handle response accordingly
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="product_type">
      <h2>Product Page</h2>

      <div className="container">
        {loading ? (
          <p>Loading...</p>
        ) : (
          searchResults.map((product) => (
            <div className="box" key={product.productId}>
              <div className="img_box">
                {product.image && <img src={product.image} alt="Product" />}
              </div>
              <div className="detail">
                <h3>{product.title}</h3>
                {product.a_link && <a href={product.a_link} target="_blank">Amazon</a>}
                {product.a_price && <p>Amazon Price: {product.a_price}</p>}
                {product.f_link && <a href={product.f_link} target="_blank">Flipkart</a>}
                {product.f_price && <p>Flipkart Price: {product.f_price}</p>}
                {product.c_link && <a href={product.c_link} target="_blank">Croma</a>}
                {product.c_price && <p>Croma Price: {product.c_price}</p>}
                {isLoggedIn && (
        <div>
          <button onClick={()=>{
            handleAddClick(product.productId)}}>Add to Wishlist</button>
          {showPopup === product.productId && (
            <div className="popup">
              <div className="popup-content">
                <span className="close" onClick={handlePopupClose}>&times;</span>
                <h2>Enter Target Price</h2>
                <input type="number" value={targetPrice} onChange={(e) => setTargetPrice(e.target.value)} />
                <button onClick={()=>{
                  handleAddToWishlistClick(product.productId)
                }
                  }>Add to Wishlist</button>
              </div>
            </div>
          )}
        </div>
      )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );

}

export default ProductPage;