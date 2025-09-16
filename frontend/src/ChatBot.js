import React, { useState } from "react";
import { sendMessage } from "./api";
import "./styles.css";
import rexLogo from "./rex-logo.png";

export default function ChatBot() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hi! Ask me investment questions." }
  ]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input) return;

    // Add user message
    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);

    // Await bot reply and add it
    const botReply = await sendMessage(input);
    setMessages([...newMessages, { sender: "bot", text: botReply }]);

    setInput("");
  };


  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((m, i) => (
          <div className={`msg ${m.sender}`} key={i}>
            <b>{m.sender === "bot" ? "Rex" : "You"}:</b> {m.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input value={input} onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && handleSend()} />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}
