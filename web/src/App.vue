<template>
    <div id="app">
      <h2>欢迎使用XX系统</h2>
        <!-- <strong>当前路由路径:</strong> {{ $route.fullPath }} -->
      <nav>
        <div v-if="$route.path === '/' | $route.path === '/Register' | $route.path === '/Login'">
          <RouterLink to="/Register">注册</RouterLink>&nbsp&nbsp<RouterLink to="/Login">登录</RouterLink>
        </div>
      </nav>
    </div>
    <main>
      <RouterView />
    </main>
      <br />
      <h4>版本一：编写完所有页面和API后，用于学习Vue页面的编写和API的调用</h4>
      <h4>版本二：在版本一的基础上增加路由，用于学习Vue路由相关的知识</h4>
      <h4>版本三：在版本二的基础打包和部署及CROS配置，用于学习Vue打包和部署相关知识</h4>
</template>


<script>
import Login from './components/Login.vue';
import Register from './components/Register.vue';


export default {
  name: 'App',
  components: {
    Register,
    Login
  }
}
</script>




<style>
/* Add some basic styling */
nav {
  margin-bottom: 20px;
}
nav ul {
  list-style-type: none;
  padding: 0;
}
nav ul li {
  display: inline;
  margin-right: 10px;
}
</style>
