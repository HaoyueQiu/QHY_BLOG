import Vue from 'vue'
import App from './App'
import router from './router'
import axios from './http'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import 'markdown-it-katex'

//阻止显示生产模块的消息
Vue.config.productionTip = false;

// 将 $moment 挂载到 prototype 上，在组件中可以直接使用 this.$moment 访问
//Vue.prototype.$moment = moment
// 将 $axios 挂载到 prototype 上，在组件中可以直接使用 this.$axios 访问
Vue.prototype.$axios = axios;

Vue.use(VueRouter);
Vue.use(ElementUI);
Vue.use(mavonEditor);

let mk = require('markdown-it-katex');
mavonEditor.markdownIt.use(mk);

/*
在js中new 一个对象，需要返回赋值给某个变量
但用Vue实例化的时候却不需要赋值给变量
防止报错，单独配一条规则，加这个注释代表跳过这行代码的校验
 */
/* eslint-disable no-new */
new Vue({
  /*el:为实例提供挂载元素
  挂载（mounting）是指由操作系统使一个存储设备上的计算机文件和目录可供用户通过计算机的文件系统访问的一个过程。
  挂载使文件和目录能够通过文件系统被索引，所以el可以理解为类似id的东西。
  */
  el: '#app',//最终效果会被替换成页面中id为app的div元素，id绑定
  router,//使用路由
  components: {App},//当前页面想使用的组件名称
  template: '<App/>',//使用的组件应当用这个标签去包裹
  render: h => h(App)
});





