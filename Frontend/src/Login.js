import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
function Login({isLoggedIn,setIsLoggedIn}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate()


  const handleSignUp = () => {
    navigate('/signup')

  };

  const handleLogin = async () => {
    // Send POST request to /login endpoint
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    });

    // Check if request was successful
    if (response.ok) {
      // Extract access token from response
      const data = await response.json();
      const accessToken = data.access_token;

      // Save access token to local storage
      localStorage.setItem('accessToken', accessToken);

      // Set isLoggedIn state to true
      setIsLoggedIn(true);
    } else {
      // Handle login error
      console.error('Login failed');
    }
  };
  const handleLogout = () => {
    // Remove access token from local storage
    localStorage.removeItem('accessToken');
    
    // Set isLoggedIn state to false
    setIsLoggedIn(false);
  };
  return (
    <div>
      {isLoggedIn ? (
        <div>
          <p>Welcome! You are logged in.</p>
          <button onClick={handleLogout}>Logout</button>
          {/* Add logout button here */}
        </div>
      ) : (
        <div>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
          <button onClick={handleSignUp}>Sign Up</button>
        </div>
      )}
    </div>
  );
}

export default Login;
