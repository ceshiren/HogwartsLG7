// 修改from地址，引用http.js的实例
import axios from "./http";
// 定义具体的接口，通过不同的函数
const testcase = {
    selectTescase(){
        // 第一个参数是path， 后面的是其他的请求信息
        return axios("/testcase_orm", {
            "method": "get"
        })
    },
    // 添加用例
    addTestcase(params){
        return axios("/testcase_orm", {
            "method": "post",
            // 传递请求体
            data: params
        })    
    }
}
export default testcase