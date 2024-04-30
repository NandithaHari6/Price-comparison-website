import React, { useState ,useEffect} from 'react'
import { FaShoppingCart } from "react-icons/fa";
import { FaUser } from "react-icons/fa";
import { CiLogin } from 'react-icons/ci';
import { CiLogout } from 'react-icons/ci';
import { Link } from 'react-router-dom';
import { useAuth0 } from "@auth0/auth0-react";
import Logo from "./img/logo.svg";

import './nav.css'
const Nav = ({searchbtn,isLoggedIn}) => {
    const [search, setSearch] = useState('');
    const { loginWithRedirect, logout, user, isAuthenticated} = useAuth0();
    const [showUserDetails, setShowUserDetails] = useState(false);

    useEffect(() => {
        if (isAuthenticated) {
            setShowUserDetails(true);
        }
    }, [isAuthenticated]);

    const handleUserIconClick = () => {
        if (!isLoggedIn) {
            loginWithRedirect();
        }
        else {
            setShowUserDetails(!showUserDetails);
        }
    };
  return (
    <>
   
    <div className='main_header'>
        <div className='container'>
            <div className='logo'>
                <img src={Logo} alt='logo'></img>
            </div>
            <div className='search_box'>
                <input type='text' value={search} placeholder='Search Your Product...' autoComplete='off' onChange={(e) => setSearch(e.target.value)}></input>
                <button onClick={() => searchbtn (search)}>Search</button>
            </div>
            <div className='icon'>
                {
                    
                        <div className='account'>
                        <div className='user_icon' onClick={handleUserIconClick}>
                            <FaUser />
                            {showUserDetails && isAuthenticated && <p>Hello, {user.name}</p>}
                        </div>
                        </div>
                    
                }
                <div className='second_icon'>
                <Link to="/cart" className='link'><FaShoppingCart /></Link>
                </div>
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
                
            </ul>
            </div>
            <div className='auth' >
                {
                    isAuthenticated ?
                    <button onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}><CiLogout />Logout</button>
                    :
                    <button onClick={() => loginWithRedirect()}><CiLogin />Login</button>
                }
            </div>
        </div>
    </div>
    </>
  )
}

 export default Nav;
