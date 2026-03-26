<template>
  <div class="auth-card">
    <h2>{{ title }}</h2>
    <slot></slot>
  </div>
</template>

<script setup>
defineProps({
  title: String
})
</script>

<style scoped>
.auth-card {
  max-width: 400px;
  margin: 50px auto;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  background: white;
  text-align: left;
}
h2 {
  margin-top: 0;
  color: #2c3e50;
  text-align: center;
}
</style>
