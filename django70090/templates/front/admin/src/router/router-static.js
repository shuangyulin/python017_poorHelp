import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import zizhushenqing from '@/views/modules/zizhushenqing/list'
    import qingongjianxue from '@/views/modules/qingongjianxue/list'
    import xuesheng from '@/views/modules/xuesheng/list'
    import zizhuxiangmu from '@/views/modules/zizhuxiangmu/list'
    import zizhufafang from '@/views/modules/zizhufafang/list'
    import gangweishenqing from '@/views/modules/gangweishenqing/list'
    import yuanxiao from '@/views/modules/yuanxiao/list'
    import pinkunshenqing from '@/views/modules/pinkunshenqing/list'
    import daikuanshenqing from '@/views/modules/daikuanshenqing/list'
    import daikuanfafang from '@/views/modules/daikuanfafang/list'
    import config from '@/views/modules/config/list'


//2.配置路由   注意：名字
const routes = [{
    path: '/index',
    name: '首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '首页',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '校园资讯',
        component: news
      }
      ,{
	path: '/zizhushenqing',
        name: '资助申请',
        component: zizhushenqing
      }
      ,{
	path: '/qingongjianxue',
        name: '勤工俭学',
        component: qingongjianxue
      }
      ,{
	path: '/xuesheng',
        name: '学生',
        component: xuesheng
      }
      ,{
	path: '/zizhuxiangmu',
        name: '资助项目',
        component: zizhuxiangmu
      }
      ,{
	path: '/zizhufafang',
        name: '资助发放',
        component: zizhufafang
      }
      ,{
	path: '/gangweishenqing',
        name: '岗位申请',
        component: gangweishenqing
      }
      ,{
	path: '/yuanxiao',
        name: '院校',
        component: yuanxiao
      }
      ,{
	path: '/pinkunshenqing',
        name: '贫困申请',
        component: pinkunshenqing
      }
      ,{
	path: '/daikuanshenqing',
        name: '贷款申请',
        component: daikuanshenqing
      }
      ,{
	path: '/daikuanfafang',
        name: '贷款发放',
        component: daikuanfafang
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: '首页',
    redirect: '/index'
  }, /*默认跳转路由*/
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})

export default router;
