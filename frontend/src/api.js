import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api =axios.create({
    baseURL: import.meta.env.VITE_API_URL,  //use the API URL from environment variables
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);  //get the access token from local storage
        if (token) {
            config.headers["Authorization"] = `Bearer ${token}`;  //add the token to the Authorization header
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
)

export default api;