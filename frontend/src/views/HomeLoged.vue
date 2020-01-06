<template>
<div class="home">
  <NavBarLoged/>
  <Slider/>
  <Cards/>
  <Footer/>
</div>
</template>

<script>
import NavBarLoged from '../components/NavBarLoged.vue';
import Slider from '@/components/Slider.vue';
import Footer from '@/components/Footer.vue';
import Cards from '@/components/Cards.vue';

export default {
  name: 'HomeLoged',
  components: {
    NavBarLoged,
    Cards,
    Footer,
    Slider,
  },
};
</script>

<style lang="scss" scoped>

</style>
