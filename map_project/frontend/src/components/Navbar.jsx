import { NavLink } from "react-router-dom";
import { useState } from "react";
import styled from 'styled-components';

const NavbarWrapper = styled.div`
  width: 100%;
  height: 6rem;
  background: #000;
  z-index: 15;
  position: fixed;	
  left: 0;
  top: 0;
  padding: 0 10vw;
  box-shadow: 0 0 10px 10px rgba(0, 0, 3, 0.2);
`;

const NavbarComponent = styled.span`
  position: fixed;
  top: 0;
  right: 0;
  margin-right: 5vw;
  display: flex;
  gap: 5vw;
  @media (max-width: 750px) {
    display: none;
  }
`;

const SidebarWrapper = styled.div`
  position: fixed;
  display: grid;
  height: calc(100vh - min(8vw, 1.5rem));
	width: min(45vw, 20rem);
	overflow-x: hidden; 
  overflow-y: auto;
  background: #000;
	right: 0%; top: 0%;
	transition: all 0.7s cubic-bezier(.53, -0.41, .55, 1.2);
`;


const NavTitle = styled.h1`
  color: #fff;
  text-decoration: none;
  transition: all 0.1s ease-out;
  margin-right: 25vw;
  margin-top: 1.5rem;
`;

const NavFont = styled.h2`
  display: inline-block;
  color: #777;
  text-decoration: none;
  margin-top: 1.5rem;
  transition: all 0.1s ease-out;
  &:hover {
    color: #fff;
    transition: all 0.1s ease-out;
    transform: scale(1.05);
  }
`;

const SideFont = styled.h2`
  display: inline-block;
  color: #777;
  text-decoration: none;
  margin-left: 1.5rem;
  transition: all 0.1s ease-out;
  &:hover {
    color: #fff;
    transition: all 0.1s ease-out;
    transform: scale(1.05);
  }
`;

const XBarWrapper = styled.div`
  position: fixed;
  top: 0%;
  right: 0.5%;
  z-index: 1000;
  cursor: pointer;
`;

const XBar = styled.div`
  display: inline-block;
  color: #777;
  text-decoration: none;
  transition: all 0.1s ease-out;
  font-size: 5rem;
  margin-right: 1rem;
  &:hover {
    color: #fff;
    transition: all 0.1s ease-out;
    transform: scale(1.05);
  }
`;

const BurgerbarWrapper = styled.div`
  position: fixed;
  top: 0%;
  right: 0%;
  margin-top: 1.0rem;
  margin-right: 2.0rem;
  @media (min-width: 750px) {
    display: none;
  }
`;

const WhiteLine = styled.span`
  display: flex;
  width: 3rem;
  height: 0.6rem;
  margin: 0.5rem 0;
  border-radius: 3px;
  position: relative;
  background: #fff;
  z-index: 100;
  cursor: pointer;
`;

const Navbar = () => {
  const [sideBarOn, updateSideBarOn] = useState(false);
  return (
      <>
        <NavbarWrapper>
          <NavTitle>TrackTC</NavTitle>
          <NavbarComponent>
            <NavLink title="home" to="/" style={{textDecoration: 'none'}}><NavFont>Home</NavFont></NavLink>
            <NavLink title="login" to="/accounts/login/" style={{textDecoration: 'none'}}><NavFont>Log In</NavFont></NavLink>
            <NavLink title="sign up" to="/accounts/signup/" style={{textDecoration: 'none'}}><NavFont>Sign Up</NavFont></NavLink>
          </NavbarComponent>
          <BurgerbarWrapper onClick={() => updateSideBarOn(true)}>
            <WhiteLine/>
            <WhiteLine/>
            <WhiteLine/>
          </BurgerbarWrapper>
          {sideBarOn 
          ? <SidebarWrapper>
              <XBarWrapper onClick={() => updateSideBarOn(false)}><XBar>×</XBar></XBarWrapper>
              <br/>
              <NavLink title="home" to="/" style={{textDecoration: 'none'}}><SideFont>Home</SideFont></NavLink>
              <NavLink title="login" to="/accounts/login/" style={{textDecoration: 'none'}}><SideFont>Log In</SideFont></NavLink>
              <NavLink title="signup" to="/accounts/signup/" style={{textDecoration: 'none'}}><SideFont>Sign Up</SideFont></NavLink>
            </SidebarWrapper> 
          : <></>}
        </NavbarWrapper>
      </>
    );
}

export default Navbar;