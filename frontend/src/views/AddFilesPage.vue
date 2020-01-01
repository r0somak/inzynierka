<template>
  <div>
  <NavBarLoged/>
  <AddFiles/>
  </div>
</template>

<script>
import NavBarLoged from '../components/NavBarLoged.vue';
import AddFiles from '../components/AddFiles.vue';

export default {
  name: 'AddFilesPage',
  components: {
    NavBarLoged,
    AddFiles,

  },
};
</script>

<style scoped>

</style>
