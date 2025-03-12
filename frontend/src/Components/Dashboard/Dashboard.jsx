
import React, { useState, useEffect } from "react";
import axios from 'axios';
import { getUsersEndpoint, getTasksEndpoint, createTaskEndpoint } from "../../backendConfig";
import './Dashboard.css'

function Dashboard() {
    const newdt = new Date()
    const [monthd, setMonth] = useState(newdt.getMonth() + 1)
    const [weekd, setWeek] = useState(1)
    const [tableData, setTableData] = useState([])
    const [projectsData, setProjectsData] = useState([])
    const [userList, setUserList] = useState([])

    useEffect(() => {
        getUserList()
    }, []);

    function getSeshToken() {
        return JSON.parse(sessionStorage.login).token
    }

    function getUserList() {
        const seshtoken = getSeshToken()
        axios.get(getUsersEndpoint, {
            headers: {
                Authorization: `Token ${seshtoken}`
            }
        }).then(res => {
                if (res.status < 300) {
                    const resp_users = res.data.users
                    setUserList(
                        resp_users.map((u, idx) => {
                            if (idx === 0) {
                                console.log("here?")
                                return <option value={u} selected>{u}</option>
                            }
                            else {return <option value={u}>{u}</option>}
                        })
                    )
                    handleChange()
                }
            }
        )
    }


    function handleChange(e=null) {
        const month = document.getElementById("month").value.split("-")[1]
        const week = document.getElementById("week").value
        const user = document.getElementById("user-select").value
        loadWeekTable(month, week, user)

    }

    function loadWeekTable(month, week, user) {
        //populate tasks table
        const seshtoken = getSeshToken()
        axios.get(getTasksEndpoint, {params: {
            month: parseInt(month),
            week: parseInt(week),
            user: user
        },
            headers: {
                Authorization: `Token ${seshtoken}`
            }
        }).then(res => {
            if (res.status < 300) {

                setTableData(
                    res.data.tasks.map((t) => {
                        return <tr>
                            <td>{t.start_dt}</td>
                            <td>{t.description}</td>
                            <td>{t.hours}</td>
                            <td>{t.project}</td>
                        </tr>
                })
                )

                loadProjectsTable(res.data.projects_total_hrs)
            }
        })
    }

    function loadProjectsTable(projHrsData) {
        let projHrsArr = []
        for (let key in projHrsData) {
            let item = [key, projHrsData[key]]
            projHrsArr.push(
                item
            )
        }
        setProjectsData(
            projHrsArr.map((item) => {
                return <tr>
                    <td>{item[0]}</td>
                    <td>{item[1]}</td>
                </tr>
            })
        )
    }

    return (
        <div>
            <div className="date-select">
                Month: <input type="month" id="month" min="2025-01" max="2025-12" onChange={handleChange} value={`2025-${String(monthd).padStart(2, "0")}`}/>
                Week: <select name="week" id="week" onChange={handleChange}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
                User: <select name="user" id="user-select" onChange={handleChange}>
                    {userList}
                </select>

            </div>
            <div className="timesheet">
                <table>
                    <thead>
                        <tr>
                            <th>DateTime</th>
                            <th>Task</th>
                            <th>Number Of Hrs</th>
                            <th>Project</th>
                        </tr>
                    </thead>
                    <tbody>
                        {tableData}
                    </tbody>
                </table>
            </div>
            <br></br>
            <div className="projects-total">
               <table>
                    <thead>
                        <tr>
                            <th>Project</th>
                            <th>Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        {projectsData} 
                    </tbody>
                </table> 
            </div>
        </div>
    )
}


export default Dashboard
