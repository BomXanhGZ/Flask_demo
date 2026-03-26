<template>
  <button :type="type" :class="['custom-btn', variant]" :disabled="loading">
    <span v-if="loading">Loading...</span>
    <slot v-else></slot>
  </button>
</template>

<script setup>
defineProps({
  type: { type: String, default: 'submit' },
  variant: { type: String, default: 'primary' },
  loading: Boolean
})
</script>

<style scoped>
.custom-btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 16px;
}
.primary {
  background: #42b983;
  color: white;
}
.primary:hover:not(:disabled) {
  background: #36a372;
}
.danger {
  background: #f44336;
  color: white;
}
.danger:hover:not(:disabled) {
  background: #d32f2f;
}
.custom-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>
