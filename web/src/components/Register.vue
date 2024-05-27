<template>
    <div>
        <h2>注册</h2>
        <form @submit.prevent="register">
            <div>
                <label for="email">Email:</label>
                <input type="email" v-model="email" required>
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" v-model="password" required>
            </div>
            <button type="submit">注册</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
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
        }
    }
}
</script>