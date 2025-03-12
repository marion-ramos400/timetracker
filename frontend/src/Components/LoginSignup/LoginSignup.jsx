import React, { useState } from "react";
import axios from 'axios';
import './LoginSignup.css'
import { signupEndpoint, loginEndpoint } from "../../backendConfig";
import {useNavigate} from 'react-router-dom'


function LoginSignup() {
    
    const navigate = useNavigate()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const signup = (user, pw) => {
        axios.post(signupEndpoint, {username: user, password: pw})
            .then(res => {
                if (res.status < 300) {
                    //if signin success, save login data to sessionStorage
                    sessionStorage.setItem('login', res.data)
                    //go to dashboard
                    navigate('/dash')
                }
            })
    }
    const login = (user, pw) => {
        axios.post(loginEndpoint, {}, {
            auth:{username: user, password: pw} 
        })
            .then(res => {
                if (res.status < 300) {
                    //if login success, save login data to sessionStorage
                    sessionStorage.setItem('login', JSON.stringify(res.data))
                    //go to dashboard
                    navigate('/dash')
                }
            })
    }

    function handleChangeUsername(e) {
        setUsername(e.target.value)
    }
    function handleChangePassword(e) {
        setPassword(e.target.value)
    }
    return (
        <div className="container">
            <div className="header">
                {/*<div className="text">Sign Up</div>*/}
            </div>
            <div className="inputs">
                <div className="input">
                    <input type="username" placeholder="username" onChange={handleChangeUsername}></input>
                </div>
                <div className="input">
                    <input type="password" placeholder="password" onChange={handleChangePassword}></input>
                </div>
            </div>
            <div className="submit-container">
                <div className="submit" onClick={() => signup(username, password)}>Sign Up</div>
                <div className="submit" onClick={() => login(username, password)}>Login</div>
            </div>
        </div>
    )

}

export default LoginSignup