import AnimatedBackground from "../components/AnimatedBackground";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";

export default function MainLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <AnimatedBackground />

      <Sidebar />

      <main className="main-content">
        <Topbar />

        {children}
      </main>
    </>
  );
}