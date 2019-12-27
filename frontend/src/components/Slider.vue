<template>
  <div>
    <b-carousel
      id="carousel-fade"
      v-model="slide"
      :interval="3000"
      controls
      style="text-shadow: 0px 0px 2px #000"
      fade
      indicators
      img-width="1024"
      img-height="300"
    >
      <b-carousel-slide>
      <template v-slot:img>
        <img
          class="d-block img-fluid w-100"
        caption="First slide"
        src="../assets/slider/slide1.jpg"
        >
      </template>
      </b-carousel-slide>

      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            caption="Second slide"
            src="../assets/slider/slide2.jpg"
            alt="med"
          >
        </template>
      </b-carousel-slide>

      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            caption="Third slide"
            src="../assets/slider/slide3.jpg"
          >
        </template>
      </b-carousel-slide>

      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            caption="Fourth slide"
            src="../assets/slider/slide4.png"
          >
        </template>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
export default {
  name: 'Slider',
};
</script>

<style scoped>
</style>
