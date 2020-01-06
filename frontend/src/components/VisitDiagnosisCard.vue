<template>
  <div>
    <b-card
      no-body
      style="max-width: 25rem;"
      img-src="https://img.pngio.com/epidemiology-hepscreen-prevalence-png-809_680.png"
      img-alt="Image"
      img-top
      align="center"
    >
      <template v-slot:header>
        <h4 class="mb-0">Dane epidemiologiczne</h4>
      </template>

      <b-card-body>
        <b-card-text>
        </b-card-text>
      </b-card-body>
      <b-list-group flush>
        <div v-for="item in results" :key="item.nazwa">
        <b-list-group-item>
          Pokrycie: {{ item.pokrycie }}<br>
          Nazwa: {{ item.nazwa }}<br>
          Prewalencja: {{ item.prewalencja }}
        </b-list-group-item>
        </div>
      </b-list-group>

      <b-card-footer></b-card-footer>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VisitDiagnosisCard',
  data() {
    return {
      results: [],
      przekazanie_id: 0,
    };
  },
  created() {
    this.przekazanie_id = this.$route.params.id;
  },
  mounted() {
    this.getDiagnosis();
  },
  methods: {
    getDiagnosis() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase,max-len
        results,
      } = this;
      const data = {
        results,
      };
        // const { id } = this.$route.params;
      const token = localStorage.getItem('token');
      // const id = localStorage.getItem('id');
      const URL = `http://localhost:8000/wizyta/epidemic/${this.przekazanie_id}/`;
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
          this.results = res.data;
        });
    },
  },
};
</script>


<style lang="scss" scoped>
  .card{
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, 5%)
  }
</style>
