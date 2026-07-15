import { useState } from "react";

export default function Settings() {
  const [model, setModel] = useState("llama3.2");
  const [algorithm, setAlgorithm] = useState("hnsw");
  const [topK, setTopK] = useState(5);

  return (
    <div style={{ padding: 30 }}>
      <h1>Settings</h1>

      <div
        style={{
          background: "#1f2937",
          color: "white",
          padding: 25,
          borderRadius: 12,
          maxWidth: 600,
        }}
      >
        <div style={{ marginBottom: 20 }}>
          <label>Model</label>

          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            style={{
              width: "100%",
              marginTop: 8,
              padding: 10,
              borderRadius: 8,
            }}
          >
            <option>llama3.2</option>
          </select>
        </div>

        <div style={{ marginBottom: 20 }}>
          <label>Search Algorithm</label>

          <select
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
            style={{
              width: "100%",
              marginTop: 8,
              padding: 10,
              borderRadius: 8,
            }}
          >
            <option value="hnsw">HNSW</option>
            <option value="kdtree">KDTree</option>
            <option value="bruteforce">Brute Force</option>
          </select>
        </div>

        <div style={{ marginBottom: 20 }}>
          <label>Top K Results</label>

          <input
            type="number"
            value={topK}
            onChange={(e) => setTopK(Number(e.target.value))}
            style={{
              width: "100%",
              marginTop: 8,
              padding: 10,
              borderRadius: 8,
            }}
          />
        </div>

        <button
          style={{
            width: "100%",
            padding: 12,
            border: "none",
            borderRadius: 10,
            background: "#2563eb",
            color: "white",
            cursor: "pointer",
          }}
        >
          Save Settings
        </button>
      </div>
    </div>
  );
}