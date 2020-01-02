<template>
  <div class="visit">
    <NavBarLoged/>
    <div class="form">
      <p><b>Twoje wizyty</b></p>
      <VisitView v-if="flaga  === true"/>
      <VisitViewDoc v-else/>
    </div>
    <div class="backgroundimage">
      <BackgroundImageLong/>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import BackgroundImageLong from '@/components/BackgroundImageLong.vue';
import VisitView from '@/components/VisitView.vue';
import VisitViewDoc from '@/components/VisitViewDoc.vue';
import NavBarLoged from '@/components/NavBarLoged.vue';


export default {
  name: 'VisitList',
  components: {
    BackgroundImageLong,
    VisitView,
    VisitViewDoc,
    NavBarLoged,
  },
  data() {
    return {
      flaga: '',
    };
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    fetchUserDetails() {
      const { flaga } = this;
      const data = {
        flaga,
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
          this.flaga = res.data.flaga;
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
    margin-top: 50px;
    font-size: 35px;
    font-family: 'Source Sans Pro', sans-serif;
    @media (max-width: 1400px) {
      font-size: 25px;
    }
    @media (max-width: 920px) {
      font-size: 20px;
    }
    @media (max-width: 800px) {
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
