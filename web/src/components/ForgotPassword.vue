<template>
    <div>
        <h2>忘记密码</h2>
        <form @submit.prevent="sendResetLink">
            <div>
                <label for="email">邮箱:</label>
                <input type="email" v-model="email" required />
            </div>
            <button type="submit">发送重置密码链接</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '123@qq.com',
            message: ''
        };
    },
    methods: {
        async sendResetLink() {
            try {
                const response = await axios.post('http://localhost:8000/auth/forgot-password', { email: this.email });
                this.message = '重置密码链接已发送到您的邮箱。';
                console.log("response:", response.status);
            } catch (error) {
                this.message = '发送重置密码链接时出错。请重试。';
            }
        }
    }
};
</script>

<style scoped>
/* Add your styles here */
</style>