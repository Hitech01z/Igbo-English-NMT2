import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import "./styles/globals.css";
import { Toaster } from "react-hot-toast";

import { router } from "./router";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
    <Toaster position="top-right" />
  </React.StrictMode>
);