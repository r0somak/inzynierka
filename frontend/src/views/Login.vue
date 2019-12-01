<template>
  <div class="login">
    <div class="nav">
      <router-link to="/">Strona główna</router-link>
      <router-link to="/login">Logowanie</router-link>
      <router-link to="/register">Rejestracja</router-link>
          </div>
      <div class="form">
        <LoginForm />
      </div>
    <BackgroundImageHalf />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue';
import BackgroundImageHalf from '@/components/BackgroundImageHalf.vue';

export default {
  components: {
    LoginForm,
    BackgroundImageHalf,
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');

  h3 {
    padding: 30px;
    text-align: center;
    font-size: 35px;
    font-family: 'Abril Fatface', cursive;
  }
  .nav {
    padding: 0px;
    text-align: left;
    font-size: 25px;
    font-family: 'Abril Fatface', cursive;
    top:0px;
    position: sticky;
    a {
      font-weight: bold;
      color: black;
      text-decoration: none;
      padding: 10px;
      float:right;

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
  .form {
    width: 100%;
    display: flex;
    justify-content: right;
    float: right;
  }
  .backgroundImageHalf {
    justify-content: left;
    width: 100%;
  }

</style>
