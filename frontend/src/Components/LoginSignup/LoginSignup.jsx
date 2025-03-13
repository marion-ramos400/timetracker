import React, { useState } from "react";
import axios from 'axios';
import './LoginSignup.css'
import { signupEndpoint, loginEndpoint } from "../../backendConfig";
import {useNavigate} from 'react-router-dom'
import ErrorMsg from "../ErrorMsg/ErrorMsg";


function LoginSignup() {
    
    const navigate = useNavigate()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [isError, setIsError] = useState(false)
    const [errorMsg, setErrorMsg] = useState("")

    const isEmptyField = () => {
        if (username === "" | password === "") return true
        return false
    }

    const signup = (user, pw) => {
        if (isEmptyField()){
            setErrorMsg("Empty Field")
            setIsError(true)
            return
        }
        axios.post(signupEndpoint, {username: user, password: pw})
            .then(res => {
                if (res.status < 300) {
                    //if signin success, save login data to sessionStorage
                    sessionStorage.setItem('login', JSON.stringify(res.data))
                    //go to dashboard
                    navigate('/dash')
                }
            }).catch(error => {
                    //show error message
                    setErrorMsg(JSON.stringify(error.response.data))
                    setIsError(true)
            })
    }
    const login = (user, pw) => {
        if (isEmptyField()){
            setErrorMsg("Empty Field")
            setIsError(true)
            return
        }
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
            }).catch(error => {
                    //show error message
                    setErrorMsg(JSON.stringify(error.response.data))
                    setIsError(true)
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
                <ErrorMsg isOpen={isError} msg={errorMsg}/>
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