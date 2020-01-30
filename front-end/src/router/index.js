import Vue from 'vue'
import Router from 'vue-router'
import test from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'HelloWorld',
      component: test,
    },
  ]
})
