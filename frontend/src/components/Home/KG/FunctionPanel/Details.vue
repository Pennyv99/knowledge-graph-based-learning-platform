<template>
    <div :class="ns.b()">
        <div :class="ns.e('detail-wrapper')">
            <span :class="ns.e('label')">知识点名称：</span>
            <span>{{ cur?.properties?.name }}</span>
        </div>
        <div :class="ns.e('detail-wrapper')">
            <span :class="ns.e('label')"> 知识点级别：</span>
            <span>{{ cur?.label }}</span>
        </div>
        <div :class="ns.e('detail-wrapper')">
            <span :class="ns.e('label')">知识点描述：</span>
            <span>{{ cur?.properties?.description }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace';
import { inject } from 'vue'

const ns = useNamespace('details')



const cur = inject('cur')

</script>

<style lang="scss"></style>