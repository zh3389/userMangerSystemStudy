<template>
    <div>
        <!-- <h2>登录</h2> -->
        <div>
            <label for="email">Email:</label>
            <input type="email" v-model="email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" v-model="password" required>
        </div>
        <button @click="login">登录</button>&nbsp&nbsp<button @click="sendResetLink">忘记密码</button>
        <p v-if="message">{{ message }}</p>
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
            message: ''
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post('/auth/jwt/login', {
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
                router.push('/Home')
            } catch (error) {
                alert('登录失败');
            }
        },
        async sendResetLink() {
            try {
                const response = await axios.post('/auth/forgot-password', { email: this.email });
                this.message = '重置密码链接已发送到您的邮箱。';
                console.log("response:", response.status);
                router.push('/ResetPassword')
            } catch (error) {
                this.message = '发送重置密码链接时出错。请重试。';
            }
        }
    }
}

</script>