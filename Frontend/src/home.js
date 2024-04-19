import React, { useState, useEffect } from 'react'
import {Link } from 'react-router-dom'
import { BsArrowRight } from 'react-icons/bs';
import { AiOutlineShoppingCart, AiOutlineCloseCircle } from 'react-icons/ai';
import { BsEye } from 'react-icons/bs';
import Homeproduct from './homeproduct';
import './home.css'
import mobile from "./img/Mobile Phone.png";
import ac from "./img/ac.png";
import lap from "./img/lap.png";
import fridge from "./img/fridge.png";
import { AiFillAmazonCircle } from "react-icons/ai";
import { SiFlipkart } from "react-icons/si";
import { IoGridSharp } from "react-icons/io5";
import { TbCircleLetterC } from "react-icons/tb";
import smartwatch from "./img/smart watch.png";
import headphone from "./img/headphone.png";
import tablets from "./img/tablets.png"
import slider2 from "./img/smw.png"
import slider3 from "./img/slider3.png"


const Home = ({detail, view, close, setClose, addtocart}) => {
 
    const [currentSlide, setCurrentSlide] = useState(0);
    const sliderImages = [tablets, slider2, slider3];
    function nextSlide() {
      setCurrentSlide(function(prevIndex) {
        return (prevIndex + 1) % sliderImages.length;
      });
    }
    useEffect(() => {
    const interval = setInterval(nextSlide, 1500); // Change slide every 5 seconds
    return () => clearInterval(interval);
  }, []);
  return(
  <>
    <div className='top_banner'>
        <div className='container'>
            <div className='detail'>
                <h2>Price Comparison Made Simple:</h2>
                <h3>Find the Best Deals in Seconds</h3>
            </div>
            <div className='img_box'>
                <img src={sliderImages[currentSlide]} alt='slider'></img>
            </div>
        </div>
    </div>
    <div className='product_type'>
      <div className='container'>
        <div className='box'>
          <div className='img_box'>
            <img src={mobile} alt='mobile'></img>
          </div>
          <div className='detail'>
            <p>Smartphones</p>
          </div>
        </div>
        <div className='box'>
          <div className='img_box'>
            <img src={lap} alt='lap'></img>
          </div>
          <div className='detail'>
            <p>Laptops</p>
          </div>
        </div>
        <div className='box'>
          <div className='img_box'>
            <img src={ac} alt='ac'></img>
          </div>
          <div className='detail'>
            <p>Air Conditioners</p>
          </div>
        </div>
        <div className='box'>
          <div className='img_box'>
            <img src={fridge} alt='fridge '></img>
          </div>
          <div className='detail'>
            <p>Refrigerators</p>
          </div>
        </div>
        <div className='box'>
          <div className='img_box'>
            <img src={headphone} alt='headphone'></img>
          </div>
          <div className='detail'>
            <p>Headphones</p>
          </div>
        </div>
        <div className='box'>
          <div className='img_box'>
            <img src={smartwatch} alt='smartwatch '></img>
          </div>
          <div className='detail'>
            <p>Smartwatches</p>
          </div>
        </div>
      </div>
    </div>
    <div className='about'>
      <div className='container'>
        <div className='box'>
        <a href="https://www.amazon.com" target="_blank" rel="noopener noreferrer">
          <div className='icon'>
            <AiFillAmazonCircle />
          </div>
          </a>
          <div className='detail'>
            <h2>Amazon</h2>
          </div>
          </div>
        <div className='box'>
        <a href="https://www.flipkart.com" target="_blank" rel="noopener noreferrer">
          <div className='icon'>
          <SiFlipkart />
          </div>
          </a>
          <div className='detail'>
            <h2>Flipkart</h2>
          </div>
        </div>
        <div className='box'>
        <a href="https://www.croma.com" target="_blank" rel="noopener noreferrer"> 
          <div className='icon'>
          <TbCircleLetterC />
          </div>
          </a>
          <div className='detail'>
            <h2>Croma</h2>
          </div>
        </div>
        <div className='box'>
          <div className='icon'>
          <IoGridSharp />
          </div>
          <div className='detail'>
            <h2>Many More</h2>
          </div>
        </div>
      </div>
    </div>
    <div className='product'>
      <h2>Top Products</h2>
      <div className='container'>
        {
          Homeproduct.map((curElm) => 
          {
            return(
              <div className='box' key={curElm.id}>
                <div className='img_box'>
                  <img src={curElm.Img} alt={curElm.Title}></img>
                  <div className='icon'>
                    <li onClick={() => addtocart (curElm)}><AiOutlineShoppingCart /></li>
                    <li onClick={() => view (curElm)}><BsEye /></li>
                                                       
                  </div>
                </div>
                <div className='detail'>
                  <p>{curElm.Cat}</p>
                  <h3>{curElm.Title}</h3>
                  <h4>${curElm.Price}</h4>
                </div>
              </div>
            )
          })
        }
      </div>
    </div>
    <div className='banner'>
      <div className='container'>
      <div className='detail'>
        <h4>LATEST TECHNOLOGY ADDED</h4>
        <h3>Apple iPad 10.2 9th Gen - 2024</h3>
        <p>$ 89986</p>
        <Link to='/product' className='link'>Shop Now  <BsArrowRight /></Link>
      </div>
      <div className='img_box'>
        <img src={tablets} alt='tablets'></img>
      </div>
      </div>
    </div>
    </>
  )
}

export default Home