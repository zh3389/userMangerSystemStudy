<template>
  <div>
    <h4>版本一：编写完所有页面和API后，用于学习Vue页面的编写和API的调用</h4>
    <h4>版本二：在版本一的基础上增加路由，用于学习Vue路由相关的知识</h4>
    <h4>版本三：在版本二的基础打包和部署及CROS配置，用于学习Vue打包和部署相关知识</h4>
    <hr>
    <h2>欢迎使用XX系统</h2>
    <Register />
    <hr>
    <Verification />
    <hr>
    <Login /><Logout />
    <hr>
    <SearchInfo />
    <hr>
    <ForgotPassword />
    <hr>
    <ResetPassword />
    <hr>
    <AuthTest />
  </div>
</template>

<script>
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import SearchInfo from './components/SearchInfo.vue';
import ForgotPassword from './components/ForgotPassword.vue';
import ResetPassword from './components/ResetPassword.vue';
import Verification from './components/Verification.vue';
import AuthTest from './components/AuthTest.vue';

export default {
  components: {
    Login,
    Register,
    SearchInfo,
    ForgotPassword,
    ResetPassword,
    Verification,
    AuthTest,
  }
}
</script>
