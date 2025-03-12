import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from './Components/Dashboard/Dashboard'
import logo from './logo.svg';
import './App.css';
import LoginSignup from './Components/LoginSignup/LoginSignup';

function App() {
  return (

    <BrowserRouter>
        <Routes>
            <Route path="/" element={<LoginSignup/>}/>
            <Route path="/dash" element={<Dashboard/>}/>
        </Routes>
    </BrowserRouter>

  );
}

export default App;



    {/*
    <div>
        
        <LoginSignup/>
    </div>
    */}
