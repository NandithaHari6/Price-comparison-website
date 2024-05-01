import React, { useState, useEffect } from 'react';

function ProductPage({ isLoggedIn }) {
  const [searchWord, setSearchWord] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (searchResults.length > 0) {
      setLoading(false); // Set loading to false once search results are available
    }
  }, [searchResults]);

  const handleSearch = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchWord }),
      });
      const data = await response.json();
      setSearchResults(data);
      console.log(searchResults);
    } catch (error) {
      console.error(error);
    }
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
    <div>
      <h2>Product Page</h2>
      <div>
        <input type="text" value={searchWord} onChange={(e) => setSearchWord(e.target.value)} />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div>
        {loading ? (
          <p>Loading...</p>
        ) : (
          searchResults.map((product) => (
            <div key={product.productId}>
              <h3>{product.title}</h3>
              {product.image && <img src={product.image} alt="Product" />}
              {product.a_link && <a href={product.a_link}>Amazon</a>}
              {product.a_price && <p>Amazon Price: {product.a_price}</p>}
              {product.f_link && <a href={product.f_link}>Flipkart</a>}
              {product.f_price && <p>Flipkart Price: {product.f_price}</p>}
              {product.c_link && <a href={product.c_link}>Croma</a>}
              {product.c_price && <p>Croma Price: {product.c_price}</p>}
              {isLoggedIn && (
                <button onClick={() => handleAddToWishlist(product.ProductId, product.targetPrice)}>
                  Add to Wishlist
                </button>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default ProductPage;
