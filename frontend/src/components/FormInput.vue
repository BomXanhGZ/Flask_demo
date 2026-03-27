<template>
  <div class="form-group">
    <label v-if="label">{{ label }}</label>
    <input 
      :type="type" 
      :placeholder="placeholder" 
      :required="required"
      :value="inputValue"
      v-on:input="$emit('update:inputValue', $event.target.value)"
    />
  </div>
</template>

<script setup>
defineProps({
  label: String,
  type: { type: String, default: 'text' },
  placeholder: String,
  required: Boolean,
  inputValue: String
})
defineEmits(['update:inputValue'])
</script>

<style scoped>
.form-group {
  margin-bottom: 20px;
}
label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #2c3e50;
}
input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-sizing: border-box;
  font-size: 14px;
  transition: border-color 0.2s;
}
input:focus {
  outline: none;
  border-color: #42b983;
}
</style>
