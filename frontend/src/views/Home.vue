<template>
  <div class="home">
    <div class="nav">
      <div class="logo">
      <a>MediVi</a>
      </div>
      <div class="links">
      <router-link to="/">Strona główna</router-link>
      <router-link to="/login">Logowanie</router-link>
      <router-link to="/register">Rejestracja</router-link>
      </div>
    </div>
    <BackgroundImage />
    <div class="divek"/>
  </div>
</template>

<script>
import BackgroundImage from '@/components/BackgroundImage.vue';


export default {
  name: 'home',
  components: {
    BackgroundImage,
  },
};
</script>

<style lang="scss" scoped>
  .divek {
    height:800px;
    background-color:white;
  }
  .logo,.links {
    width:50%;
  }
   .logo {
    float: left;
     text-align: left;
     font-size: 35px;
     padding: 0px;
  }
  .links, {
    float:right;
  }

  .nav {
    height: 100px;
    padding: 30px;
    font-size: 25px;
    font-family: 'Abril Fatface', cursive;
    position: sticky;
    display:block;
    top: 0;
    z-index:10000;
    bottom:0;

    a {
      font-weight: bold;
      color: black;
      text-decoration: none;
      padding: 10px;

      &.router-link-exact-active {
        color: royalblue;
      }
    }

    @media (max-width: 700px) {
      font-size: 20px;
    }
    @media (max-width: 500px) {
      font-size: 15px;
      a {
        padding: 5px;
      }
    }
    #BackgroumdImage {
      position:absolute;
    }
  }
</style>
