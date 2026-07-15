import { useState } from "react";
import api from "../services/api";

export default function Knowledge() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [category, setCategory] = useState("knowledge");
  const [loading, setLoading] = useState(false);

  async function saveKnowledge() {
    if (!question || !answer) {
      alert("Enter question and answer.");
      return;
    }

    setLoading(true);

    try {
      await api.post("/knowledge", {
        question,
        answer,
        category,
      });

      alert("Knowledge saved!");

      setQuestion("");
      setAnswer("");
    } catch (err) {
      console.error(err);
      alert("Failed to save knowledge.");
    }

    setLoading(false);
  }

  return (
    <div style={{ padding: 30 }}>
      <h1>Knowledge Base</h1>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 15,
          maxWidth: 700,
        }}
      >
        <input
          placeholder="Question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{
            padding: 12,
            borderRadius: 8,
          }}
        />

        <textarea
          placeholder="Answer"
          rows={8}
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          style={{
            padding: 12,
            borderRadius: 8,
          }}
        />

        <input
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{
            padding: 12,
            borderRadius: 8,
          }}
        />

        <button
          onClick={saveKnowledge}
          disabled={loading}
          style={{
            padding: 12,
            border: "none",
            borderRadius: 8,
            background: "#2563eb",
            color: "white",
            cursor: "pointer",
          }}
        >
          {loading ? "Saving..." : "Save Knowledge"}
        </button>
      </div>
    </div>
  );
}