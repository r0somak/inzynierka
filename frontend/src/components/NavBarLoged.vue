<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand tag="h1" class="mb-0">MEDIVI</b-navbar-brand>
      <b-nav-text>Jesteś zalogowany jako {{ username }}</b-nav-text>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-navbar-nav>
            <b-nav-item href="/">Strona główna</b-nav-item>
            <b-nav-item href="/visit" v-if="flaga  === true">Umów wizytę</b-nav-item>
          </b-navbar-nav>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>Twoje konto</em>
            </template>
            <b-dropdown-item href="/editprofile">Edytuj dane</b-dropdown-item>
            <b-dropdown-item href="/visitlist" v-if="flaga  === true">Twoje wizyty</b-dropdown-item>
            <b-dropdown-item href="/visitlist" v-else>Wizyty</b-dropdown-item>
            <b-dropdown-item-button @click="logOut">Wyloguj się
            </b-dropdown-item-button>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>O nas</em>
            </template>
            <b-dropdown-item href="#">Kontakt</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NavBarLoged',
  data() {
    return {
      username: '',
      flaga: '',
    };
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    fetchUserDetails() {
      const { username, flaga } = this;
      const data = {
        username, flaga,
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
          this.flaga = res.data.flaga;
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
  .navbar-brand {
    font-size: 1.75rem;
    font-style: italic;
    font-weight: bold;
  }

</style>
