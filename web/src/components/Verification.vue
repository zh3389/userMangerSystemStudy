<template>
    <div>
        <h2>电子邮箱验证</h2>
        <input v-model="email" placeholder="请输入需要验证的邮箱" />
        <button @click="sendVerificationEmail">验证邮箱</button>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '321@qq.com',
            message: ''
        };
    },
    methods: {
        async sendVerificationEmail() {
            try {
                const response = await axios.post('http://localhost:8000/auth/request-verify-token', {
                    email: this.email
                });
                console.log(this.email)
                console.log(response)
                if (response.status == 202) {
                    this.message = '验证电子邮件发送成功。请检查您的收件箱。';
                } else {
                    this.message = '无法发送验证电子邮件。请再试一次。';
                }
            } catch (error) {
                this.message = '发送验证电子邮件时出错。';
                console.error(error);
            }
        }
    }
};
</script>