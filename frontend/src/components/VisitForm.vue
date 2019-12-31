<template>
    <form @submit.prevent="newVisit">
      <input v-model="data_wizyty" type="datetime-local" required>

      <ValidationProvider name="Uwagi"  rules="min:5" v-slot="{ errors }">
        <textarea v-model="uwagi" type="text" class="uwagi" placeholder="Uwagi"/>
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <select v-model="przychodnia" required>
        <option disabled value="">Wybierz przychodnie</option>
        <option value="1">Najlepsza</option>
      </select>

      <select v-model="lekarz" required>
        <option disabled value="">Wybierz lekarza</option>
        <option value="1">Michał Napnap</option>
        <option value="2">Marczek Kłodka</option>
        <option value="3">Eligiusz Niewiadomski</option>
      </select>

      <select multiple v-model="objawy" required>
        <option disabled value="">Wybierz objawy</option>
        <option :value="result.id" v-for="result in results" :key="result.id">
          {{result.nazwa}}
        </option>
      </select>

      <b-form-file
        class="badania"
        v-model="badania"
        :state="Boolean(badania)"
        placeholder="Wybierz plik z badaniami..."
        drop-placeholder="Albo przeciągnij..."
      ></b-form-file>
      <div class="mt-3">Wybrany plik z badaniami: {{ badania ? badania.name : '' }}</div>

      <b-form-file
        class="dokumenty"
        v-model="dokumenty"
        :state="Boolean(dokumenty)"
        placeholder="Wybierz plik z dokumentami..."
        drop-placeholder="Albo przeciągnij..."
      ></b-form-file>
      <div class="mt-3">Wybrany plik z dokumentami: {{ dokumenty ? dokumenty.name : '' }}</div>

      <button type="submit">Umów wizytę</button>
    </form>
</template>

<script>
import { extend, localize } from 'vee-validate';
// eslint-disable-next-line camelcase
import { required, alpha_dash, email } from 'vee-validate/dist/rules';
import pl from 'vee-validate/dist/locale/pl.json';
import axios from 'axios';

localize('pl', pl);

extend('required', {
  ...required,
  message: 'Pole {_field_} jest wymagane',
});

extend('alpha_dash', {
  // eslint-disable-next-line camelcase
  ...alpha_dash,
  message: 'Pole {_field_} może zawierać litery, cyfry oraz myślnik lub podkreślnik',
});

extend('email', {
  ...email,
  message: 'Pole {_field_} musi być poprawnym adresem email',
});

extend('min', {
  validate(value, args) {
    return value.length >= args.length;
  },
  params: ['length'],
  message: 'Pole {_field_} musi być długie na co najmniej {length} znaki',
});

extend('minmax', {
  validate(value, { min, max }) {
    return value.length >= min && value.length <= max;
  },
  params: ['min', 'max'],
  message: 'Pole {_field_} musi zawierać min {min} znaków, a max {max}',
});

export default {
  name: 'VisitForm',
  data() {
    return {
      // eslint-disable-next-line no-useless-concat
      data_wizyty: '',
      uwagi: '',
      przychodnia: '',
      lekarz: '',
      objawy: [],
      badania: [],
      dokumenty: [],
      results: [],
    };
  },
  mounted() {
    this.getSympt();
  },
  methods: {
    newVisit() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        data_wizyty, uwagi, przychodnia, lekarz, objawy, badania, dokumenty,
      } = this;
      const data = {
        data_wizyty,
        uwagi,
        fk_id_przychodnia: przychodnia,
        fk_id_lekarz: lekarz,
        objawy,
        badania,
        dokumenty,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/wizyta/create/';
      axios({
        method: 'post',
        url: URL,
        headers: {
          Accept: 'application/json',
          Content: 'application/json',
          Authorization: `Token ${token}`,
        },
        data,
      })
        .then((res) => {
          sessionStorage.setItem('token', res.data.token);
          this.data = res.data;
        });
    },
    getSympt() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        results,
      } = this;
      const data = {
        results,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/objawy/list/';
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
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  span {
    padding: 5px 0 12px 0;
    display: block;
    color: red;
  }
  select {
    display: block;
    width: 40%;
    margin:10px 0 0 30%;
    padding: 1px;
    border: 2px solid lightblue;
    font-family: 'Abril Fatface', cursive;
    font-size: 1em;
    border-radius: 20px;
    background-color: white;
  }
  select:focus {
    outline: none;
  }
  .badania, .dokumenty {
    margin: 15px 0 0 0;
    width: 80%;
  }
  .mt-3 {
    margin: 0 0 20px 0;
  }
  input {
    width: 40%;
    padding: 1%;
    border: 2px solid lightblue;
    font-family: 'Abril Fatface', cursive;
    font-size: 1em;
    border-radius: 40px;
    text-align:center;
    margin-top: 5px;
  }
  input:focus {
    outline: none;
  }
  textarea {
    width: 40%;
    padding: 1%;
    border: 2px solid lightblue;
    font-family: 'Abril Fatface', cursive;
    font-size: 1em;
    border-radius: 40px;
    text-align:center;
    margin-top: 5px;
  }
  .uwagi{
    height: 100px;
    border-radius: 20px;
  }
  button {
    margin: 20px;
    width: 30%;
    padding: 1%;
    text-align: center;
    font-size: 16px;
    font-family: 'Abril Fatface', cursive;
    background-color: lightblue;
    border: 3px solid lightblue;
    border-radius: 40px;
    box-shadow: none;
  }
  button:focus {
    background-color: transparent;
    border: 3px solid lightblue;
    border-radius: 40px;
    outline: none;
  }
  button, button:focus, input, input:focus, span {
    @media (max-width: 1400px) {
      font-size: 15px;
    }
    @media (max-width: 920px) {
      font-size: 12px;
      padding: 5px 0 10px 0;
    }
    @media (max-width: 800px) {
      font-size: 10px;
      padding: 5px 0 5px 0;
    }
    @media (max-width: 650px) {
      font-size: 5px;
      padding: 5px 0 3px 0;
    }
  }
</style>
