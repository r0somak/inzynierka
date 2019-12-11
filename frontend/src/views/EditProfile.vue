<template>
  <div class="edit">
    <div class="form">
  <p>Edycja danych</p>
  <EditForm/>
  </div>
  <div class="backgroundimage">
    <BackgroundImageHalf/>
  </div>
  </div>
</template>

<script>
import EditForm from '@/components/EditForm.vue';
import BackgroundImageHalf from '@/components/BackgroundImageHalf.vue';

export default {
  name: 'EditProfile',
  components: {
    EditForm,
    BackgroundImageHalf,
  },
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');
  .nav {
    padding: 30px;
    text-align: right;
    font-size: 25px;
    font-family: 'Abril Fatface', cursive;
    a {
      font-weight: bold;
      color: black;
      text-decoration: none;
      padding: 10px;

      &.router-link-exact-active {
        color: royalblue;
      }
    }
    @media (max-width: 1400px){
      font-size: 20px;
      a {
        padding: 5px;
      }
    }
    @media (max-width: 920px){
      font-size: 17px;
    }
    @media (max-width: 800px){
      font-size: 12px;
      a {
        padding: 5px;
      }
    }
    @media (max-width: 650px){
      font-size: 8px;
      a {
        padding: 5px;
      }
    }
  }
  p {
    margin-top: 100px;
    font-size: 35px;
    font-family: 'Abril Fatface', cursive;
    @media (max-width: 1400px) {
      font-size: 25px;
    }
    @media (max-width: 920px) {
      font-size: 20px;
    }
    @media (max-width: 790px) {
      font-size: 15px;
    }
    @media (max-width: 650px) {
      font-size: 10px;
    }
  }
  .form {
    float:right;
    width:50%;
  }
  #BackgroundImageHalf {
    float:left;
    width:50%;
  }

</style>
