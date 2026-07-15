import axios from "axios";

const api = axios.create({
  baseURL: "https://aquatic-territory-scoop-washer.trycloudflare.com",
});

export default api;