import React, { useState ,useEffect} from 'react'
import { FaShoppingCart } from "react-icons/fa";
import { FaUser } from "react-icons/fa";

import { Link } from 'react-router-dom';

import Logo from "./img/logo.svg";
import { useNavigate } from 'react-router-dom';
import './nav.css'
import {handleSearch } from './handleSearch'

const Nav = ({logout,isLoggedIn,searchWord,setSearchWord,setSearchResults}) => {
    const navigate = useNavigate()
  
  return (
    <>
   
    <div className='main_header'>
        <div className='container'>
            <div className='logo'>
                <img src={Logo} alt='logo'></img>
            </div>
            <div className='search_box_nav'>
                <input type='text' value={searchWord} placeholder='Search Your Product...' autoComplete='off' onChange={(e) => setSearchWord(e.target.value)}></input>
                <button onClick={()=>{
                    handleSearch(searchWord,setSearchResults)
                    navigate('/product')
                }}>Search</button>
            </div>
            <div className='icon'>
                {
                    
                        <div className='account'>
                        <div className='user_icon' onClick={()=>{
                             navigate('/login')
                        }
                           }>
                            <FaUser />
                            
                        </div>
                        </div>
                    
                }
                {
                    isLoggedIn && (
                        <div className='second_icon'>


                            <button onClick={logout}> Logout </button>
                        </div>)
                }
                
                {
                    isLoggedIn &&  (<div className='second_icon'>
                <Link to="/cart" className='link'><FaShoppingCart /></Link>
                </div>)
                }
               
            </div>
        </div>
    </div>
    <div className='header'>
        <div className='container'>
            <div className='nav'>
            <ul>
                <li>
                    <Link to='/' className='link'>Home</Link>
                </li>
                <li>
                    <Link to='/product' className='link'>Products</Link>
                </li>
                <li>
                    <Link to='/about'className='link'>About</Link>
                </li>
                <li>
                    <Link to='/contact'className='link'>Contact Us</Link>
                </li>
                {
                    !isLoggedIn && (
                        <li>
                        <Link to='/login'className='link'>Login</Link>
                    </li>
                    )
                }
                {
                    isLoggedIn && (
                        <li>
                       <Link to='/cart'className='link'>WishList</Link>
                    </li>
                    )
                }
                
            </ul>
            </div>
            
        </div>
    </div>
    </>
  )
}

 export default Nav;
