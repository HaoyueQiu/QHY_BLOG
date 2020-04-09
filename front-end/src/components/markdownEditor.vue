<template>
  <div id="main">
    <mavon-editor v-model="content" ref="md" @imgAdd="$imgAdd" @imgDel="$imgDel"></mavon-editor>
  </div>
</template>

<script>
  export default {
    name: "markdownEditor",
    data() {
      return {
        content: '',
        html: '',
        configs: {}

      }
    },
    methods: {
      // 将图片上传到服务器，返回地址替换到md中
      $imgAdd(pos, $file) {
        // // 第一步.将图片上传到服务器.
        // let formdata = new FormData();
        // formdata.append('image', $file);
        // this.$axios({
        //   url: 'server url',
        //   method: 'post',
        //   data: formdata,
        //   headers: {'Content-Type': 'multipart/form-data'},
        // }).then((url) => {
        //   // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)
        //   // $vm.$img2Url 详情见本页末尾
        //   $vm.$img2Url(pos, url);
        // })
        // $vm.$img2Url(pos, 'static/img/Login.png')
        console.log(this.refs.md.markdownIt)
      },
      // 所有操作都会被解析重新渲染
      $imgDel(pos) {
        delete this.img_file[pos];
      },
      // 提交
      submit() {
        console.log(this.content);
        console.log(this.html);
        this.$message.success('提交成功，已打印至控制台！');
      }
    },
  }
</script>

<style scoped>

</style>
