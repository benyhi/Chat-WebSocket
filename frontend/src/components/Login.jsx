import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    Box,
    TextField,
    Button,
    Typography,
    Container,
    Alert,
} from "@mui/material";
import { setToken } from './../auth'

const Login = () => {
    const navigate = useNavigate()
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

    // Validación simple
        if (!email || !password || !username ) {
            setError("Por favor, completa todos los campos.");
            setSuccess("");
            return;
        }
        if (!/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
            setError("Ingresa un correo válido.");
            setSuccess("");
            return;
        }

        const loginData = {
            username: username,
            email: email,
            password: password
        }
    
        try{
            const response = await fetch("http://localhost:5000/login", {
                method: 'POST',
                headers: {
                    'Content-Type':'application/json',
                },
                body: JSON.stringify(loginData)
            });
            if (!response.ok){
                throw new Error('Login fallido. Verifica tus credenciales.');
            }

            const data = await response.json();

            setToken(data.Token);
            
            console.log('Login exitoso', data)

            setSuccess("Inicio de sesion exitoso. Redirigiendo...")
            setTimeout(() => navigate("/"), 2000);

        } catch (error){
            setError(error.message);
        }
    };

    return (
    <Container maxWidth="sm">
        <Box
        sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
        }}
        >
        <Typography component="h1" variant="h5">
            Iniciar Sesión
        </Typography>
        <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}
        >
            {error && <Alert severity="error">{error}</Alert>}
            {success && <Alert severity="success">{success}</Alert>}
            <TextField
            margin="normal"
            required
            fullWidth
            id="username"
            label="Nombre de Usuario"
            name="username"
            autoComplete="username"
            autoFocus
            value={username}
            onChange={(e) => setUsername(e.target.value)}/>
            <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="Correo Electrónico"
            name="email"
            autoComplete="email"
            autoFocus
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Contraseña"
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />
            <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            >
            Iniciar Sesión
            </Button>
        </Box>
        </Box>
    </Container>
  );
};

export default Login;
