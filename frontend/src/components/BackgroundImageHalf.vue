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
@import url('https://fonts.googleapis.com/css?family=Abril+Fatface&display=swap');

  .backgroundImage {
   background-image: url('../assets/medbackground.jpg');
    width: 50%;
    min-height: 800px;
    background-position: top left;
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>
