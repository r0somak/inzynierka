<template>
<div class="home">
  <div class="info">
      <a>Jesteś zalogowana jako {{ username }}</a>
  </div>
  <div class="nav">
    <div class="logo">
      <a>MediVi</a>
    </div>
    <div class="dropdown">
      <a>Twoje konto</a>
      <div class="dropdown-content">
        <router-link to="/editprofile">Edytuj dane</router-link>
      </div>
    </div>
    <div class="links">
      <router-link to="/homeloged">Strona główna</router-link>
      <router-link to="/visit">Umów wizytę</router-link>
    </div>
  </div>
  <BackgroundImage />
  <div class="divek"/>
</div>
</template>

<script>
import axios from 'axios';
import BackgroundImage from '@/components/BackgroundImage.vue';

export default {
  name: 'HomeLoged',
  components: {
    BackgroundImage,
  },
  data() {
    return {
      username: '',
    };
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    fetchUserDetails() {
      const { username } = this;
      const data = {
        username,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/user/main_profile/';
      console.log('TOKEN: {0}', token);
      axios({
        method: 'get',
        url: URL,
        headers: {
          Accept: 'application/json',
          Authorization: `Token ${token}`,
        },
        data,
      })
        .then((res) => {
          this.username = res.data.username;
        })
        .catch((err) => {
          // eslint-disable-next-line
          console.log(err)
        });
    },
    logOut() {
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/patient/profile/';
      axios({
        method: 'get',
        url: URL,
        headers: {
          Accept: 'application/json',
          Authorization: `Token ${token}`,
        },
      })
        .then(() => {
          sessionStorage.removeItem('token');
          this.$router.push('/login');
        })
        .catch((err) => {
          // eslint-disable-next-line
          console.log(err)
        });
    },
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  .info {
    width: 100%;
    font-size: 12px;
    font-family: 'Abril Fatface', cursive;
    position: sticky;
    display:block;
    top: 0;
    z-index:10000;
    bottom:0;
    a {
      margin: 10px 10px 0 0;
      float:right;
    }
    button {
      margin: 10px 10px 0 0;
      padding: 5px 20px 5px 20px;
      text-align: center;
      font-size: 12px;
      font-family: 'Abril Fatface', cursive;
      background-color: lightblue;
      border: 3px solid lightblue;
      border-radius: 40px;
      box-shadow: none;
      color: black;
    }
    button:focus {
      background-color: transparent;
      border: 3px solid lightblue;
      border-radius: 40px;
      color: black;
    }
  }
  .divek {
    height:800px;
    background-color:white;
  }
  .logo {
    width:40%;
  }
  .links
  {
    margin: 0 0 0 0;
    width:30%;
    float:right;
  }
  .dropdown {
    width:15%;
    float:right;
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 140px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    padding: 12px 16px;
    z-index: 1;
    font-size: 18px;
    border-radius: 40px;
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
  .logo {
    float: left;
    text-align: left;
    font-size: 35px;
    padding: 0px;
  }

  .nav {
    height: 100px;
    padding: 5px;
    font-size: 25px;
    font-family: 'Abril Fatface', cursive;
    position: sticky;
    display:block;
    top: 20px;
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
    #BackgroumdImage {
      position:absolute;
    }
  }
</style>
