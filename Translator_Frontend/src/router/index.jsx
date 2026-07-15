import { createBrowserRouter } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Home from "../pages/Home";
import Dashboard from "../pages/Dashboard";
import Translation from "../pages/Translation";
import Dataset from "../pages/Dataset";
import Contribute from "../pages/Contribute";
import History from "../pages/History";
import About from "../pages/About";
import NotFound from "../pages/NotFound";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    errorElement: <NotFound />,

    children: [
      {
        index: true,
        element: <Home />,
      },

      {
        path: "dashboard",
        element: <Dashboard />,
      },

      {
        path: "translation",
        element: <Translation />,
      },

      {
        path: "translate",
        element: <Translation />,
      },

      {
        path: "dataset",
        element: <Dataset />,
      },

      {
        path: "contribute",
        element: <Contribute />,
      },

      {
        path: "history",
        element: <History />,
      },

      {
        path: "about",
        element: <About />,
      },
    ],
  },
]);
