<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/github-markdown-css/2.2.1/github-markdown.css"/>

    <mavon-editor
      class="md"
      :value="content"
      :subfield="false"
      :defaultOpen="'preview'"
      :toolbarsFlag="false"
      :editable="false"
      :scrollStyle="true"
      :ishljs="true"
    ></mavon-editor>
  </div>
</template>

<script>
  export default {
    name: "Blog",
    data() {
      return {
        content: ''
      }
    },
    methods: {
      $imgAdd(pos, $file) {
        // 第一步.将图片上传到服务器.
        let formdata = new FormData();
        formdata.append('image', $file);
        this.$axios({
          url: '/',
          method: 'post',
          data: formdata,
          headers: {'Content-Type': 'multipart/form-data'},
        }).then((url) => {
          // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)
          // $vm.$img2Url 详情见本页末尾
          $vm.$img2Url(pos, url);
        })
      },
    },
    created() {
      // this.content = '# hi ![skeleton](http://127.0.0.1:8800/CVPR%202018%20DGNN/skeleton%20pic.jpg) 作识别任务，使用自适应的DGN模块(Adaptive DGN block)使得图的拓扑结构可以根据训练过程进行自适应地改变。如原始的是相连点的边权都为1，不相连点的边权为0，现在这些边权可以在训练过程中被改变。\n';
      // this.content = '![点击查看源网页](https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3173584241,3533290860&fm=26&gp=0.jpg)'
      // console.log(this.content)
      const path = '/blogs';
      this.$axios.get(path, {})
        .then(response => {
          // console.log(response.data);
          // this.content = '# hello!';
          // this.content = '#hi ![skeleton](http://127.0.0.1:8800/CVPR 2018 DGNN/skeleton pic.jpg) 作识别任务，使用自适应的DGN模块(Adaptive DGN block)使得图的拓扑结构可以根据训练过程进行自适应地改变。如原始的是相连点的边权都为1，不相连点的边权为0，现在这些边权可以在训练过程中被改变。\n';
          // console.log(this.content)
          this.content = response.data.content

        })
    }
  }
</script>

<style scoped>

</style>
