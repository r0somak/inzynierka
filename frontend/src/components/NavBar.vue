<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand tag="h1" class="mb-0">MEDIVI</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-navbar-nav>
            <b-nav-item href="/">Strona główna</b-nav-item>
            <b-nav-item href="/login">Logowanie</b-nav-item>
            <b-nav-item href="/register">Rejestracja</b-nav-item>
          </b-navbar-nav>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>O nas</em>
            </template>
            <b-dropdown-item href="#">Kontakt</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style lang="scss" scoped>
  .navbar-brand {
    font-size: 1.75rem;
    font-style: italic;
    font-weight: bold;
  }

</style>
