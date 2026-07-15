import { useState } from "react";
import api from "../services/api";

export default function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  async function search() {
    if (!query.trim()) return;

    setLoading(true);

    try {
      const res = await api.post("/chat", {
        message: query,
      });

      setResults(res.data.context || []);
    } catch (err) {
      console.error(err);
      setResults([]);
    }

    setLoading(false);
  }

  return (
    <div style={{ padding: 30 }}>
      <h1>Semantic Search</h1>

      <div
        style={{
          display: "flex",
          gap: 10,
          marginBottom: 20,
        }}
      >
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search..."
          style={{
            flex: 1,
            padding: 12,
            borderRadius: 8,
          }}
        />

        <button onClick={search}>
          Search
        </button>
      </div>

      {loading && <p>Searching...</p>}

      {results.map((item, index) => (
        <div
          key={index}
          style={{
            padding: 15,
            marginBottom: 15,
            background: "#1f2937",
            color: "white",
            borderRadius: 10,
          }}
        >
          <h3>{item.category}</h3>

          <p>{item.metadata}</p>

          <small>
            Distance: {item.distance}
          </small>
        </div>
      ))}
    </div>
  );
}