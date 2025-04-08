import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Login from './components/VideogameDatabase';
import HomePage from "./components/HomePage";
import GameCopiesFront from './components/GameCopiesFront';
import DatabaseDisplay from './components/DatabaseDisplay';
import CreateConsole from './components/CreateConsole';
import AddData from './components/AddData';
import About from './components/About';
import ProtectedRoute from './components/ProtectedRoute';
import NavBar from './components/NavBar';
import { AuthProvider } from './auth/AuthProvider';

const Layout = ({ children }) => (
  <>
    <NavBar />
    {children}
  </>
);

const App = () => {
  const router = createBrowserRouter([
    {
      path: "/myapp/",
      element: <Layout><Login /></Layout>
    },
    {
      path: "/myapp/home",
      element: <Layout><ProtectedRoute><HomePage /></ProtectedRoute></Layout>
    },
    {
      path: "/myapp/signup",
      element: <Layout><Login /></Layout>
    },
    {
      path: "/myapp/gamecopiesfront",
      element: <Layout><ProtectedRoute><GameCopiesFront /></ProtectedRoute></Layout>
    },
    {
      path: "/myapp/databasedisplay",
      element: <Layout><ProtectedRoute><DatabaseDisplay /></ProtectedRoute></Layout>
    },
    {
      path: "/myapp/createconsole",
      element: <Layout><ProtectedRoute><CreateConsole /></ProtectedRoute></Layout>
    },
    {
      path: "/myapp/adddata",
      element: <Layout><ProtectedRoute><AddData /></ProtectedRoute></Layout>
    },
    {
      path: "/myapp/about",
      element: <Layout><About /></Layout>
    }
  ]);

  return (
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  );
};

export default App;

