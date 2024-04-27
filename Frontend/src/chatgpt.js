import React, { useState } from 'react';

const SignUpForm = () => {
  const [phoneNo, setPhoneNo] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:4000/user/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ phoneNo, name, email, password }),
      });
      const data = await response.json();
      console.log(data); // Handle successful signup response
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Phone Number" value={phoneNo} onChange={(e) => setPhoneNo(e.target.value)} />
      <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Sign Up</button>
    </form>
  );
};

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:4000/user/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      localStorage.setItem('token', data.token);
      localStorage.setItem('email', email);
      console.log(data); // Handle successful login response
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Login</button>
    </form>
  );
};

const AddToWishlist = () => {
  const token = localStorage.getItem('token');
  const email = localStorage.getItem('email');
  const targetPrice=5000;
  const productId=103;
  const handleAddToWishlist = async () => {
    try {
      const response = await fetch('http://localhost:4000/user/addToWishlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': ` ${token}`,
        },
        body: JSON.stringify({ email,targetPrice,productId }),
      });
      const data = await response.json();
      console.log(data); // Handle successful add to wishlist response
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <button onClick={handleAddToWishlist}>Add to Wishlist</button>
  );
};

const App = () => {
  return (
    <div>
      <h2>Sign Up</h2>
      <SignUpForm />
      <h2>Login</h2>
      <LoginForm />
      <h2>Add to Wishlist</h2>
      <AddToWishlist />
    </div>
  );
};

export default App;