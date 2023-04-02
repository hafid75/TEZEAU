import React from "react";
import "./NavBar.css";

import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <nav>
      <Link
        to="/"
        className="nav-logo"
        aria-label="Visiter la page d'accueil de TezEau"
        aria-current="page"
      >
        <span>TezEau</span>
      </Link>

      <div className="nav-links">
        <Link to="/dashBoard">Dash Board</Link>
        <Link to="/vote">Mon vote</Link>
      </div>

      <button className="nav-signup">Sign up</button>
      <button className="nav-signin">Sign in</button>
    </nav>
  );
};

export default NavBar;
