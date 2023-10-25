const base = {
    get() {
        return {
            url : "http://localhost:8080/django70090/",
            name: "django70090",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "贫困生资助管理系统"
        } 
    }
}
export default base
