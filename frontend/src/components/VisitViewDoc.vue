<template>
  <div class="list">
    <div v-for="result in results" :key="result.id" class="results-data">
      <div class="results-stats">
        <div class="oneline">
          <a>Data wizyty:</a>
          <span>{{result.data_wizyty.replace('T',' ').replace('Z', ' ')}}</span>
        </div>
        <div class="oneline">
          <a>Pacjent:</a>
          <p>{{result.fk_id_pacjent.name}}</p>
          <span>{{result.fk_id_pacjent.surname}}</span>
        </div>
        <div :id="result.id" class="details">
          <div class="oneline">
            <a>Pacjent:</a>
            <p>{{result.fk_id_pacjent.name}}</p>
            <span>{{result.fk_id_pacjent.surname}}</span>
          </div>
          <div class="oneline">
            <a>Telefon kontaktowy:</a>
            <p>{{result.fk_id_pacjent.telefon}}</p>
          </div>
          <div class="oneline">
            <a>Przychodnia:</a>
            <p>{{result.fk_id_przychodnia.nazwa}}</p>
          </div>
          <div class="oneline">
            <a>Objawy:</a>
            <div v-for="objaw in result.objawy" :key="objaw.id" class="results-data">
              <p>{{objaw.nazwa}}, </p>
            </div>
          </div>
        </div>
      </div>
      <button id='button' v-on:click="navigate_details(result.id)">
        Szczegóły wizyty</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VisitViewDoc',
  data() {
    return {
      results: [],
    };
  },
  mounted() {
    this.getVisits();
  },
  methods: {
    navigate_details(id) {
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
          // const { id } = res.data.results[0];
          // localStorage.setItem('id', id);
          this.$router.push({ name: 'visitdetails', params: { id } });
        });
    },
    navigate_diagnosis() {
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
          const { id } = res.data.results[0];
          // localStorage.setItem('id', id);
          this.$router.push({ name: 'visitdiagnosis', params: { id } });
        });
    },
    togglee(id) {
      const div = document.getElementById(id);
      if (div.style.display === 'block') {
        div.style.display = 'none';
      } else {
        div.style.display = 'block';
      }
    },

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
  a {
    margin: 0 10px 0 0;
  }
  span {
    color: black;
    display: block;
  }
  p {
    margin-top: 50px;
    margin: 0 5px 0 0;
  }
  .results-stats {
    margin: 20px;
  }
  .details {
    display: none;
  }
  .oneline {
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 0 0 10px 0;
  }
  button {
    margin: 0 5px 20px 5px;
    width: 30%;
    padding: 5px;
    text-align: center;
    font-size: 15px;
    font-family: 'Abril Fatface', cursive;
    background-color: lightblue;
    border: 3px solid lightblue;
    border-radius: 40px;
    box-shadow: none;
  }
</style>
