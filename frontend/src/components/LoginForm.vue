<template>
  <ValidationObserver v-slot="{ invalid }">
    <form @submit.prevent="Login">
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
      <ul v-if="photos && photos.length">
        <li v-for="photo of photos" v-bind:key="photo.id">
          <p><strong>{{photo.title}}</strong></p>
          <img :src="photo.url">
        </li>
      </ul>
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
      photos: [],
    };
  },
  created() {
    axios.get('http://jsonplaceholder.typicode.com/photos').then((response) => {
      this.photos = response.data;
    })
      .catch((e) => {
        console.error(e);
      });
  },
  methods: {
    Login() {
      console.log(this.login);
      console.log(this.password);
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
