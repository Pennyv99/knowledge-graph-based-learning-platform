<template>
    <div :class="[ns.b()]" @click="() => emits('click')">
                <img 
                    :class="[ns.e('icon')]" 
                    src="@/assets/pics/ship.png" 
                    >
                <span>{{ msg }}</span>
            </div>
</template>

<script setup lang="ts">

import { useNamespace } from '@/utils/useNamespace'

const ns = useNamespace('icon-panel')

const props = defineProps({
    src: {
        type: String,
        default: '@/assets/pics/ship.png'
    },
    msg: {
        type: String,
        default: '智慧学航'
    }
})

const emits = defineEmits({
    click: Function
})


</script>

<style scoped>

</style>