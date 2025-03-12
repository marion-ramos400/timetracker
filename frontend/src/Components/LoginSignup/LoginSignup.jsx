import React, { useState } from "react";
import axios from 'axios';
import './LoginSignup.css'
import { signupEndpoint, loginEndpoint } from "../../backendConfig";

function LoginSignup() {
    
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const signup = (user, pw) => {
        axios.post(signupEndpoint, {username: user, password: pw})
            .then(res => {
                console.log(res)
                console.log(res.data)
            })
    }
    const login = (user, pw) => {
        console.log(`login ${user}`)
        console.log(`login ${pw}`)
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
                <div className="submit">Login</div>
            </div>
        </div>
    )

}

export default LoginSignup