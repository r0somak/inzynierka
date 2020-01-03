<template>
  <div class="backgroundImage">
  </div>
</template>

<script>
export default {
  name: 'BackgroundImageHalf',
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap');

  .backgroundImage {
    background-image: url('../assets/medbackground.jpg');
    width: 50%;
    min-height: 950px;
    background-position: top left;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
  }
</style>
