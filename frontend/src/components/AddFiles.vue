<template>
  <b-card
    title="Dołączanie badań i dokumentów"
    img-src="http://transportoweprawo.pl/wp-content/uploads/2017/12/Organize-File-and-Folder-1.jpg"
    img-top
    tag="article"
    style="max-width: 30rem;"
    class="mb-2">
    <b-card-text>
    </b-card-text>
  <form>
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

    <button type="submit">Wyślij pliki</button>
  </form>
  </b-card>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddFiles',
  data() {
    return {
      badania: [],
      dokumenty: [],
      przekazanie_id: 0,
    };
  },
  created() {
    this.przekazanie_id = this.$route.params.id;
  },
  methods: {
    editFiles() {
      // eslint-disable-next-line no-shadow,max-len,camelcase
      const {
        // eslint-disable-next-line camelcase
        badania, dokumenty,
      } = this;
      const data = {
        badania,
        dokumenty,
      };
      const token = localStorage.getItem('token');
      const URL = `http://localhost:8000/wizyta/details/${this.przekazanie_id}`;
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
          this.badania = res.data.badania;
          this.dokumenty = res.data.dokumenty;
          // this.$router.push('/editprofile');
        });
    },
  },
};
</script>

<style lang="scss" scoped>
  .card{
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, 10%);
  }
  .badania, .dokumenty {
    margin: 15px 0 0 0;
    width: 80%;
    font-size: 15px;
  }
  .mt-3 {
    margin: 0 0 20px 0;
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
  button, button:focus {
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
