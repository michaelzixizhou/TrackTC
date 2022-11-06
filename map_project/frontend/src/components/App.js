import React, { Component } from "react";
import { render } from 'react-dom';
import Home from "./Home.jsx";
window.React = React;

const App = () => {
    return (
        <>
            <Home/>
        </>
    );
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);