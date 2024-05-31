import { createApp } from 'vue'
import './style.css'
import router from './router'
import App from './App.vue'
import axios from 'axios'

// axios.defaults.baseURL = "http://localhost:8000"
axios.defaults.baseURL = "http://154.8.156.156:8000"

createApp(App).use(router).mount('#app')
