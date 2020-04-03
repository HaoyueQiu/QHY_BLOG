<template>
  <div>
    <el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">首页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">行为识别</template>
        <el-menu-item index="2-4">行为识别</el-menu-item>
        <el-menu-item index="2-1">基于骨架的行为识别</el-menu-item>
        <el-menu-item index="2-2">基于视频的行为识别</el-menu-item>
        <el-menu-item index="2-3">计算机视觉基础网络</el-menu-item>
      </el-submenu>
      <el-menu-item index="3">前端</el-menu-item>
      <el-menu-item index="4">生活</el-menu-item>
      <el-menu-item index="5">归档</el-menu-item>
      <el-menu-item index="6">关于博主</el-menu-item>
      <el-menu-item v-if="store.state.is_authenticated" index="7">登出</el-menu-item>
      <el-menu-item v-else index="7">登录/注册</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  import store from '../store.js'
  export default {
    name: "Navbar",
    data() {
      return {
        activeIndex: '1',
        navigationBar:{'1':'首页','2-1':'基于骨架的行为识别','2-2':'基于视频的行为识别','2-3':'CV基础网络',
          '3':'前端','4':'生活','5':'归档','6':'关于博主'},
        store:store,
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        this.activeIndex = keyPath[0];
        switch (key) {
          case '1':
            this.$router.push({path: '/'});
            break;
          case '2-1':
          case '2-2':
          case '2-3':
          case '2-4':
          case '3':
          case '4':
            this.$router.push({path: '/blogPage',params:{'key':key}});
            break;
          case '5':
            this.$router.push({path: '/archive'});
            break;
          case '6':
            this.$router.push({path:'aboutMe'});
            break;
          case '7':
            store.logoutAction();
            if(store.state.is_authenticated){
              store.logoutAction();
            }else{
              console.log('enter login');
              this.$router.push({path:'/login'});
            }
            this.store = store;
            break;
          default:
            break;
        }
      }
    }
  }
</script>

<style scoped>

</style>
