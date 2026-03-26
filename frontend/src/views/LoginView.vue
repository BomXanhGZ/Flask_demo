<template>
  <AuthCard title="Welcome Back">
    <form @submit.prevent="handleLogin">
      <FormInput 
        label="Username" 
        v-model="form.username" 
        placeholder="Enter your username" 
        required 
      />
      <FormInput 
        label="Password" 
        v-model="form.password" 
        type="password" 
        placeholder="Enter your password" 
        required 
      />
      <AppButton :loading="loading">Login</AppButton>
    </form>
    <p class="auth-link">
      Don't have an account? <router-link to="/register">Register here</router-link>
    </p>
  </AuthCard>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '../api/userApi'
import AuthCard from '../components/AuthCard.vue'
import FormInput from '../components/FormInput.vue'
import AppButton from '../components/AppButton.vue'

const router = useRouter()
const loading = ref(false)
const form = reactive({
  username: '',
  password: ''
})

const handleLogin = async () => {
  loading.value = true
  try {
    const data = await login(form)
    localStorage.setItem('user', JSON.stringify(data))
    router.push('/profile')
  } catch (error) {
    alert('Login failed: ' + (error.response?.data?.message || error.message))
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
