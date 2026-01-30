<template>
    <div :class="[ns.b()]" >
        <Nav></Nav>
        <div :class="[ns.b(), ns.is('left-right', true)]" @wheel="handleScroll" >
            <Sidebar :labels="labels" @click-item="handleClick"></Sidebar>
            <SwiperWrapper :offset="offset" ></SwiperWrapper>
        </div>
    </div>
    
</template>

<script setup lang="ts">

import Sidebar from '@/components/Home/Sidebar.vue'
import Nav from '@/components/Guide/Nav.vue';
import { computed, ref, provide } from 'vue'
import { useNamespace } from '@/utils/useNamespace';
import SwiperWrapper from '@/components/Home/SwiperWrapper.vue';

const ns = useNamespace('container')

const labels = ref(['数据展示', '智能问答', '推荐系统'])


const i = ref(0)
const offset = computed(() => {
    return i.value*(-100)
})

const handleClick = (index: number) => {
    i.value = index
}

provide('i', i)



const handleScroll = (e: WheelEvent) => {
    e.preventDefault()
    e.stopPropagation()
}
</script>

<style scoped>

</style>