import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
    const [system, setSystem] = useState<any>(null);

    useEffect(() => {
        api.get("/system/info")
            .then((res) => {
                console.log("API Response:", res.data);
                setSystem(res.data);
            })
            .catch((err) => {
                console.error("API Error:", err);
            });
    }, []);

    return (
        <div className="dashboard">

            <div className="card">
                <h3>System</h3>
                <h1>{system ? system.status : "Loading..."}</h1>
            </div>

            <div className="card">
                <h3>Engine</h3>
                <h1>{system ? system.engine : "--"}</h1>
            </div>

            <div className="card">
                <h3>Version</h3>
                <h1>{system ? system.version : "--"}</h1>
            </div>

            <div className="card">
                <h3>Name</h3>
                <h1>{system ? system.name : "--"}</h1>
            </div>

        </div>
    );
}