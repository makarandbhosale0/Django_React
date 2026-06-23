import React from 'react'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoutes'

// clears the cookies and redirects to login page to avoid using token of already logged in user
function Logout(){
  localStorage.clear();
  return <Navigate to="/login" />
}

// clears the cookies and redirects to register page to avoid using token of already logged in user
function RegisterAndLogout(){
  localStorage.clear();
  return <Register />
}



const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/'
        element={
        <ProtectedRoute>
          <Home />
        </ProtectedRoute>} />

        <Route path='/login' element={<Login />} />
        <Route path='/register' element={<RegisterAndLogout />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='*' element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App