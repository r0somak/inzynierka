<template>
  <div class="register">
    <NavBar/>
    <div class="form">
      <p><b>Rejestracja</b></p>
    <RegisterForm/>
  </div>
    <div class="backgroundimage">
      <BackgroundImageHalf/>
    </div>
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue';
import BackgroundImageHalf from '@/components/BackgroundImageHalf.vue';
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'Register',
  components: {
    NavBar,
    RegisterForm,
    BackgroundImageHalf,
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap');
  .nav {
    padding: 30px;
    text-align: right;
    font-size: 25px;
    font-family: 'Source Sans Pro', sans-serif;
    a {
      font-weight: bold;
      color: black;
      text-decoration: none;
      padding: 10px;

      &.router-link-exact-active {
        color: royalblue;
      }
    }
    @media (max-width: 1400px){
      font-size: 20px;
      a {
        padding: 5px;
      }
    }
    @media (max-width: 920px){
      font-size: 17px;
    }
    @media (max-width: 800px){
      font-size: 12px;
      a {
        padding: 5px;
      }
    }
    @media (max-width: 650px){
      font-size: 8px;
      a {
        padding: 5px;
      }
    }
  }
  p {
    margin-top: 100px;
    font-size: 35px;
    font-family: 'Source Sans Pro', sans-serif;
    @media (max-width: 1400px) {
      font-size: 25px;
    }
    @media (max-width: 920px) {
      font-size: 20px;
    }
    @media (max-width: 790px) {
      font-size: 15px;
    }
    @media (max-width: 650px) {
      font-size: 10px;
    }
  }
  .form {
    float:right;
    width:50%;
  }
  #BackgroundImageHalf {
    float:left;
    width:50%;
  }

</style>
