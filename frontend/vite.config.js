import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'


// --- GLOBAL CONFIGURATION VARIABLES ---
const API_PREFIX = '/api'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  return {
    plugins: [vue()],
    server: {
      port: env.VITE_PORT,
      proxy: {
        [API_PREFIX]: {
          target: env.VITE_API_TARGET,
        },
      },
    },
  }
})