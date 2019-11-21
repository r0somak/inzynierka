<template>
  <div class="login">
    <div class="nav">
      <router-link to="/">Strona główna</router-link>
      <router-link to="/login">Logowanie</router-link>
      <router-link to="/register">Rejestracja</router-link>
      <h3>Zaloguj się</h3>
      <div class="form">
        <LoginForm />
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue';

export default {
  components: {
    LoginForm,
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
  .form {
    margin-top: 50px;
    display: flex;
    justify-content: center;
  }

</style>
