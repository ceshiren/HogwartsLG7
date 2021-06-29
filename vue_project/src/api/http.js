// http.js起到的作用类似于po中的basepage对通用接口操作进行封装
import axios from 'axios'

var instance = axios.create({
    headers: {
        'Content-Type':'application/json'
    },
    baseURL:'http://127.0.0.1:5000/'
})
 
export default instance