import { motion } from "framer-motion";

export default function SplashScreen() {
  return (
    <motion.div
      initial={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.8 }}
      style={{
        position: "fixed",
        inset: 0,
        background:
          "radial-gradient(circle at center, #312e81 0%, #0f172a 45%, #020617 100%)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        zIndex: 99999,
        overflow: "hidden",
      }}
    >
      {/* Glow */}
      <motion.div
        animate={{
          scale: [1, 1.25, 1],
          opacity: [0.4, 0.9, 0.4],
        }}
        transition={{
          repeat: Infinity,
          duration: 3,
        }}
        style={{
          position: "absolute",
          width: 420,
          height: 420,
          borderRadius: "50%",
          background:
            "radial-gradient(circle,#3b82f6,#8b5cf6,transparent)",
          filter: "blur(100px)",
        }}
      />

      <motion.div
        initial={{
          opacity: 0,
          scale: 0.7,
          y: 40,
        }}
        animate={{
          opacity: 1,
          scale: 1,
          y: 0,
        }}
        transition={{
          duration: 1,
        }}
        style={{
          textAlign: "center",
          color: "white",
          zIndex: 10,
        }}
      >
        <motion.h1
          animate={{
            textShadow: [
              "0 0 15px #3b82f6",
              "0 0 45px #8b5cf6",
              "0 0 15px #3b82f6",
            ],
          }}
          transition={{
            repeat: Infinity,
            duration: 2,
          }}
          style={{
            fontSize: 70,
            fontWeight: 800,
            letterSpacing: 8,
            marginBottom: 15,
          }}
        >
          NYRION AI
        </motion.h1>

        <motion.p
          animate={{
            opacity: [0.4, 1, 0.4],
          }}
          transition={{
            repeat: Infinity,
            duration: 1.5,
          }}
          style={{
            fontSize: 20,
            color: "#cbd5e1",
            marginBottom: 35,
          }}
        >
          Initializing Neural Engine...
        </motion.p>

        <div
          style={{
            width: 350,
            height: 8,
            background: "#1e293b",
            borderRadius: 20,
            overflow: "hidden",
            margin: "auto",
          }}
        >
          <motion.div
            initial={{ width: 0 }}
            animate={{ width: "100%" }}
            transition={{
              duration: 2.5,
            }}
            style={{
              height: "100%",
              background:
                "linear-gradient(90deg,#3b82f6,#8b5cf6,#06b6d4)",
            }}
          />
        </div>

        <motion.p
          animate={{
            opacity: [0.5, 1, 0.5],
          }}
          transition={{
            repeat: Infinity,
            duration: 1.3,
          }}
          style={{
            marginTop: 20,
            color: "#94a3b8",
          }}
        >
          Powered by Ollama
        </motion.p>
      </motion.div>
    </motion.div>
  );
}