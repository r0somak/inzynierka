<template>
  <div class="home">
    <BackgroundImage />
    <div class="divek"/>
  </div>
</template>

<script>
import BackgroundImage from '@/components/BackgroundImage.vue';


export default {
  name: 'home',
  components: {
    BackgroundImage,
  },
};
</script>

<style lang="scss" scoped>
  .divek {
    height:800px;
    background-color:white;
  }
</style>
