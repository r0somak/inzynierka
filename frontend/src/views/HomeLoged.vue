<template>
<div>
  <p>homeloged</p>
  <p>Witaj {{ name }} {{ wojewodztwo }} {{ id }}!</p>
  <button @click="logOut">Wyloguj się</button>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeLoged',
  data() {
    return {
      wojewodztwo: '',
      name: '',
      id: '',
    };
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    fetchUserDetails() {
      const { name, wojewodztwo, id } = this;
      const data = {
        name,
        wojewodztwo,
        id,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/patient/profile/';
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
          console.log(res.data);
          this.wojewodztwo = res.data.wojewodztwo;
          this.name = res.data.name;
          this.id = res.data.id;
        })
        .catch((err) => {
          // eslint-disable-next-line
          console.log(err)
        });
    },
    logOut() {
      const token = sessionStorage.getItem('token');
      const URL = 'http://http://localhost:8000/users/patient/profile/';
      axios({
        method: 'get',
        url: URL,
        headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${token}`,
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

<style scoped>

</style>
