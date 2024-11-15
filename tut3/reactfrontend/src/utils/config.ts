import axios from "axios";

export const baseurl = import.meta.env.VITE_API_BASE_URL;

axios.defaults.baseURL = baseurl;
axios.defaults.headers.common["Authorization"] = "Bearer your-token";