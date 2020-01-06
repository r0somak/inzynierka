<template>
  <div>
    <NavBar/>
    <Slider/>
    <Cards/>
    <Footer/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import Slider from '@/components/Slider.vue';
import Footer from '@/components/Footer.vue';
import Cards from '@/components/Cards.vue';


export default {
  name: 'home',
  components: {
    Cards,
    Footer,
    Slider,
    NavBar,
  },
};
</script>

<style lang="scss" scoped>
</style>
