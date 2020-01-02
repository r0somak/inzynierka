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
    toast(toaster, append = false) {
      this.$bvToast.toast('Nieprawidłowa nazwa użytkownika lub hasło!', {
        title: 'Informacja',
        toaster,
        solid: true,
        appendToast: append,
        variant: 'danger',
      });
    },
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
          // eslint-disable-next-line
          // alert('Nieprawidłowa nazwa użytkownika lub hasło!');
          // eslint-disable-next-line
          console.log(err);
          this.toast('b-toaster-top-center');
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
    width: 40%;
    padding: 1%;
    border: 2px solid lightblue;
    border-radius: 40px;
    font-size: 1em;
    font-family: 'Abril Fatface', cursive;
  }
  input:focus {
    border: 2px solid lightblue;
    border-radius: 40px;
    box-shadow: inset 0 0 0 0px #fff,
    0 0 0 0px #fff,
    -4px 4px 20px lightblue,
    4px -4px 20px #10abff;
    outline: none;
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
