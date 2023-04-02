import { React } from "react";
import "./Form.css";

import NavBar from "./NavBar";

const Form = () => {
  return (
    <>
      <NavBar />
      <div className="form-container">
        <iframe
          src="https://docs.google.com/forms/d/1c8KXC0-BwokL2EJPi36Tp8HIuMG6l5gsIe00tAl07eQ/viewform?embedded=true"
          width="100%"
          height="1124"
          title="Quizz"
        >
          Chargement…
        </iframe>
      </div>
    </>
  );
};

export default Form;
