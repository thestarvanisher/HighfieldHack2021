<template>
 <nav>
  <div v-if="name" id="logo">
         <a href="/">{{ name }}</a>
      </div>
  <div v-else id="logo">
   <img v-bind:src="logoImg" alt="Logo" />
  </div>
  <div>
  </div>
  <div v-if="username" class="log-link">
    <a href="/logout/">Logout</a>
  </div>
  <div v-else id="login" class="log-link">
    <a href="/login/">Login</a>
  </div>
 </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['name', 'logoImg', 'username'],
  methods: {},
  mounted() {},
}
</script>

<style scoped>
nav {
	width: 100%;
	position: fixed;
  display: flex;
  align-items: center;
  background-color: #8edc87;
  min-height: 10vh;
  font-family: 'Montserrat', sans-serif;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.4);
}

.log-link {
  float: right;
  clear: right;
  margin-left: 65%;
}
a {
  color: inherit;
  text-decoration: none;
  font-family: 'Montserrat', sans-serif;
  font-weight: 800;
}
div#logo {
  letter-spacing: 5px;
  color: #fefefe;
  font-weight: 800;
  font-size: 2rem;
  float: left;
  margin-left: 5%;
}
</style>