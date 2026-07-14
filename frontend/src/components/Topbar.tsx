export default function Topbar() {
  return (
    <header className="topbar">
      <div>
        <h2>Nyrion AI</h2>
        <small>Semantic Intelligence Platform</small>
      </div>

      <input
        className="search-box"
        placeholder="Search everything..."
      />
    </header>
  );
}