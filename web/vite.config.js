import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  // // 配置跨域
  // server: {
  //   proxy: {
  //     '/backend': {
  //       target: 'http://localhost:8000',
  //       changeOrigin: true,
  //       rewrite: (path) => {
  //         console.log('Rewriting path:', path);
  //         return path.replace(/^\/backend/, '');
  //       }
  //     }
  //   }
  // }
})
