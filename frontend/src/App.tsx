import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";

import Dashboard from "./pages/Dashboard";
import Chat from "./pages/Chat";
import Search from "./pages/Search";
import Database from "./pages/Database";
import Benchmark from "./pages/Benchmark";
import Settings from "./pages/Settings";
import Knowledge from "./pages/Knowledge";

import MainLayout from "./layouts/MainLayout";
import SplashScreen from "./components/SplashScreen";

export default function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false);
    }, 2600);

    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return <SplashScreen />;
  }

  return (
    <Routes>
      <Route
        path="/"
        element={
          <MainLayout>
            <Dashboard />
          </MainLayout>
        }
      />

      <Route
        path="/chat"
        element={
          <MainLayout>
            <Chat />
          </MainLayout>
        }
      />

      <Route
        path="/search"
        element={
          <MainLayout>
            <Search />
          </MainLayout>
        }
      />

      <Route
        path="/database"
        element={
          <MainLayout>
            <Database />
          </MainLayout>
        }
      />

      <Route
        path="/knowledge"
        element={
          <MainLayout>
            <Knowledge />
          </MainLayout>
        }
      />

      <Route
        path="/benchmark"
        element={
          <MainLayout>
            <Benchmark />
          </MainLayout>
        }
      />

      <Route
        path="/settings"
        element={
          <MainLayout>
            <Settings />
          </MainLayout>
        }
      />
    </Routes>
  );
}