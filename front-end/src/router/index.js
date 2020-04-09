import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import BlogPage from '@/components/blogPage'
import Archive from '@/components/archive'
import AboutMe from '@/components/aboutMe'
import markdownEditor from '@/components/markdownEditor'
import Blog from '@/components/Blog'
Vue.use(Router);
const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },

    {
      path: '/login',
      name: 'Login',
      component: Login
    },

    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/blogPage',
      name: 'blogPage',
      component: BlogPage,
    },
    {
      path: '/archive',
      name: 'archive',
      component: Archive,
    },
    {
      path: '/aboutMe',
      name: 'aboutMe',
      component: AboutMe,
    },
    {
      path: '/editBlog',
      name: 'markdownEditor',
      component: markdownEditor,
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog,
    }
  ]

});


// 导航守卫控制路由的重定向，路由跳转时会经过该函数判断
// 比如，登录过后就去不到Login界面了，有的网站要求一定要登陆才能继续接下来的操作也可以在这里实现逻辑
// https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#导航守卫
router.beforeEach((to, from, next) => {
  const token = window.localStorage.getItem('blog-token');
  if (token && to.name == 'Login') {
    // 用户已登录，但又去访问登录页面时不让他过去
    next({
      path: from.fullPath
    })
  } else if (to.matched.length === 0) {  // 要前往的路由不存在时
    if (from.name) {
      next({
        name: from.name  //回到原来的路由
      })
    } else {
      next({
        path: '/' //回到主界面
      })
    }
  } else {
    next()
  }
});


export default router
