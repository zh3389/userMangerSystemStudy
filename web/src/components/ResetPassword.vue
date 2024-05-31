<template>
    <div>
        <h2>重置密码</h2>
        <form @submit.prevent="resetPassword">
            <div>
                <label for="newPassword">新密码:</label>
                <input type="password" v-model="newPassword" required />
            </div>
            <div>
                <label for="confirmPassword">确认新密码:</label>
                <input type="password" v-model="confirmPassword" required />
            </div>
            <button type="submit">重置密码</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            newPassword: '',
            confirmPassword: '',
            message: ''
        };
    },
    methods: {
        async resetPassword() {
            if (this.newPassword !== this.confirmPassword) {
                this.message = '两次输入的密码不一致。';
                return;
            }
            try {
                const token = this.$route.query.token; // 假设重置链接中包含token
                const response = await axios.post('/auth/jwt/change-password', {
                    password: this.newPassword,
                    token: token
                });
                this.message = '密码已成功重置。';
            } catch (error) {
                this.message = '重置密码时出错。请重试。';
            }
        }
    }
};
</script>

<style scoped>
/* Add your styles here */
</style>