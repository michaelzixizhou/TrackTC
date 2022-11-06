import React, { Component } from "react";
import { render } from 'react-dom';
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from "react-router-dom";
import Home from "./Home.jsx";
import Navbar from "./Navbar.jsx";
import Signup from "./Signup.jsx";
window.React = React;

const App = () => {
    return (
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/signup" element={<Signup/>}/>
            </Routes>
        </Router>
    );
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);