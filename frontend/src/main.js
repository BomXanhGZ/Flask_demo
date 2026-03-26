import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
// import router from './router' // uncomment when router is set up

const app = createApp(App)
app.use(createPinia())
// app.use(router)
app.mount('#app')
