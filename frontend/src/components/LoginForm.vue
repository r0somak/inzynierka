<template>
  <div class="loginForm">
    <div class="input">
    <input class="email" label="Twój email" type="email"/>
    <input class="password" label="Twoje hasło" type="password"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
};
</script>

<style lang="scss" scoped>
  .loginForm {
    width:100%;
  }

.input {
}
  .email,.password {
    width: 30%;
    margin-top: 30px;
    margin-left: 450px;
    background-color: transparent;
    border: none;
    border-bottom: 1px solid black;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
