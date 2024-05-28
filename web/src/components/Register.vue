<template>
    <div>
        <!-- <h2>注册</h2> -->
        <div>
            <label for="email">Email:</label>
            <input type="email" v-model="email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" v-model="password" required>
        </div>
        <button @click="register">注册</button>&nbsp&nbsp<button @click="sendVerificationEmail">验证邮箱</button>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '123@qq.com',
            password: '123123',
            message: '' // 添加 message 到 data 属性
        }
    },
    methods: {
        async register() {
            try {
                await axios.post('http://localhost:8000/auth/register', {
                    email: this.email,
                    password: this.password
                });
                alert('注册成功');
            } catch (error) {
                alert('注册失败');
            }
        },
        async sendVerificationEmail() {
            try {
                const response = await axios.post('http://localhost:8000/auth/request-verify-token', {
                    email: this.email
                });
                console.log(this.email)
                console.log(response)
                if (response.status == 202) {
                    this.message = '验证电子邮件发送成功。请检查您的收件箱。'; // 更新 message
                } else {
                    this.message = '无法发送验证电子邮件。请再试一次。'; // 更新 message
                }
            } catch (error) {
                this.message = '发送验证电子邮件时出错。'; // 更新 message
                console.error(error);
            }
        }
    }
}
</script>