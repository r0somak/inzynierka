<template>
  <div>
    <NavBarLoged/>
    <VisitDiagnosisCard/>
  </div>
</template>

<script>
import NavBarLoged from '../components/NavBarLoged.vue';
import VisitDiagnosisCard from '../components/VisitDiagnosisCard.vue';


export default {
  name: 'VisitDiagnosis',
  components: {
    NavBarLoged,
    VisitDiagnosisCard,
  },
};
</script>

<style scoped>

</style>
