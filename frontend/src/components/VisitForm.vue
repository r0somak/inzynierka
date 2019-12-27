<template>
    <form @submit.prevent="newVisit">

      <input v-model="data_wizyty" type="datetime-local" required>

      <ValidationProvider name="Uwagi" rules="min:5" v-slot="{ errors }">
        <input v-model="uwagi" type="text" placeholder="Uwagi">
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
        <option value="1">Ból gardła</option>
        <option value="2">Nieżyt nosa</option>
        <option value="3">Kaszel</option>
        <option value="4">Duszność</option>
        <option value="5">Sinica</option>
        <option value="6">Krwioplucie</option>
        <option value="7">Gorączka</option>
        <option value="8">Zawroty głowy</option>
        <option value="9">Osłabienie siły mięśniowej</option>
        <option value="10">Ból głowy</option>
      </select>
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
      data_wizyty: '',
      uwagi: '',
      przychodnia: '',
      lekarz: '',
      objawy: [],
    };
  },
  methods: {
    newVisit() {
      // eslint-disable-next-line no-shadow,camelcase
      const {
        // eslint-disable-next-line camelcase
        data_wizyty, uwagi, przychodnia, lekarz, objawy,
      } = this;
      const data = {
        data_wizyty,
        uwagi,
        fk_id_przychodnia: przychodnia,
        fk_id_lekarz: lekarz,
        objawy,
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
  input {
    width: 40%;
    padding: 1%;
    border: 2px solid lightblue;
    font-family: 'Abril Fatface', cursive;
    font-size: 1em;
    border-radius: 40px;
  }
  input:focus {
    border: 2px solid lightblue;
    border-radius: 40px;
    box-shadow: inset 0 0 0 0px #fff,
    0 0 0 0px #fff,
    -4px 4px 20px lightblue,
    4px -4px 20px #10abff;
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
