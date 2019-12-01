<template>
  <ValidationObserver v-slot="{ invalid }">
    <form @submit.prevent="onSubmit">
      <ValidationProvider name="Login" rules="required|alpha_num|min:3" v-slot="{ errors }">
        <input v-model="login" type="text" placeholder="Login">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>

      <ValidationProvider name="Password" rules="required|alpha_num|minmax:7,30"
       v-slot="{ errors }">
        <input v-model="password" type="password" placeholder="Hasło">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>
      <button type="submit" :disabled="invalid">Zarejestruj się</button>
    </form>
  </ValidationObserver>
</template>

<script>
import { extend } from 'vee-validate';
// eslint-disable-next-line camelcase
import { required, alpha_num } from 'vee-validate/dist/rules';

extend('required', {
  ...required,
  message: 'Wypełnij pole!',
});

extend('alpha_num', {
  // eslint-disable-next-line camelcase
  ...alpha_num,
  message: 'Może zawierać litery, liczby i znaki: - _',
});

extend('min', {
  validate(value, args) {
    return value.length >= args.length;
  },
  params: ['length'],
  message: 'Login musi zawierać min 3 znaki',
});

extend('minmax', {
  validate(value, { min, max }) {
    return value.length >= min && value.length <= max;
  },
  params: ['min', 'max'],
  message: 'Hasło musi zawierać min 7 znaków, a max 30',
});

export default {
  name: 'RegisterForm',
  data: () => ({
    login: '',
    password: '',
  }),
  methods: {
    onSubmit() {
      alert('Rejestracja przebiegła pomyślnie!');
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
    width: 30%;
    padding: 1%;
    border: 2px solid lightblue;
    border-radius: 5px;
    font-family: 'Abril Fatface', cursive;
  }
  input:focus {
    border: 2px solid blue;
    border-radius: 4px;
  }
  button {
    margin: 20px;
    padding: 10px 20px 10px 20px;
    text-align: center;
    font-size: 14px;
    font-family: 'Abril Fatface', cursive;
    background-color: lightblue;
    border: 3px solid lightblue;
    border-radius: 5px;
    box-shadow: none;
  }
  button:focus {
    background-color: transparent;
    border: 3px solid lightblue;
  }
</style>
