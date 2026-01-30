<template>
    <div :class="[ns.b()]">


        <div :class="[ns.e('item-group')]">
            <div :class="[
                ns.e('item'),
                ns.is('active', active === index)
            ]" v-for="(label, index) in labels" :key="index" @click="handleClick(index)">
                <span>{{ label }}</span>
            </div>
        </div>

    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { useNamespace } from '@/utils/useNamespace'
import IconPanel from '@/components/icons/IconPanel.vue'
import { useRouter } from 'vue-router'

const ns = useNamespace('sidebar')



const props = defineProps({
    labels: {
        type: Array<String>
    },

})
const emits = defineEmits(['clickItem'])

const router = useRouter()

const msg = ref('智慧学航')
const src = ref('@/assets/pics/ship.png')

// sidebar 选择
const active = ref(0)
const handleClick = (index: number) => {
    active.value = index
    emits('clickItem', index)

    

}



</script>

<style scoped></style>