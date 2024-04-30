import React, { useState } from 'react';
import axios from 'axios';

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    phoneNo: '',
    email: '',
    password: ''
  });
  const [error, setError] = useState('');

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
      const response = await axios.post('http://127.0.0.1:8000/signup', formData);
      console.log(response.data);
      // Redirect user or show success message
    } catch (error) {
      console.error(error);
      // Handle error response
    }
  };

  const validateEmail = (email) => {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="phoneNo">Phone Number:</label>
          <input type="text" id="phoneNo" name="phoneNo" value={formData.phoneNo} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} required />
        </div>
        {error && <div style={{ color: 'red' }}>{error}</div>}
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}

export default Signup;