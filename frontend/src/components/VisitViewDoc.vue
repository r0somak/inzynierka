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
      <b-button class='button3' v-on:click="navigate_details(result.id)">
        Szczegóły wizyty</b-button>
    </div>
    <div class="oneline">
      <b-button-toolbar key-nav aria-label="Toolbar with button groups">
        <b-button-group class="mx-1" size="lg">
          <b-button
            v-on:click="previousPage(previous)"
            :disabled="previous === null"
            variant="info">
            &lsaquo;</b-button>
        </b-button-group>
        <b-button-group class="mx-1" size="lg">
          <b-button v-on:click="nextPage(next)"
                    :disabled="next === null"
                    variant="info">
            &rsaquo;</b-button>
        </b-button-group>
      </b-button-toolbar>
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
      next: '',
      previous: '',
    };
  },
  mounted() {
    this.getVisits();
  },
  methods: {
    nextPage(ne) {
      const {
        // eslint-disable-next-line camelcase
        results,
        next,
        previous,
      } = this;
      const data = {
        results,
        next,
        previous,
      };
      console.log(ne);
      const token = localStorage.getItem('token');
      axios({
        method: 'get',
        url: ne,
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
          this.next = res.data.next;
          this.previous = res.data.previous;
          console.log(this.next);
        });
    },
    previousPage(pr) {
      console.log(pr);
      const {
        // eslint-disable-next-line camelcase
        results,
        previous,
        next,
      } = this;
      const data = {
        results,
        previous,
        next,
      };
      console.log(pr);
      const token = localStorage.getItem('token');
      axios({
        method: 'get',
        url: pr,
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
          this.previous = res.data.previous;
          this.next = res.data.next;
          console.log(this.next);
        });
    },
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
          this.$router.push({ name: 'visitdetails', params: { id } });
        });
    },
    getVisits() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        results,
        next,
        previous,
      } = this;
      const data = {
        results,
        next,
        previous,
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
          this.next = res.data.next;
          this.previous = res.data.previous;
          console.log(this.next);
          console.log(this.previous);
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
    margin-top: 40px;
    margin: 0 5px 0 0;
  }
  .results-stats {
    margin: 20px;
  }
  .details {
    display: none;
  }
  .btn-toolbar {
    margin: 30px;
  }
  .oneline {
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 0 0 2px 0;
  }
  .button3 {
    margin: 0 5px 20px 5px;
    width: 20%;
    padding: 5px;
    text-align: center;
    color: black;
    font-size: 15px;
    font-family: 'Abril Fatface', cursive;
    background-color: lightblue;
    border: 3px solid lightblue;
  }
  .button3 {
    @media (max-width: 1400px) {
      font-size: 15px;
    }
    @media (max-width: 1226px) {
      font-size: 11.5px;
      padding: 5px 0 8px 0;
    }
    @media (max-width: 920px) {
      font-size: 10px;
      padding: 5px 0 7px 0;
    }
    @media (max-width: 800px) {
      font-size: 9px;
      padding: 5px 0 5px 0;
    }
    @media (max-width: 698px) {
      font-size: 5px;
      padding: 5px 0 3px 0;
    }
  }
</style>
