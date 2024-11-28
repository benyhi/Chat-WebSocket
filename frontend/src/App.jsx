import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Chat from "./components/Chat"
import Home from "./components/Home"
import './assets/App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/chat" element={<Chat/>}/>
      </Routes>
    </Router>
  )
}

export default App
