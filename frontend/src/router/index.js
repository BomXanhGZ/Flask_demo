import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/LoginView.vue'
import Register from '../views/RegisterView.vue'
import Profile from '../views/ProfileView.vue'
import GGAuthSuccess from '../views/GGAuthSuccessView.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/profile', name: 'Profile', component: Profile },
  { path: '/gg-auth-success', name: 'GGAuthSuccess', component: GGAuthSuccess }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
