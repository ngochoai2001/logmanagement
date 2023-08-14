import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store'


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000'

axios.interceptors.response.use(undefined, function (error) {
    if (error) {
      const originalRequest = error.config;
      if (error.response&& error.response.status === 403 && !originalRequest._retry) {
        originalRequest._retry = true;
        store.dispatch('logOut');
        return router.push('/login')
      }
    }
  });

  
createApp(App)
.use(router)
.use(store)
.mount('#app')
