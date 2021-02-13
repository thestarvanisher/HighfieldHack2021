<template>
  <div id="app">
    <div id="movedown">
      <img alt="Vue logo" src="./assets/logo.png">
      <Login/>
    </div>
    
  </div>
</template>

<script>
import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#movedown {
  padding-top: 10vh;
}

</style>
