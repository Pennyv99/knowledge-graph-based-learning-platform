<template>
    <div :class="ns.b()">
        
        <Button @click="handleClickReset">重置</Button>
        <Button @click="handleClickSetRoot"> 设置为根节点</Button>
    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace';
import Button from '@/components/Common/Button.vue';
import {inject } from 'vue'

const ns = useNamespace('operations')

const handleClickReset = inject('reset')

const handleClickSetRoot = inject('setRoot')

</script>

<style scoped>


</style>