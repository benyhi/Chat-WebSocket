import React, { useState, useEffect } from "react";
import { Box, TextField, Button, Typography, Paper, List, ListItem, ListItemText } from "@mui/material";
import {io} from "socket.io-client";

const socket = io("http://localhost:5000/chat");

const Chat = () => {
  const [messages, setMessages] = useState([]); // Lista de mensajes
  const [inputMessage, setInputMessage] = useState(""); // Mensaje actual

    // Escuchar mensajes entrantes
    useEffect(() => {
        socket.on("message", (data) => {
          setMessages((prevMessages) => [...prevMessages, data]);
        });
    
        // Limpiar la conexión al desmontar el componente
        // return () => {
        //   socket.off("message");
        // };
    }, []);

  // Maneja el envío de mensajes
  const handleSendMessage = () => {
    if (inputMessage.trim() === "") return; // Evitar mensajes vacíos
    const newMessage = { text: inputMessage, sender: "Tú"}
    socket.emit("message", newMessage)
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInputMessage("");
  };

  // Maneja el Enter para enviar mensajes
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        width: "400px",
        margin: "0 auto",
        backgroundColor: "#f5f5f5",
        borderRadius: 2,
        boxShadow: 3,
      }}
    >
      {/* Header */}
      <Typography variant="h6" component="div" sx={{ padding: 2, textAlign: "center", backgroundColor: "#3f51b5", color: "white" }}>
        Chat App
      </Typography>

      {/* Lista de mensajes */}
      <Paper
        elevation={3}
        sx={{
          flex: 1,
          overflowY: "auto",
          margin: 2,
          padding: 2,
        }}
      >
        <List>
          {messages.map((message, index) => (
            <ListItem key={index}>
              <ListItemText
                primary={message.sender}
                secondary={message.text}
                primaryTypographyProps={{ fontWeight: "bold" }}
              />
            </ListItem>
          ))}
        </List>
      </Paper>

      {/* Input para escribir mensajes */}
      <Box
        sx={{
          display: "flex",
          gap: 1,
          padding: 2,
          borderTop: "1px solid #ddd",
        }}
      >
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Escribe un mensaje..."
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyDown={handleKeyPress}
        />
        <Button variant="contained" color="primary" onClick={handleSendMessage}>
          Enviar
        </Button>
      </Box>
    </Box>
  );
};

export default Chat;
