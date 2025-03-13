
import './ErrorMsg.css'


function ErrorMsg({isOpen, msg}) {
    if (!isOpen) {return null}
    return (
        <div className="error">
            Error: {msg}
        </div>
    )
}

export default ErrorMsg