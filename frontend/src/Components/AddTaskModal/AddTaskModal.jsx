
import React, { useState, useEffect } from "react";
import DateTimePicker from 'react-datetime-picker'
import axios from 'axios';
import {createTaskEndpoint } from "../../backendConfig";
import { getSessionToken } from "../../helper";
import './AddTaskModal.css'


function AddTaskModal({isOpen, onClose}) {
    if (!isOpen) {return null}
    function getProjects(){
        const projects = sessionStorage.projects.split(',')
        return projects.map((p, idx) => {
            if (idx === 0) {
                return <option value={p} selected>{p}</option>
            }
            else {return <option value={p}>{p}</option>}
        })
    }

    function setDefaultDateTime(){
        let now = new Date();
        let utcString = now.toISOString().substring(0,19);
        let year = now.getFullYear();
        let month = now.getMonth() + 1;
        let day = now.getDate();
        let hour = now.getHours();
        let minute = now.getMinutes();
        let second = now.getSeconds();
        let localDatetime = year + "-" +
                          (month < 10 ? "0" + month.toString() : month) + "-" +
                          (day < 10 ? "0" + day.toString() : day) + "T" +
                          (hour < 10 ? "0" + hour.toString() : hour) + ":" +
                          (minute < 10 ? "0" + minute.toString() : minute) +
                          utcString.substring(16,19);
        return localDatetime 
    }
   
    function createTask(){
        const token = getSessionToken()
        const projSelect = document.getElementById("project-select")
        const payload = {
            user: JSON.parse(sessionStorage.login).user,
            start_dt: document.getElementById("task-datetime").value,
            hours: document.getElementById("task-hrs").value,
            description: document.getElementById("task-desc").value,
            project: projSelect.options[projSelect.selectedIndex].text
        }
        axios.post(createTaskEndpoint, payload,
            {
                headers: {
                    Authorization: `Token ${token}`
                }
            }
        ).then(res => {
                if (res.status < 300) {
                    onClose()
                }
            }
        )

    }


    return (
        <div className="bg-container">
            <div className="modal-container">
                <div className="inputs">
                    <div>
                        <label>Task Start Date Time: </label>
                        <input aria-label="Date and time" id="task-datetime" type="datetime-local" 
                            defaultValue={setDefaultDateTime()}
                            />
                    </div>
                    <div>
                        <label>Task Description: </label><input type="text" placeholder="task" id="task-desc"></input>
                    </div>
                    <div>
                        <label>Hours: </label><input type="number" placeholder="number of hours" id="task-hrs"></input>
                    </div>
                    <div>
                        <label>Project: </label>
                        <select name="project" id="project-select">
                            {getProjects()}
                        </select>
                    </div>
                </div>
                <div className="modal-btn-container">
                    <div className="modal-btn close" onClick={onClose}>Close</div>
                    <div className="modal-btn" onClick={createTask}>Create</div>
                </div>
            </div>
        </div>

    )
}

export default AddTaskModal