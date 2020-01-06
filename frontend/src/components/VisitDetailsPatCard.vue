<template>
  <div>
    <b-card
      no-body
      style="max-width: 25rem;"
      img-src="https://www.heart.org/-/media/images/health-topics/metabolic-syndrome/istock842852832-met-syndrome-doctor-sharing-tests.jpg"
      img-alt="Image"
      img-top
      align="center"
    >
      <template v-slot:header>
        <h4 class="mb-0">Szczegółowe dane wizyty</h4>
      </template>

      <b-card-body>
        <b-card-title>Data: {{ data_wizyty.replace('T',' ').replace('Z', ' ') }}</b-card-title>
        <b-card-title>Lekarz: {{ dane_lekarza.name }} {{ dane_lekarza.surname }}</b-card-title>
        <b-card-text>
        </b-card-text>
      </b-card-body>

      <b-list-group flush>
        <b-list-group-item>Nazwa przychodni: {{ dane_przychodni.nazwa }}</b-list-group-item>
        <b-list-group-item>Uwagi: {{ uwagi }}</b-list-group-item>
        <b-list-group-item><b>Objawy:</b>
          <div v-for="objaw in objawy" :key="objaw.id" class="results-data">
            {{objaw.nazwa}},
          </div>
        </b-list-group-item>
        <b-list-group-item>Badania: {{ badania }}</b-list-group-item>
        <b-list-group-item>Dokumenty: {{ dokumenty }}</b-list-group-item>
      </b-list-group>

      <b-card-footer></b-card-footer>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VisitDetailsPatCard',
  data() {
    return {
      data_wizyty: '',
      uwagi: '',
      dane_lekarza: '',
      dane_przychodni: '',
      dokumenty: [],
      objawy: [],
      badania: [],
      przekazanie_id: 0,


    };
  },
  created() {
    this.przekazanie_id = this.$route.params.id;
  },
  mounted() {
    this.getDetails();
  },
  methods: {
    getDetails() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase,max-len
        data_wizyty, uwagi, dane_lekarza, dane_przychodni, dokumenty, objawy, badania,
      } = this;
      const data = {
        data_wizyty,
        uwagi,
        fk_id_lekarz: dane_lekarza,
        fk_id_przychodnia: dane_przychodni,
        dokumenty,
        objawy,
        badania,
      };
        // const { id } = this.$route.params;
      const token = localStorage.getItem('token');
      // const id = localStorage.getItem('id');
      const URL = `http://localhost:8000/wizyta/details/${this.przekazanie_id}/`;
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
          this.data_wizyty = res.data.data_wizyty;
          this.uwagi = res.data.uwagi;
          this.dane_lekarza = res.data.fk_id_lekarz;
          this.dane_przychodni = res.data.fk_id_przychodnia;
          this.dokumenty = res.data.dokumenty;
          this.objawy = res.data.objawy;
          this.badania = res.data.badania;
          console.log(this.id);
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
