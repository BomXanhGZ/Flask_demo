<template>
  <div class="success-page">
    <h2>Login with Google Success!</h2>
    <AppButton :loading="loading" @click="handleGoToProfile">
      Go to Profile
    </AppButton>
  </div>
</template>

<script setup>
import AppButton from '../components/AppButton.vue'
import getProfile from '../utils/getProfile'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

const loading = ref(false)
const route = useRoute()
const router = useRouter()

onMounted(() => {
  // Lấy token từ URL sau khi Google callback thành công
  const token = route.query.access_token
  if (token) {
    localStorage.setItem('access_token', token)
  } else {
    // Nếu không có token, quay lại login
    router.push('/login')
  }
})

const handleGoToProfile = () => {
  loading.value = true
  const token = localStorage.getItem("access_token")
  
  if (token) {
    // Gọi utility để xử lý việc lưu data user và chuyển hướng
    getProfile(token)
  } else {
    alert('No access token found')
    router.push('/login')
  }
  loading.value = false
}
</script>

<style scoped>
.success-page {
  text-align: center;
  padding: 50px;
}
h2 { color: #42b983; margin-bottom: 20px; }
</style>