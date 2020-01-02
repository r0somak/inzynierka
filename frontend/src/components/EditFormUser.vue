<template>
    <form @submit.prevent="mix">
      <ValidationProvider name="Imię" rules="alpha|min:3" v-slot="{ errors }">
        <input v-model="name" type="text" placeholder="Imię">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Nazwisko" rules="alpha|min:3" v-slot="{ errors }">
        <input v-model="surname" type="text" placeholder="Nazwisko">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Pesel" rules="digits:11" v-slot="{ errors }">
        <input v-model="pesel" type="text" placeholder="Pesel">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Ulica" rules="alpha|min:3" v-slot="{ errors }">
        <input v-model="street" type="text" placeholder="Ulica">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Nr ulicy" rules="numeric|min:1" v-slot="{ errors }">
        <input v-model="street_number" type="text" placeholder="Numer ulicy">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Nr mieszkania" rules="numeric|min:1" v-slot="{ errors }">
        <input v-model="ap_number" type="text" placeholder="Numer mieszkania">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Kod pocztowy" rules="alpha_dash|min:6" v-slot="{ errors }">
        <input v-model="post_code" type="text" placeholder="Kod pocztowy">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Miasto" rules="alpha|min:3" v-slot="{ errors }">
        <input v-model="town" type="text" placeholder="Miasto">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <select v-model="selected">
        <option disabled value="">Wybierz województwo</option>
        <option value="BRAK">Brak</option>
        <option value="DOLNOSLAKIE">Dolnośląskie</option>
        <option value="LUBELSKIE">Lubelskie</option>
        <option value="LUBUSKIE">Lubuskie</option>
        <option value="LODZKIE">Łódzkie</option>
        <option value="MALOPOLSKIE">Małopolskie</option>
        <option value="MAZOWIECKIE">Mazowieckie</option>
        <option value="OPOLSKIE">Opolskie</option>
        <option value="PODKARPACKIE">Podkarpackie</option>
        <option value="PODLASKIE">Podlaskie</option>
        <option value="POMORSKIE">Pomorskie</option>
        <option value="SLASKIE">Śląskie</option>
        <option value="SWIETOKRZYSKIE">Świętokrzyskie</option>
        <option value="WARMINSKOMAZURSKIE">Warmińsko-mazurskie</option>
        <option value="WIELKOPOLSKIE">Wielkopolskie</option>
        <option value="ZACHODNIOPOMORSKIE">Zachodniopomorskie</option>
      </select>

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
  name: 'EditFormUser',
  data() {
    return {
      name: '',
      surname: '',
      pesel: '',
      street: '',
      street_number: '',
      ap_number: '',
      post_code: '',
      town: '',
      selected: '',
      phone: '',
    };
  },
  mounted() {
    this.getUser();
  },
  methods: {
    mix() {
      this.toast('b-toaster-top-center');
      this.editUser();
    },
    toast(toaster, append = false) {
      this.$bvToast.toast('Dane zostały zaktualizowane w systemie ', {
        title: 'Informacja',
        toaster,
        solid: true,
        appendToast: append,
        variant: 'primary',
      });
    },
    editUser() {
      // eslint-disable-next-line no-shadow,max-len,camelcase
      const {
        // eslint-disable-next-line camelcase
        name, surname, pesel, street, street_number, ap_number, post_code, town, selected, phone,
      } = this;
      const data = {
        name,
        surname,
        pesel,
        ulica: street,
        nr_ulicy: street_number,
        nr_mieszkania: ap_number,
        kod_pocztowy: post_code,
        miasto: town,
        wojewodztwo: selected,
        telefon: phone,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/patient/profile/';
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
    getUser() {
      // eslint-disable-next-line no-shadow,max-len,camelcase
      const {
        // eslint-disable-next-line camelcase
        name, surname, pesel, street, street_number, ap_number, post_code, town, selected, phone,
      } = this;
      const data = {
        name,
        surname,
        pesel,
        ulica: street,
        nr_ulicy: street_number,
        nr_mieszkania: ap_number,
        kod_pocztowy: post_code,
        miasto: town,
        wojewodztwo: selected,
        telefon: phone,
      };
      const token = localStorage.getItem('token');
      const URL = 'http://localhost:8000/users/patient/profile/';
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
          this.pesel = res.data.pesel;
          this.street = res.data.ulica;
          this.street_number = res.data.nr_ulicy;
          this.ap_number = res.data.nr_mieszkania;
          this.post_code = res.data.kod_pocztowy;
          this.town = res.data.miasto;
          this.selected = res.data.wojewodztwo;
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
    border: 1px solid lightblue;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1em;
    border-radius: 5px;
  }
  input:focus {
    outline: none;
  }
  select {
    width: 40%;
    padding: 1px;
    border: 1px solid lightblue;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1em;
    border-radius: 5px;
    background-color: white;
    text-align: center;
    text-align-last: center;
    margin-bottom: 10px;
  }
  select:focus {
    outline: none;
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
