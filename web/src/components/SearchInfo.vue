<template>
    <h2>查询用户信息</h2>
    <form @submit.prevent="getUserInfo">
        <div v-if="this.user">
            <h2>User Info</h2>
            <p>Email: {{ user.email }}</p>
            <p>id: {{ user.id }}</p>
        </div>
        <button type="submit">查询用户信息</button>
    </form>
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
        async getUserInfo() {
                try {
                    const response = await axios.get('http://localhost:8000/users/me', {
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('token') || this.access_token}`,
                            'accept': 'application/json',
                        }
                    });
                    this.user = response.data;
                    console.log("this.user:", this.user)
                } catch (error) {
                    console.error('Failed to fetch user info:', error);
                }
            }
        }
    }

</script>