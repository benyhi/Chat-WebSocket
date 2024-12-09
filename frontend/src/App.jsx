import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Chat from "./components/Chat"
import Home from "./components/Home"
import Login from "./components/Login"
import './assets/App.css'
import ProtectedRoute from "./components/ProtectedRoute"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login/>}/>
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <Home/>
            </ProtectedRoute>
          }
        />
        <Route 
          path="/chat" 
          element={
            <ProtectedRoute>
              <Chat/>
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  )
}

export default App
