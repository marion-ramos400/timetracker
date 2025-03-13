
export const getSessionToken = () => {
    const login = sessionStorage.login 
    if (login == undefined) {
        return null
    }

    return JSON.parse(sessionStorage.login).token
}

export const getLoginStorage = () => {
    return JSON.parse(sessionStorage.login)
}

export const clearSessionToken = () => {
    sessionStorage.setItem('login', JSON.stringify({}));
}

