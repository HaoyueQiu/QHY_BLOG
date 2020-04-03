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

        <!--  ref的作用  https://www.jianshu.com/p/623c8b009a85-->
        <!-- 表单验证Vue组件库element-ui中的Form表单组件提供了表单验证功能
              通过rules属性传入验证规则
              Form-Item中的prop属性设置需要校验的字段名
        -->
        <el-form ref="registerForm" :model="registerForm" :rules="rules" label-width="80px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="registerForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input placeholder="请输入密码" v-model="registerForm.password" show-password></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input
              placeholder="请输入邮箱"
              v-model="registerForm.email"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
          </el-form-item>
        </el-form>

      </el-col>
      <el-col :span="8">
      </el-col>
    </el-row>

  </div>
</template>

<script>
  export default {
    data() {
      let checkEmail = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if (!value) {
          return callback(new Error('邮箱不能为空'))
        }
        setTimeout(() => {
          if (mailReg.test(value)) {
            callback()
          } else {
            callback(new Error('请输入正确的邮箱格式'))
          }
        }, 100)
      };
      return {
        registerForm: {
          name: '',
          username: '',
          email: '',
          password: '',
          errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
          createError: null,
        },
        rules: {
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ],
          username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'}
          ],
          email: [
            //触发方式，blur失去焦点，change数据改变
            {validator: checkEmail, trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      openError() {
        this.$notify({
          title: '警告',
          message: this.registerForm.createError,
          type: 'warning',
          duration: 3000,
        });
      },
      onSubmit(e) {

        const path = '/users';
        const payload = {
          username: this.registerForm.username,
          email: this.registerForm.email,
          password: this.registerForm.password
        };
        console.log(payload);
        this.$axios.post(path, payload)
          .then((response) => {
            // 成功注册，跳转到login界面
            console.log(response.data);
            this.$router.push('/login')
          })
          .catch((error) => {
            this.createError = null
            // handle error
            console.log(error.response.data.message);
            for (let field in error.response.data.message) {
              if (field == 'username') {
                this.createError = error.response.data.message.username
                this.openError()
              } else if (field == 'email') {
                this.createError = error.response.data.message.email
                this.openError()
              }
            }
            console.log(this.createError)

          })
      },
    }
  }
</script>
