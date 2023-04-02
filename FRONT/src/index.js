import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import './assets/fonts/fonts.css';


import Home from './components/Home';
import Form from './components/Form';
import DashBoard from './components/DashBoard';
import Vote from './components/Vote';


import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Home/>,
  },
  {
    path: "/form",
    element: <Form/>,
  },
  {
    path: "/dashBoard",
    element: <DashBoard/>,
  },
  {
    path: "/vote",
    element: <Vote/>,
  }
]);




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
