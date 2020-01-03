<template>
    <form @submit.prevent="mix">
      <input v-model="data_wizyty" type="datetime-local" required>

      <ValidationProvider name="Uwagi"  rules="min:5" v-slot="{ errors }">
        <textarea v-model="uwagi" type="text" class="uwagi" placeholder="Uwagi"/>
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <select v-model="przychodnia" required>
        <option disabled value="">Wybierz przychodnie</option>
        <option :value="result.id" v-for="result in results_przych" :key="result.id">
          {{ result.nazwa }}
        </option>
      </select>

      <select v-model="lekarz" required>
        <option disabled value="">Wybierz lekarza</option>
        <option :value="result.id" v-for="result in results_doc" :key="result.id">
          {{ result.name }} {{ result.surname }}
        </option>
      </select>

      <div id="multi">
        <label class="typo__label">Wybierz objawy</label>
        <multiselect
          v-model="objawy"
          :options="results"
          :multiple="true" :close-on-select="false"
          :clear-on-select="false"
          :preserve-search="true"
          placeholder="Wybierz"
          label="nazwa"
          track-by="id"
          selectLabel="Naciśnij aby wybrać"
          selectedLabel="Wybrany"
          deselectLabel="Naciśnij aby usunąć"
          :preselect-first="true"
          @input="updateId">
          <template slot="selection" slot-scope="{ objaw, search, isOpen }">
            <span class="multiselect__single" v-if="objaw &amp;&amp; !isOpen">
              {{ objaw }} wybrane objawy</span></template>
        </multiselect>
      </div>

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
      ></b-form-file><br>
      <div class="mt-3">Wybrany plik z dokumentami: {{ dokumenty ? dokumenty.name : '' }}</div>

      <b-button type="submit">Umów wizytę</b-button>
    </form>
</template>

<script>
import { extend, localize } from 'vee-validate';
// eslint-disable-next-line camelcase
import { required, alpha_dash, email } from 'vee-validate/dist/rules';
import pl from 'vee-validate/dist/locale/pl.json';
import axios from 'axios';
import Multiselect from 'vue-multiselect';

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
  components: {
    Multiselect,
  },
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
      results_przych: [],
      results_doc: [],
      upid: [],
    };
  },
  mounted() {
    this.getSympt();
    this.getPrzych();
    this.getDoc();
  },
  methods: {
    mix() {
      this.toast('b-toaster-top-center');
      this.newVisit();
      this.clear();
    },
    toast(toaster, append = false) {
      this.$bvToast.toast('Wizyta została zarejestrowana w systemie', {
        title: 'Informacja',
        toaster,
        solid: true,
        appendToast: append,
        variant: 'primary',
      });
    },
    updateId(objawy) {
      const upid = [];

      objawy.forEach((objaw) => {
        upid.push(objaw.id);
      });

      this.upid = upid;
    },
    clear() {
      this.data_wizyty = '';
      this.uwagi = '';
      this.przychodnia = '';
      this.lekarz = '';
      this.objawy = '';
      this.badania = [];
      this.dokumenty = [];
      this.upid = [];
    },
    newVisit() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        data_wizyty, uwagi, przychodnia, lekarz, upid, badania, dokumenty,
      } = this;
      const data = {
        data_wizyty,
        uwagi,
        fk_id_przychodnia: przychodnia,
        fk_id_lekarz: lekarz,
        objawy: upid,
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
          console.log(res.data);
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

    getPrzych() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        results_przych,
      } = this;
      const data = {
        results: results_przych,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/przychodnia/list/';
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
          this.results_przych = res.data.results;
          console.log('przychodnia', res.data.results);
        });
    },

    getDoc() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        results_doc,
      } = this;
      const data = {
        results: results_doc,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/doctor/list/';
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
          this.results_doc = res.data.results;
        });
    },

  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap" rel="stylesheet');
    .multiselect {
      width: 60%;
      display: inline-block;
      margin: 0 0 20px 0;
    }
    label {
      margin: 15px 0 0 0;
      display: block;
    }
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
      border: 1px solid lightblue;
      font-family: 'Source Sans Pro', sans-serif;
      font-size: 1em;
      border-radius: 5px;
      background-color: white;
      text-align: center;
      text-align-last: center;
    }
    select:focus {
      outline: none;
    }
    .badania, .dokumenty {
      margin: 15px 0 0 0;
      width: 60%;
    }
    .mt-3 {
      margin: 0 0 20px 0;
    }
    input {
      width: 40%;
      padding: 1%;
      border: 1px solid lightblue;
      font-family: 'Source Sans Pro', sans-serif;
      font-size: 1em;
      border-radius: 5px;
      text-align:center;
      margin-top: 5px;
    }
    input:focus {
      outline: none;
    }
    textarea {
      width: 40%;
      padding: 1%;
      border: 1px solid lightblue;
      font-family: 'Source Sans Pro', sans-serif;
      font-size: 1em;
      border-radius: 10px;
      text-align:center;
      margin-top: 5px;
    }
    textarea:focus {
      outline: none;
  }
    .uwagi{
      height: 100px;
      border-radius: 5px;
    }
    button {
      margin: 20px;
      width: 20%;
      padding: 1%;
      text-align: center;
      font-size: 16px;
      color: black;
      font-family: 'Source Sans Pro', sans-serif;
      background-color: lightblue;
      border: 3px solid lightblue;
    }
    button, textarea, input, input:focus, span {
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
