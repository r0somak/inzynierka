<template>
<div>
  <NavBarLoged/>
  <VisitDetailsDocCard v-if="flaga  === false"/>
  <VisitDetailsPatCard v-else/>
</div>
</template>

<script>
import axios from 'axios';
import NavBarLoged from '../components/NavBarLoged.vue';
import VisitDetailsDocCard from '../components/VisitDetailsDocCard.vue';
import VisitDetailsPatCard from '../components/VisitDetailsPatCard.vue';

export default {
  name: 'VisitDetails',
  components: {
    VisitDetailsPatCard,
    NavBarLoged,
    VisitDetailsDocCard,
  },
  data() {
    return {
      flaga: '',
    };
  },
  mounted() {
    this.fetchUserFlag();
  },
  methods: {
    fetchUserFlag() {
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

<style scoped>

</style>
