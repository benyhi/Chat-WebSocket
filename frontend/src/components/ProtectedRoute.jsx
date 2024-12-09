import { Navigate } from "react-router-dom";
import { getToken } from './../auth'

const ProtectedRoute = ({ children }) =>{
    const token = getToken();
    console.log(token)

    if (!token){
        return <Navigate to="/login" />;
    }

    return children;
};

export default ProtectedRoute