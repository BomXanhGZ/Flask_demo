<template>
  <AuthCard title="Create Account">
    <form @submit.prevent="handleRegister">
      <FormInput 
        label="Username" 
        v-model:input-value="form.username" 
        placeholder="Enter your username" 
        required 
      />
      <FormInput 
        label="Email" 
        v-model:input-value="form.email" 
        type="email" 
        placeholder="Enter your email" 
        required 
      />
      <FormInput 
        label="Password" 
        v-model:input-value="form.password" 
        type="password" 
        placeholder="Choose a password" 
        required 
      />
      <AppButton :loading="loading">Register</AppButton>
    </form>
    <p class="auth-link">
      Already have an account? <router-link to="/login">Login here</router-link>
    </p>
  </AuthCard>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { register } from '../api/userApi'
import AuthCard from '../components/AuthCard.vue'
import FormInput from '../components/FormInput.vue'
import AppButton from '../components/AppButton.vue'

const router = useRouter()
const loading = ref(false)
const form = reactive({
  username: '',
  email: '',
  password: ''
})

const handleRegister = async () => {
  loading.value = true
  try {
    await register(form)
    alert('Registration successful! Please login.')
    router.push('/login')
  } catch (error) {
    alert('Registration failed: ' + (error.response?.data?.message || error.message))
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-link {
  margin-top: 20px;
  text-align: center;
  font-size: 14px;
}
.auth-link a {
  color: #42b983;
  text-decoration: none;
  font-weight: 600;
}
</style>
