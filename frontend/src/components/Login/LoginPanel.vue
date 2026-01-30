<template>
    <div :class="[ns.b()]">
        <el-form>
            <el-form-item label="用户名">
                <el-input></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password"></el-input>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace.ts'


const ns = useNamespace('login-panel')

</script>

<style scoped></style>