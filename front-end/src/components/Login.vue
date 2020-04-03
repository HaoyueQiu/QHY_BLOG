<template>
  <div>
    <img src="../assets/logo.png">
    <el-row>
      <el-col :span="8">
        <p></p>
        <el-button
          plain
          @click="openError"
          v-show="false">
        </el-button>
      </el-col>
      <el-col :span="8">
        <el-form ref="registerForm" :model="loginForm" :rules="rules" label-width="80px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input placeholder="请输入密码" v-model="loginForm.password" show-password></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">登录</el-button>
            <el-button @click="clearForm">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="8">
      </el-col>
    </el-row>
    <p> New User?
      <router-link to="/register">Click to Register!</router-link>
    </p>
    <p>
      Forgot your password?
      <!--重置密码功能-->
      <a href="#">Click to Reset It!</a>
    </p>
  </div>
</template>

<script>
  import store from '../store.js'

  export default {
    data() {
      return {
        loginForm: {
          name: '',
          username: '',
          email: '',
          password: '',
          errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
          passwordError: null,
        },
        rules: {
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ],
          username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'}
          ],
        }
      }
    },
    methods: {
      openError() {
        this.$notify({
          title: '警告',
          message: this.LoginForm.passwordError,
          type: 'warning',
          duration: 3000,
        });
      },
      onSubmit(e) {
        //通过 axios 连接前后端，能够调用后端API，以下实现了auth，获得token
        const path = '/tokens';
        // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
        this.$axios.post(path, {}, {
          auth: {
            'username': this.loginForm.username,
            'password': this.loginForm.password,
          }
        }).then((response) => {
          //handle success;
          window.localStorage.setItem('blog-token', response.data.token);
          store.state.username = this.loginForm.username;
          //虚假权限管理，后期修改！
          if (this.loginForm.username == "root") {
            store.state.authority = true;
          }
          store.loginAction();
          this.$router.push({path: '/'})
          //this.$router.push({path:`/profile${this.loginForm.username}`})
        })
          .catch((error) => {
            //handle error
            this.loginForm.passwordError = '密码错误 password Error!';
            this.openError();
            console.log(error.response);
          })
      },
      clearForm() {
        this.loginForm.username = '';
        this.loginForm.password = '';
      }
    }
  }
</script>
