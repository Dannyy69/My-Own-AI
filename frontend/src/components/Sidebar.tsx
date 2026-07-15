import {
  LayoutDashboard,
  Search,
  MessageSquare,
  Database,
  BookOpen,
  BarChart3,
  Settings,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menu = [
  {
    icon: LayoutDashboard,
    title: "Dashboard",
    path: "/",
  },
  {
    icon: Search,
    title: "Search",
    path: "/search",
  },
  {
    icon: MessageSquare,
    title: "Chat",
    path: "/chat",
  },
  {
    icon: Database,
    title: "Database",
    path: "/database",
  },
  {
    icon: BookOpen,
    title: "Knowledge",
    path: "/knowledge",
  },
  {
    icon: BarChart3,
    title: "Benchmark",
    path: "/benchmark",
  },
  {
    icon: Settings,
    title: "Settings",
    path: "/settings",
  },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <h2 className="logo">NYRION</h2>

      {menu.map((item) => (
        <NavLink
          key={item.title}
          to={item.path}
          className="menu-item"
          style={({ isActive }) => ({
            textDecoration: "none",
            color: "inherit",
            background: isActive ? "#1e3a8a" : "transparent",
            borderRadius: "10px",
            padding: "10px",
          })}
        >
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "10px",
            }}
          >
            <item.icon size={20} />
            <span>{item.title}</span>
          </div>
        </NavLink>
      ))}
    </aside>
  );
}