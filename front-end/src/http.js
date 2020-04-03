import axios from 'axios'
import store from './store.js'

axios.defaults.timeout = 5000;
axios.defaults.baseURL = 'http://localhost:5000/api';
axios.interceptors.response.use(function (response) {
  // Do something with response data
  const token = window.localStorage.getItem('blog-token');
  if (token) {
    response.headers.Authorization = `Bearer ${token}`
  }
  return response
}, function (error) {
  // Do something with response error
  switch (error.response.status) {
    case 401:
      // 清除 Token 及 已认证 等状态
      store.logoutAction();
      // 跳转到登录页
      if (router.currentRoute.path !== '/login') {
        router.replace({
          path: '/login',
          query: {redirect: router.currentRoute.path},
        })
      }
      break;
    case 404:
      router.back();
      break
  }
  return Promise.reject(error)
});

export default axios
