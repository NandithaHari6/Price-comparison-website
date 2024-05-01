import React, { useState, useEffect } from 'react';
import './product.css';

function ProductPage({ isLoggedIn, searchWord, searchResults, setSearchResults }) {

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    if (searchResults.length > 0) {
      setLoading(false); // Set loading to false once search results are available
    }
  }, [searchResults]);


  const handleAddToWishlist = async (productId, targetPrice) => {
    if (!isLoggedIn) {
      return;
    }
    try {
      const response = await fetch('http://127.0.0.1:8000/add_to_wishlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
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
                  <button onClick={() => handleAddToWishlist(product.productId, product.targetPrice)}>
                    Add to Wishlist
                  </button>
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