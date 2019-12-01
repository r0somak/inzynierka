<template>
  <div class="loginForm">
    <div class="title"><h3>Zaloguj się</h3></div>
    <div class="input">
    <input class="email" type="email"/>
      <span class ="label-input">Email</span>
    <input class="password" type="password"/>
      <span class ="label-input">Password</span>
    </div>
    <div class="loginbButton">Zaloguj się</div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
};
</script>

<style lang="scss" scoped>
  .loginForm {
    width: 50%;
    height: 100%;
  }
  .title {
    margin-top: 50px;
    font-size: 30px;
  }
  .input {
    display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  width: 100%;
  height: 80px;
  position: relative;
  }
</style>
