<template>
  <div class="backgroundImage">
  </div>
</template>

<script>
export default {
  name: 'BackgroundImage',
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap');;

  .backgroundImage {
    width: 100%;
    min-height: 400px;
    background-image: url('../assets/medbackground.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: top;
    background-attachment: fixed;
    @media (max-width: 700px) {
      min-height: 300px;
    }
  }
  .nav {
    padding: 30px;
    text-align: right;
    font-size: 25px;
    font-family: 'Source Sans Pro', sans-serif;
    a {
      font-weight: bold;
      color: black;
      text-decoration: none;
      padding: 10px;

      &.router-link-exact-active {
        color: white;
      }
    }
    @media (max-width: 700px){
      font-size: 20px;
    }
    @media (max-width: 500px){
      font-size: 15px;
      a {
        padding: 5px;
      }
    }
  }
</style>
