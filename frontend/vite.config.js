import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// --- GLOBAL CONFIGURATION VARIABLES ---
const PORT = 5173
const API_PREFIX = '/api'
const API_TARGET = 'http://localhost:5000'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: PORT,
    proxy: {
      [API_PREFIX]: {
        target: API_TARGET,
      },
    },
  },
})

