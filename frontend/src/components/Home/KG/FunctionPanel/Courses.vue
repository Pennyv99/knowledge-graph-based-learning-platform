<template>
    <div :class="ns.b()" @wheel="handleScroll">
        <div v-for="(item) in courses" :key="item.id" :class="ns.e('selection-item')"
            @click="handleClickCourse(item.id)">
            <span>{{ item.name }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">

import { inject, watch } from 'vue';
import { useNamespace } from '@/utils/useNamespace';
import type { Link } from '../node';

interface Course {
    id: string
    name: string
}

const ns = useNamespace('courses')

const courses = <Array<Course>>inject('courses')
const handleClickCourse = inject('clickCourse') as Function


watch(() => courses, () => {
    console.log(courses)
})

const handleScroll = (e: WheelEvent) => {
    e.stopPropagation()
}

</script>

<style lang="scss"></style>