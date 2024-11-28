import { useNavigate } from "react-router-dom"

function Home(){
    const navigate = useNavigate();

    const handleRedirect = () => { navigate("/chat"); }

    return(
        <div style={{
            border: "1px solid white",
            borderRadius: 10,
            padding: 20   
        }}>
            <h3>Sala de chat 1</h3>
            <button onClick={ handleRedirect }>Entrar</button>
        </div>
    )
}

export default Home