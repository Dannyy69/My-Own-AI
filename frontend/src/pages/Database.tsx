import { useEffect, useState } from "react";
import api from "../services/api";

type Document = {
  id: number;
  filename: string;
  chunks: number;
  size: number;
};

export default function Database() {
  const [documents, setDocuments] = useState<Document[]>([]);

  async function loadDocuments() {
    try {
      const res = await api.get("/documents");
      setDocuments(res.data.documents);
    } catch (err) {
      console.error(err);
    }
  }

  async function deleteDocument(id: number) {
    try {
      await api.delete(`/documents/${id}`);
      loadDocuments();
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    loadDocuments();
  }, []);

  return (
    <div style={{ padding: 30 }}>
      <h1>Database</h1>

      <h3>{documents.length} Documents Uploaded</h3>

      <div style={{ marginTop: 25 }}>
        {documents.length === 0 && (
          <p>No uploaded documents.</p>
        )}

        {documents.map((doc) => (
          <div
            key={doc.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              background: "#1f2937",
              color: "white",
              padding: 18,
              borderRadius: 10,
              marginBottom: 15,
            }}
          >
            <div>
              <h3>{doc.filename}</h3>

              <p>Chunks: {doc.chunks}</p>

              <p>Characters: {doc.size}</p>
            </div>

            <button
              onClick={() => deleteDocument(doc.id)}
              style={{
                background: "#dc2626",
                color: "white",
                border: "none",
                padding: "10px 18px",
                borderRadius: 8,
                cursor: "pointer",
              }}
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}