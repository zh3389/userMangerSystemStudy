<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <div class="card">
    <p>这里是网页的Home页，用于程序进入或使用说明。</p>
    <button type="button" @click="count++">计数为 {{ count }}</button>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
