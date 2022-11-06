import { NavLink } from "react-router-dom";
import styled from 'styled-components';

const NavbarWrapper = styled.div`
  display: flex;
  width: 100%;
  height: 6rem;
  background: #000;
  z-index: 15;
  position: fixed;	
  gap: 5vw;
  left: 0;
  top: 0;
  padding: 0 10vw;
  box-shadow: 0 0 10px 10px rgba(0, 0, 3, 0.2);
`;

const NavTitle = styled.h1`
  color: #fff;
  text-decoration: none;
  transition: all 0.1s ease-out;
  margin-right: 25vw;
  margin-top: 1.5rem;
  &:hover {
    transition: all 0.1s ease-out;
    transform: scale(1.10);
  }
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

const Navbar = () => {
  return (
      <NavbarWrapper>
        <NavTitle>TrackTC</NavTitle>
        <NavLink title="home" to="/" style={{textDecoration: 'none'}}><NavFont>Home</NavFont></NavLink>
        <NavLink title="login" to="/accounts/login/" style={{textDecoration: 'none'}}><NavFont>Log In</NavFont></NavLink>
        <NavLink title="signup" to="/accounts/signup/" style={{textDecoration: 'none'}}><NavFont>Sign Up</NavFont></NavLink>
      </NavbarWrapper>
    );
}

export default Navbar;