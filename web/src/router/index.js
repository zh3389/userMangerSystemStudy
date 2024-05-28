// 导入 Vue 和 Vue Router
import { createRouter, createWebHistory } from 'vue-router'

// 导入您的组件
import HelloWorld from '../components/HelloWorld.vue'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import ResetPassword from '../components/ResetPassword.vue'

// 定义路由
const routes = [
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/Register',
        name: 'Register',
        component: Register
    },
    {
        path: '/Login',
        name: 'Login',
        component: Login
    },
    {
        path: '/ResetPassword',
        name: 'ResetPassword',
        component: ResetPassword
    },
    {
        path: '/Home',
        name: 'Home',
        component: Home
    }
]

// 创建路由器实例并传递 `routes` 配置
const router = createRouter({
    history: createWebHistory(),
    routes
})

// 导出路由器实例
export default router
