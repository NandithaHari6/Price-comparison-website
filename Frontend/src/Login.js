import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css'; // Import the CSS file

function Login({ isLoggedIn, setIsLoggedIn }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSignUp = () => {
    navigate('/signup');
  };

  const handleLogin = async () => {
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    });

    if (response.ok) {
      const data = await response.json();
      const accessToken = data.access_token;
      localStorage.setItem('accessToken', accessToken);
      setIsLoggedIn(true);
    } else {
      console.error('Login failed');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    setIsLoggedIn(false);
  };

  return (
    <div className="container">
      {isLoggedIn ? (
        <div className="login-form">
          <p>Welcome! You are logged in.</p>
          <button onClick={handleLogout} className="logout-button">Logout</button>

        </div>
      ) : (
        <div className="login-form">
          <input
            type="email"
            placeholder="Email"
            className="input-field"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            className="input-field"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <div className="button-group">
          <button onClick={handleLogin} className="login-button">Login</button>

            <button onClick={handleSignUp}>Sign Up</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Login;
