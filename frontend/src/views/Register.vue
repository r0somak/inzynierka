<template>
  <div class="register">
  <div class="nav">
    <router-link to="/">Strona główna</router-link>
    <router-link to="/login">Logowanie</router-link>
    <router-link to="/register">Rejestracja</router-link>
  </div>
  <p>REJESTRACJA</p>
    <RegisterForm/>
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue';

export default {
  name: 'Register',
  components: {
    RegisterForm,
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  .nav {
    padding: 30px;
    text-align: right;
    font-size: 25px;
    font-family: 'Abril Fatface', cursive;
  a {
    font-weight: bold;
    color: black;
    text-decoration: none;
    padding: 10px;

  &.router-link-exact-active {
     color: royalblue;
   }
  }
  @media (max-width: 700px){
    font-size: 20px;
  }
  @media (max-width: 500px){
    font-size: 15px;
    a {
      padding: 5px;
    }
  }
  }
  p {
    font-size: 35px;
    font-family: 'Abril Fatface', cursive;
  }

</style>
