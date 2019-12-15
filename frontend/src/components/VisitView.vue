<template>
  <div class="list">
    <div v-for="result in results" :key="result.id" class="results-data">
      <div class="results-stats">
        <div>
          <span>{{result.data_wizyty}}</span>
          <span>{{result.uwagi}}</span>
          <span>{{result.objawy}}</span>
          <span>{{result.fk_id_lekarz}}</span>
          <span>{{result.fk_id_przychodnia}}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VisitView',
  data() {
    return {
      results: [],
    };
  },
  mounted() {
    this.getVisits();
  },
  methods: {
    getVisits() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        results,
      } = this;
      const data = {
        results,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/wizyty/';
      axios({
        method: 'get',
        url: URL,
        headers: {
          Accept: 'application/json',
          Content: 'application/json',
          Authorization: `Token ${token}`,
        },
        data,
      })
        .then((res) => {
          console.log(res.data);
          this.results = res.data.results;
        });
    },
  },
};
</script>

<style lang="scss" scoped>
  span {
    color: black;
    display: block;
  }
  .results-stats {
    margin: 20px;
  }
</style>
