import React from "react";
import "./Vote.css";

import NavBar from "./NavBar";

const Vote = () => {
  return (
    <>
      <NavBar />
      <div className="vote-container">
        <div className="vote-header">
          <span className="vote-title">Sujet du vote :</span>
          <span className="vote-sujet">Réutilisation des eaux usées</span>
          <span className="vote-idTezos">
            L'utilisation de votre identifiant Tezos ne vous permettra de ne
            voter qu'une seule fois.
          </span>
        </div>
        <div className="vote-cards">
          <Card
            option="1"
            title="Traitement pour une utilisation non potable"
            text="Les eaux usées sont traitées
      pour éliminer les contaminants et les impuretés afin de les rendre propres
      à l'utilisation dans des applications non potables telles que l'irrigation
      des cultures, le lavage des voitures, le nettoyage des rues et des
      trottoirs, etc. Le traitement peut inclure des processus tels que la
      filtration, la désinfection, la décantation et la clarification."
          />
          <Card
            option="2"
            title="Traitement pour une utilisation potable"
            text="Les eaux usées sont traitées pour éliminer les contaminants et les impuretés afin de les rendre propres à la consommation humaine. Le traitement peut inclure des processus tels que la filtration, la désinfection, la coagulation, la clarification et l'osmose inverse. Ce type de réutilisation des eaux usées est moins courant en raison de la complexité et des coûts associés au traitement de l'eau."
          />
          <Card
            option="3"
            title="Traitement pour une utilisation industrielle"
            text="Les eaux usées sont traitées pour éliminer les contaminants spécifiques et pour répondre aux exigences de qualité de l'eau nécessaires pour une utilisation dans des applications industrielles spécifiques. Le traitement peut inclure des processus tels que la distillation, l'adsorption, l'échange d'ions et la microfiltration. Ce type de réutilisation des eaux usées est courant dans les industries qui nécessitent une grande quantité d'eau pour leurs processus de production tels que la production de papier, la production de produits chimiques et la production d'énergie."
          />
        </div>
      </div>
    </>
  );
};

const Card = ({ option, text, title }) => {
  return (
    <div className="card-container">
      <span>
        {option} - {title}
      </span>
      <p>{text}</p>
      <button>Choisir</button>
    </div>
  );
};

export default Vote;
