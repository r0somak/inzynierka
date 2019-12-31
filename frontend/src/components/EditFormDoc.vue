<template>
  <form @submit.prevent="editDoctor">
    <ValidationProvider name="Imię" rules="alpha|min:3" v-slot="{ errors }">
      <input v-model="name" type="text" placeholder="Imię">
      <span>{{ errors[0] }}</span>
    </ValidationProvider>

    <ValidationProvider name="Nazwisko" rules="alpha|min:3" v-slot="{ errors }">
      <input v-model="surname" type="text" placeholder="Nazwisko">
      <span>{{ errors[0] }}</span>
    </ValidationProvider>

    <ValidationProvider name="Specjalizacja" rules="alpha|min:3" v-slot="{ errors }">
      <input v-model="spec" type="text" placeholder="Specjalizacja">
      <span>{{ errors[0] }}</span>
    </ValidationProvider>

    <ValidationProvider name="Nr_pwz" rules="numeric|min:4" v-slot="{ errors }">
      <input v-model="nr_pwz" type="text" placeholder="Numer PWZ">
      <span>{{ errors[0] }}</span>
    </ValidationProvider>

    <ValidationProvider name="Telefon" rules="numeric|min:9" v-slot="{ errors }">
      <input v-model="phone" type="tel" placeholder="Telefon">
      <span>{{ errors[0] }}</span>
    </ValidationProvider>

    <button type="submit">Edytuj dane</button>
  </form>
</template>

<script>
import { extend, localize } from 'vee-validate';
// eslint-disable-next-line camelcase
import {
  // eslint-disable-next-line camelcase
  alpha_dash, email, alpha, digits, numeric,
} from 'vee-validate/dist/rules';
import pl from 'vee-validate/dist/locale/pl.json';
import axios from 'axios';


localize('pl', pl);


extend('alpha_dash', {
  // eslint-disable-next-line camelcase
  ...alpha_dash,
  message: 'Pole {_field_} może zawierać litery, cyfry oraz myślnik lub podkreślnik',
});

extend('alpha', {
  // eslint-disable-next-line camelcase
  ...alpha,
  message: 'Pole {_field_} może zawierać wyłącznie litery',
});

extend('email', {
  ...email,
  message: 'Pole {_field_} musi być poprawnym adresem email',
});

extend('digits', {
  ...digits,
  message: 'Pole {_field_} musi być poprawnym peselem',
});

extend('numeric', {
  ...numeric,
  message: 'Pole {_field_} musi zawierać cyfry',
});

extend('min', {
  validate(value, args) {
    return value.length >= args.length;
  },
  params: ['length'],
  message: 'Pole {_field_} musi być długie na co najmniej {length} znaki',
});


export default {
  name: 'EditFormDoc',
  data() {
    return {
      name: '',
      surname: '',
      spec: '',
      nr_pwz: '',
      phone: '',
    };
  },
  mounted() {
    this.getDoctor();
  },
  methods: {
    editDoctor() {
      // eslint-disable-next-line no-shadow,max-len,camelcase
      const {
        // eslint-disable-next-line camelcase
        name, surname, spec, nr_pwz, phone,
      } = this;
      const data = {
        name,
        surname,
        specjalizacja: spec,
        nr_pwz,
        telefon: phone,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/doctor/profile/';
      console.log('TOKEN: {0}', token);
      axios({
        method: 'patch',
        url: URL,
        headers: {
          Accept: 'application/json',
          Authorization: `Token ${token}`,
        },
        data,
      })
        .then((res) => {
          this.name = res.data.name;
          // this.$router.push('/editprofile');
        });
    },
    getDoctor() {
      // eslint-disable-next-line no-shadow,max-len,camelcase
      const {
        // eslint-disable-next-line camelcase
        name, surname, spec, nr_pwz, phone,
      } = this;
      const data = {
        name,
        surname,
        specjalizacja: spec,
        nr_pwz,
        telefon: phone,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/doctor/profile/';
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
          this.name = res.data.name;
          this.surname = res.data.surname;
          this.spec = res.data.specjalizacja;
          this.nr_pwz = res.data.nr_pwz;
          this.phone = res.data.telefon;
          // this.$router.push('/editprofile');
        });
    },
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap');
  span {
    padding: 5px 0 5px 0;
    display: block;
    color: red;
  }
  strong {
    color: black;
  }
  input {
    width: 40%;
    padding: 1px;
    border: 2px solid lightblue;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1em;
    border-radius: 20px;
  }
  input:focus {
    outline: none;
  }
  select {
    width: 40%;
    padding: 1px;
    border: 2px solid lightblue;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1em;
    border-radius: 20px;
    background-color: white;
    text-align: center;
    text-align-last: center;
    margin-bottom: 10px;
  }
  button {
    margin: 20px;
    width: 30%;
    padding: 1%;
    text-align: center;
    font-size: 16px;
    font-family: 'Source Sans Pro', sans-serif;
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
