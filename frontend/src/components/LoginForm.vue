<template>
  <ValidationObserver v-slot="{ invalid }">
    <form @submit.prevent="loginUser">
      <ValidationProvider name="Login" rules="required" v-slot="{ errors }">
        <input v-model="login" type="text" placeholder="Login">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>
      <ValidationProvider name="Hasło" rules="required"
                          v-slot="{ errors }">
        <input v-model="password" type="password" placeholder="Hasło">
        <span>{{ errors[0] }}</span>
      </ValidationProvider>
      <button type="submit" :disabled="invalid">Zaloguj się</button>
    </form>
  </ValidationObserver>
</template>

<script>
import { extend, localize } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import pl from 'vee-validate/dist/locale/pl.json';
import axios from 'axios';

localize('pl', pl);

extend('required', {
  ...required,
  message: 'Pole {_field_} jest wymagane',
});

export default {
  name: 'LoginForm',
  data() {
    return {
      login: '',
      password: '',
    };
  },
  methods: {
    loginUser() {
      const { login, password } = this;
      const data = {
        username: login,
        password,
      };
      const URL = 'http://localhost:8000/login_user/';
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
          console.log(res);
          const { token } = res.data;
          localStorage.setItem('token', token);
          this.$router.push('/homeloged');
        })
        .catch((err) => {
          alert('Nieprawidłowa nazwa użytkownika lub hasło!');
          // eslint-disable-next-line
        console.log(err)
        });
    },
  },
};
</script>

<style lang="scss" scoped>
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
