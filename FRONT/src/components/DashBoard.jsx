import { React, useState } from "react";
import "./DashBoard.css";
import NavBar from "./NavBar";
import vague from "../assets/vague.png";
import pH_Rennes from "../assets/pH_Rennes.png";
import piezo from "../assets/piezo.png";

const DashBoard = () => {
  const [onglet_pH, setOnglet_pH] = useState(true);

  const changeOnglet = (btn) => {
    btn === "pH" ? setOnglet_pH(true) : setOnglet_pH(false);
  };

  return (
    <>
      <NavBar />
      <div className="dashBoard-container">
        <div className="dashBoard-left">
          <div className="dashBoard-towns">
            <span className="dashBoard-towns-title">Communes</span>
            <input type="text" placeholder="Rechercher une commune" />
            <div className="list-towns">
              <span>Pihen lès Guînes</span>
              <span>Vichy</span>
              <span>St Brieuc</span>
              <span>Quimper</span>
              <span>Brest</span>
              <span>Lorient</span>
              <span>Orléans</span>
              <span>Paris</span>
              <span>Strasbourg</span>
              <span>Lille</span>
              <span>Caen</span>
            </div>
          </div>
        </div>
        <div className="dashBoard-right">
          <div className="dashBoard-params">
            <button onClick={() => changeOnglet("pH")}>pH</button>
            <button onClick={() => changeOnglet("!pH")}>piézométrie</button>
          </div>
          <div className="dashBoard-graph">
            {onglet_pH ? (
              <div className="dashBoard-graph-imported">
                <img
                  src={pH_Rennes}
                  alt="graphique pH"
                  className="dashboard-pH"
                />
              </div>
            ) : (
              <div className="dashBoard-graph-imported">
                <img
                  src={piezo}
                  alt="graphique piézométrie"
                  className="dashboard-piezo"
                />
              </div>
            )}
          </div>
        </div>
      </div>
      <img src={vague} alt="water" className="dashboard-vag" />
    </>
  );
};

export default DashBoard;
