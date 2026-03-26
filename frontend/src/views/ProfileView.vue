<template>
  <div class="profile-view">
    <div class="loading" v-if="loading">Loading profile...</div>
    <div class="profile-container" v-else-if="user">
      <h2>User Profile</h2>
      <div class="profile-card">
        <div class="avatar">{{ user.username.charAt(0).toUpperCase() }}</div>
        <div class="info">
          <p><strong>Username:</strong> {{ user.username }}</p>
          <p><strong>Email:</strong> {{ user.email || 'N/A' }}</p>
          <p><strong>ID:</strong> #{{ user.id }}</p>
        </div>
        <AppButton variant="danger" @click="handleLogout">Logout</AppButton>
      </div>
    </div>
    <div v-else class="login-prompt">
      <p>Please <router-link to="/login">login</router-link> to view your profile.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AppButton from '../components/AppButton.vue'

import { getProfile } from '../api/userApi'

const router = useRouter()
const user = ref(null)
const loading = ref(true)

onMounted(async () => {
  const savedUser = localStorage.getItem('user')
  if (savedUser) {
    try {
      const basicInfo = JSON.parse(savedUser)
      // basicInfo usually contains {id, username}
      // We fetch full data from backend to get email etc.
      const fullProfile = await getProfile(basicInfo.id)
      user.value = fullProfile
    } catch (error) {
      console.error('Failed to fetch profile:', error)
      // Fallback to localStorage if API fails
      user.value = JSON.parse(savedUser)
    }
  }
  loading.value = false
})

const handleLogout = () => {
  localStorage.removeItem('user')
  router.push('/login')
}
</script>

<style scoped>
.profile-view {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
}
.profile-container {
  width: 100%;
  max-width: 400px;
}
.profile-card {
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  background: white;
  text-align: center;
}
.avatar {
  width: 80px;
  height: 80px;
  background: #42b983;
  color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 32px;
  font-weight: bold;
  margin: 0 auto 20px;
}
.info {
  margin-bottom: 25px;
  text-align: left;
}
.info p {
  margin: 10px 0;
  color: #2c3e50;
}
.login-prompt {
  text-align: center;
  color: #666;
}
.login-prompt a {
  color: #42b983;
  font-weight: bold;
}
</style>
