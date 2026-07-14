import {
  LayoutDashboard,
  Search,
  MessageSquare,
  Database,
  BarChart3,
  Settings,
} from "lucide-react";

const menu = [
  { icon: LayoutDashboard, title: "Dashboard" },
  { icon: Search, title: "Search" },
  { icon: MessageSquare, title: "Chat" },
  { icon: Database, title: "Database" },
  { icon: BarChart3, title: "Benchmark" },
  { icon: Settings, title: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <h2 className="logo">NYRION</h2>

      {menu.map((item) => (
        <div className="menu-item" key={item.title}>
          <item.icon size={20} />
          <span>{item.title}</span>
        </div>
      ))}
    </aside>
  );
}