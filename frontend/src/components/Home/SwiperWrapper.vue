<template>
    <div :class="ns.b()" @wheel="handleScroll" :style="style">
        <div :class="ns.e('item')">
            <KnowledgeGraph></KnowledgeGraph>
        </div>
        <div class="inner b" :class="[ns.e('item')]">
            <!-- 此处插入组件 -->
            <QASystem></QASystem>
        </div>
        
        <div class="inner d" :class="[ns.e('item')]">
            <!-- 此处插入组件 -->
            <Recommend></Recommend>
        </div>

    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace';
import { useSlots, ref, computed, watch } from 'vue'
import throttle from '@/utils/throttle'
import KnowledgeGraph from './KG/KnowledgeGraph.vue';
import Recommend from './Recommend/Recommend.vue';
import QASystem from './QASystem/QASystem.vue';

const ns = useNamespace('swipper')


const props = defineProps(['offset'])

const style = ref({})

// 添加滚动效果
watch(() => props.offset, () => {
    style.value = {
        transform: `translateY(${props.offset}vh)`,
        transitionDuration: '500ms'
    }
})

const handleScroll = (e: WheelEvent) => {
    e.preventDefault()
    e.stopPropagation()
}
</script>

<style scoped>
.outer {
    /* height: 900px; */
    height: 100vh;
    width: 1600px;
    margin: 0 auto 0 auto;

    position: relative;
    z-index: 0;
}

.inner {
    height: 100vh;
}

.a {


    display: flex;
    justify-content: center;
    align-items: center;

}

.b {
    /* background-color: aquamarine; */
}

.c {
    /* background-color: azure; */
}

.d {
    /* background-color: beige; */
}
</style>