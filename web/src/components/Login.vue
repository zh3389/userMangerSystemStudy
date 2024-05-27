<template>
    <div>
        <h2>登录</h2>
        <form @submit.prevent="login">
            <div>
                <label for="email">Email:</label>
                <input type="email" v-model="email" required>
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" v-model="password" required>
            </div>
            <button type="submit">登录</button>
        </form>
        <div>JWT验证方式在过期前一直有效，不能在服务器端失效</div>
        <button @click="logout">退出登录</button>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '123@qq.com',
            password: '123123'
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post('http://localhost:8000/auth/jwt/login', {
                    username: this.email,
                    password: this.password
                }, {
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                });
                this.access_token = response.data.access_token;
                localStorage.setItem('token', this.access_token);
                localStorage.setItem('email', this.email);
                console.log("this.access_token:", this.access_token);
                console.log("this.email:", this.email);
                alert('登录成功');
            } catch (error) {
                alert('登录失败');
            }
        },
        async logout() {
            try {
                const response = await axios.post('http://localhost:8000/auth/jwt/logout', {'token': this.access_token}, {
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('token') || this.access_token}`,
                            'accept': 'application/json',
                        }
                });

                // 假设你在本地存储了用户的 JWT token，需要在退出时清除
                localStorage.removeItem('token');

                // 重定向到登录页面或首页
                // router.push('/login');
            } catch (error) {
                console.error('退出登录时出错，请重试。', error);
            }
        }
    }
}

</script>