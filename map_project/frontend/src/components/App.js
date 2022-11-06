import React, { Component } from "react";
import { render } from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home.jsx";
import Navbar from "./Navbar.jsx";
window.React = React;

const App = () => {
    return (
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Home/>}/>
            </Routes>
        </Router>
    );
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);