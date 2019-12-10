<template>
  <ValidationObserver v-slot="{ invalid }">
    <form @submit.prevent="registerUser">
      <ValidationProvider name="Login" rules="required|alpha_dash|min:3" v-slot="{ errors }">
        <input v-model="login" type="text" placeholder="Login">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Email" rules="required|email" v-slot="{ errors }">
        <input v-model="email" type="email" placeholder="Email">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Hasło" rules="required|alpha_dash|minmax:7,30"
       v-slot="{ errors }">
        <input v-model="password" type="password" placeholder="Hasło">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>
      <button type="submit" :disabled="invalid">Zarejestruj się</button>
    </form>
  </ValidationObserver>
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
  name: 'RegisterForm',
  data() {
    return {
      login: '',
      email: '',
      password: '',
    };
  },
  methods: {
    registerUser() {
      // eslint-disable-next-line no-shadow
      const { login, email, password } = this;
      const data = {
        username: login,
        email,
        password,
      };
      const URL = 'http://localhost:8000/create/user/';
      axios({
        method: 'post',
        url: URL,
        headers: {
          Accept: 'application/json',
          Content: 'application/json',
        },
        data,
      })
        .then((res) => {
          sessionStorage.setItem('token', res.data.token);
          this.$router.push('/');
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
