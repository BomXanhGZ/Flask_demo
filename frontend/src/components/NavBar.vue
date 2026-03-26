<template>
  <nav class="nav-bar">
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/profile">Profile</router-link>
  </nav>
</template>

<style scoped>
.nav-bar {
  padding: 30px;
  text-align: center;
}
.nav-bar a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 10px;
}
.nav-bar a.router-link-exact-active {
  color: #42b983;
}
</style>
