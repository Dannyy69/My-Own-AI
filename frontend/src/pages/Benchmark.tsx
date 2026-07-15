import { useEffect, useState } from "react";
import api from "../services/api";

export default function Benchmark() {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    api.get("/system/info")
      .then((res) => setStats(res.data))
      .catch(console.error);
  }, []);

  return (
    <div style={{ padding: 30 }}>
      <h1>Benchmark</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2,1fr)",
          gap: 20,
          marginTop: 20,
        }}
      >
        <div
          style={{
            background: "#1f2937",
            color: "white",
            padding: 20,
            borderRadius: 10,
          }}
        >
          <h2>Engine</h2>
          <h3>{stats?.engine}</h3>
        </div>

        <div
          style={{
            background: "#1f2937",
            color: "white",
            padding: 20,
            borderRadius: 10,
          }}
        >
          <h2>Status</h2>
          <h3>{stats?.status}</h3>
        </div>

        <div
          style={{
            background: "#1f2937",
            color: "white",
            padding: 20,
            borderRadius: 10,
          }}
        >
          <h2>Version</h2>
          <h3>{stats?.version}</h3>
        </div>

        <div
          style={{
            background: "#1f2937",
            color: "white",
            padding: 20,
            borderRadius: 10,
          }}
        >
          <h2>Model</h2>
          <h3>llama3.2</h3>
        </div>
      </div>
    </div>
  );
}