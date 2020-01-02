<template>
  <div>
    <div class="backgroundImage">
    </div>
    <div class="backgroundImage2">
    </div>
  </div>
</template>

<script>
export default {
  name: 'BackgroundImageLong',
};
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap');

  .backgroundImage {
    background-image: url('../assets/medbackground.jpg');
    width: 50%;
    min-height: 840px;
    background-position: top left;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
  }
  .backgroundImage2 {
    background-image: url('../assets/medbackground.jpg');
    width: 50%;
    min-height: 840px;
    background-position: top left;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
  }
</style>
