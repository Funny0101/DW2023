import axios from "axios";
import { Message } from "element-ui";

let BASE_URL = "http://localhost:5000/";

// create an axios instance
const my_axios = axios.create({
  baseURL: BASE_URL,
  timeout: 200000, // request timeout
});

// request interceptor
my_axios.interceptors.request.use(
  (config) => {
    // do something before request is sent
    console.log(config);
    // if (config.url.includes("spark")) {
    //   let baseURL = "http://localhost:5000/";
    //   config.baseURL = baseURL;
    // }
    if (config.url.includes("hive")) {
      let baseURL = "http://localhost:7777/";
      config.baseURL = baseURL;
    }
    else if (config.url.includes("neo4j")) {
      let baseURL = "http://localhost:5555/";
      config.baseURL = baseURL;
    }
    return config;
  },
  (error) => {
    // do something with request error
    console.log(error); // for debug
    return Promise.reject(error);
  }
);

// response interceptor
my_axios.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
   */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  (response) => {
    const res = response.data;
    console.log(res);
    return res;
  },
  (error) => {
    console.log("err" + error); // for debug
    Message({
      message: error.message,
      type: "error",
      duration: 5 * 1000,
    });
    return Promise.reject(error);
  }
);

export default my_axios;
