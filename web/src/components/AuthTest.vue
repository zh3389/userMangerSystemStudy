<template>
    <div>
        <h2>身份验证测试</h2>
        <button @click="testAuth">测试经过身份验证的路由</button>
        <p v-if="response">{{ response }}</p>
        <p v-if="error" style="color: red">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            response: null,
            error: null,
        };
    },
    methods: {
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
    },
};
</script>