import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// --- GLOBAL CONFIGURATION VARIABLES ---
const API_PREFIX = '/api'
const { VITE_PORT, VITE_API_TARGET } = import.meta.env

export default defineConfig({
  plugins: [vue()],
  server: {
    port: VITE_PORT,
    proxy: {
      [API_PREFIX]: {
        target: VITE_API_TARGET,
      },
    },
  },
})

