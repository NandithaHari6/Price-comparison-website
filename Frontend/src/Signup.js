import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Signup.css'; // Import the CSS file

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    phoneNo: '',
    email: '',
    password: ''
  });
  const [error, setError] = useState('');

  const navigate = useNavigate();
  
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.phoneNo.length < 10 || !validateEmail(formData.email)) {
      setError('Phone number must be at least 10 digits and email must be valid.');
      return;
    }
    try {
      const response = await fetch('http://127.0.0.1:8000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        navigate('/login'); // Redirect to login page
      } else {
        const errorData = await response.json();
        setError(errorData.message); // Display error from server
      }
    } catch (error) {
      console.error(error);
      setError('Failed to sign up.'); // Handle network errors
    }
  };

  const validateEmail = (email) => {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  };

  return (
    <div className="container">
      <div className="signup-form">
        <h2>Sign Up</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-field">
            <input type="text" id="name" name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
          </div>
          <div className="input-field">
            <input type="text" id="phoneNo" name="phoneNo" placeholder="Phone Number" value={formData.phoneNo} onChange={handleChange} required />
          </div>
          <div className="input-field">
            <input type="email" id="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
          </div>
          <div className="input-field">
            <input type="password" id="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
          </div>
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <button type="submit">Sign Up</button>
        </form>
      </div>
    </div>
  );
}

export default Signup;
