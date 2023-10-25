
var projectName = '贫困生资助管理系统';
/**
 * 轮播图配置
 */
var swiper = {
	// 设定轮播容器宽度，支持像素和百分比
	width: '100%',
	height: '400px',
	// hover（悬停显示）
	// always（始终显示）
	// none（始终不显示）
	arrow: 'none',
	// default（左右切换）
	// updown（上下切换）
	// fade（渐隐渐显切换）
	anim: 'default',
	// 自动切换的时间间隔
	// 默认3000
	interval: 2000,
	// 指示器位置
	// inside（容器内部）
	// outside（容器外部）
	// none（不显示）
	indicator: 'outside'
}

/**
 * 个人中心菜单
 */
var centerMenu = [{
	name: '个人中心',
	url: '../' + localStorage.getItem('userTable') + '/center.html'
}, 
]


var indexNav = [

{
	name: '资助项目',
	url: './pages/zizhuxiangmu/list.html'
}, 
{
	name: '勤工俭学',
	url: './pages/qingongjianxue/list.html'
}, 

{
	name: '校园资讯',
	url: './pages/news/list.html'
},
]

var adminurl =  "http://localhost:8080/django70090/admin/dist/index.html";

var cartFlag = false

var chatFlag = false




var menu = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-pay","buttons":["新增","查看","修改","删除","报表","导出"],"menu":"学生","menuJump":"列表","tableName":"xuesheng"}],"menu":"学生管理"},{"child":[{"appFrontIcon":"cuIcon-medal","buttons":["新增","查看","修改","删除"],"menu":"院校","menuJump":"列表","tableName":"yuanxiao"}],"menu":"院校管理"},{"child":[{"appFrontIcon":"cuIcon-clothes","buttons":["查看","删除","报表","审核","导出"],"menu":"贫困申请","menuJump":"列表","tableName":"pinkunshenqing"}],"menu":"贫困申请管理"},{"child":[{"appFrontIcon":"cuIcon-vip","buttons":["新增","查看","修改","删除"],"menu":"资助项目","menuJump":"列表","tableName":"zizhuxiangmu"}],"menu":"资助项目管理"},{"child":[{"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看","删除","审核","报表","发放","导出"],"menu":"资助申请","menuJump":"列表","tableName":"zizhushenqing"}],"menu":"资助申请管理"},{"child":[{"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看","修改","删除","导出","报表"],"menu":"资助发放","menuJump":"列表","tableName":"zizhufafang"}],"menu":"资助发放管理"},{"child":[{"appFrontIcon":"cuIcon-paint","buttons":["新增","查看","修改","删除"],"menu":"勤工俭学","menuJump":"列表","tableName":"qingongjianxue"}],"menu":"勤工俭学管理"},{"child":[{"appFrontIcon":"cuIcon-camera","buttons":["查看","删除","审核","报表","导出"],"menu":"岗位申请","menuJump":"列表","tableName":"gangweishenqing"}],"menu":"岗位申请管理"},{"child":[{"appFrontIcon":"cuIcon-taxi","buttons":["查看","删除","审核","发放","导出"],"menu":"贷款申请","menuJump":"列表","tableName":"daikuanshenqing"}],"menu":"贷款申请管理"},{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["查看","删除","修改","导出"],"menu":"贷款发放","menuJump":"列表","tableName":"daikuanfafang"}],"menu":"贷款发放管理"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"校园资讯","tableName":"news"},{"appFrontIcon":"cuIcon-skin","buttons":["查看","修改","删除"],"menu":"轮播图管理","tableName":"config"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","申请"],"menu":"资助项目列表","menuJump":"列表","tableName":"zizhuxiangmu"}],"menu":"资助项目模块"},{"child":[{"appFrontIcon":"cuIcon-goods","buttons":["查看","申请"],"menu":"勤工俭学列表","menuJump":"列表","tableName":"qingongjianxue"}],"menu":"勤工俭学模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-clothes","buttons":["新增","查看","修改","删除"],"menu":"贫困申请","menuJump":"列表","tableName":"pinkunshenqing"}],"menu":"贫困申请管理"},{"child":[{"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看","修改"],"menu":"资助申请","menuJump":"列表","tableName":"zizhushenqing"}],"menu":"资助申请管理"},{"child":[{"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看"],"menu":"资助发放","menuJump":"列表","tableName":"zizhufafang"}],"menu":"资助发放管理"},{"child":[{"appFrontIcon":"cuIcon-camera","buttons":["查看","修改"],"menu":"岗位申请","menuJump":"列表","tableName":"gangweishenqing"}],"menu":"岗位申请管理"},{"child":[{"appFrontIcon":"cuIcon-taxi","buttons":["新增","查看","修改","删除"],"menu":"贷款申请","menuJump":"列表","tableName":"daikuanshenqing"}],"menu":"贷款申请管理"},{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["查看"],"menu":"贷款发放","menuJump":"列表","tableName":"daikuanfafang"}],"menu":"贷款发放管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","申请"],"menu":"资助项目列表","menuJump":"列表","tableName":"zizhuxiangmu"}],"menu":"资助项目模块"},{"child":[{"appFrontIcon":"cuIcon-goods","buttons":["查看","申请"],"menu":"勤工俭学列表","menuJump":"列表","tableName":"qingongjianxue"}],"menu":"勤工俭学模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"学生","tableName":"xuesheng"}]


var isAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].backMenu.length;j++){
                for(let k=0;k<menus[i].backMenu[j].child.length;k++){
                    if(tableName==menus[i].backMenu[j].child[k].tableName){
                        let buttons = menus[i].backMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}

var isFrontAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}
