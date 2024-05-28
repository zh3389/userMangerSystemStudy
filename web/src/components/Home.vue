<template>
    <div>JWT验证方式在过期前一直有效，不能在服务器端失效<button @click="logout">退出登录</button></div>
    <button @click="getUserInfo">查询用户信息</button>
    <button @click="testAuth">验证用户身份</button>
    <div>
        <p v-if="email">Email: {{ email }}</p>
        <p v-if="id">id: {{ id }}</p>
        <p v-if="response">{{ response }}</p>
        <p v-if="error" style="color: red">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    data() {
        return {
            email: '123@qq.com',
            password: '123123',
            id: null,
            response: null,
            error: null,
        };
    },
    methods: {
        async getUserInfo() {
                try {
                    const response = await axios.get('http://localhost:8000/users/me', {
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('token') || this.access_token}`,
                            'accept': 'application/json',
                        }
                    });
                    this.email = response.data.email;
                    this.id = response.data.id
                    console.log("this.user:", this.id, this.email)
                } catch (error) {
                    console.error('Failed to fetch user info:', error);
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
                    router.push('/Login');
                } catch (error) {
                    console.error('退出登录时出错，请重试。', error);
                }
            },
        async testAuth() {
            try {
                const res = await axios.get('http://localhost:8000/authenticated-route', {
                    headers: {
                            'Authorization': `Bearer ${localStorage.getItem('token') || this.access_token}`,
                            'accept': 'application/json',
                        }
                });
                console.log('res:', res)
                console.log('res.data:', res.data)
                this.response = res.data;
                this.error = null;
            } catch (err) {
                this.error = err.response ? err.response.data : err.message;
                this.response = null;
            }
        },
    }
};

</script>