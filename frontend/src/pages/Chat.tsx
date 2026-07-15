import { useRef, useState } from "react";
import api from "../services/api";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  async function uploadFile(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    const file = e.target.files?.[0];

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {
      await api.post("/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: `✅ ${file.name} uploaded successfully.`,
        },
      ]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "❌ Upload failed.",
        },
      ]);
    }
  }

  async function sendMessage() {
    if (!message.trim() || loading) return;

    const text = message;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const res = await api.post("/chat", {
        message: text,
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: res.data.answer,
        },
      ]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "❌ Unable to contact AI.",
        },
      ]);
    }

    setLoading(false);
  }

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "82vh",
      }}
    >
      <h1>Nyrion AI Chat</h1>

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: 20,
          background: "#111827",
          borderRadius: 12,
          marginBottom: 20,
        }}
      >
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              display: "flex",
              justifyContent:
                msg.role === "user"
                  ? "flex-end"
                  : "flex-start",
              marginBottom: 15,
            }}
          >
            <div
              style={{
                maxWidth: "70%",
                padding: "14px 18px",
                borderRadius: 16,
                background:
                  msg.role === "user"
                    ? "#2563eb"
                    : "#1f2937",
                color: "white",
              }}
            >
              {msg.content}
            </div>
          </div>
        ))}

        {loading && (
          <div style={{ color: "#9ca3af" }}>
            Nyrion is thinking...
          </div>
        )}
      </div>

      <input
        type="file"
        ref={fileInputRef}
        style={{ display: "none" }}
        onChange={uploadFile}
      />

      <div
        style={{
          display: "flex",
          gap: 10,
          alignItems: "center",
        }}
      >
        <button
          onClick={() => fileInputRef.current?.click()}
          style={{
            width: 120,
            borderRadius: 10,
            border: "none",
            background: "#10b981",
            color: "white",
            fontWeight: 600,
            cursor: "pointer",
          }}
        >
          📎 Upload
        </button>

        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
          placeholder="Ask anything..."
          style={{
            flex: 1,
            padding: 15,
            borderRadius: 10,
            border: "none",
            fontSize: 16,
          }}
        />

        <button
          onClick={sendMessage}
          style={{
            width: 120,
            borderRadius: 10,
            border: "none",
            background: "#2563eb",
            color: "white",
            fontWeight: 600,
            cursor: "pointer",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}