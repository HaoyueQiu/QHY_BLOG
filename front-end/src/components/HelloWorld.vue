<template>
  <div>
    <p>{{msg}}</p>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name:'test',
    data(){
      return{
        msg:'Hello World',
      }
    },
    methods:{
      testBackEnd(){
        const path='http://localhost:5000/api/test'
      axios.get(path)
        .then((res)=>{
          this.msg=res.data;
        })
        .catch((error)=>{
          console.log(error)
        })
      }
    },
    created() {
      this.testBackEnd();
    }
  }
</script>
