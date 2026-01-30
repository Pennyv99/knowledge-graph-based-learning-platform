<template>
    <div :class="[ns.b()]">
        <div id="KG" :class="ns.e('kg')">
            <svg id="kg-svg"></svg>
        </div>

        <div :class="[ns.e('panel-wrapper')]">
            <FunctionPanel></FunctionPanel>
        </div>
    </div>
</template>

<script setup lang="ts">
// components
import FunctionPanel from './FunctionPanel/FunctionPanel.vue';
import nodes from '@/assets/data/nodes.json'
import links from '@/assets/data/relationship.json'

import * as d3 from 'd3'
import { onBeforeMount, onMounted, provide, ref, computed, watch, inject } from 'vue';
import { useNamespace } from '@/utils/useNamespace';

import createChart from './chart'
import { currentActiveNode } from './chart'
import { getCourses, getData, getDataByArbitraryId } from '@/utils/apis';
import type { Link, Node } from './node';
import graph from '@/assets/data/data.json'

const props = defineProps({
    width: {
        type: Number
    },
    height: {
        type: Number
    }
})

const ns = useNamespace('graph')

const i = inject('i')


const currentCourse = ref('1')
const data = ref<{ nodes: Array<Node>, links: Array<Link> }>({})

const courses = ref({})
const sim = ref({})

provide('courses', courses)
onBeforeMount(async () => {
    courses.value = (await getCourses()).nodes.map((node: Node) => {
        return {
            id: node.id,
            name: node.properties.name
        }
    })
})

const stopSim = () => {
    const svg = d3.select('#kg-svg')
    svg.selectAll('*').remove()
    sim.value?.stop()
}

const startSim = async () => {
    data.value = await getDataByArbitraryId(currentActiveNode.value)
    console.log(data.value)
    sim.value = createChart(data.value).simulation
}

watch(() => i, () => {
    if (i !== 1) {
        stopSim()
    } else {
        startSim()
    }
})



onMounted(async () => {
    startSim()
})


const handleClickCourse = async (id: string) => {
    currentCourse.value = id
    currentActiveNode.value = id
    stopSim()
    startSim()
}

// const currentShowNode = ref(null)

const currentShowNode = computed(() => {
    if (data.value.nodes) {
        return data.value?.nodes.find(item => item.id === currentActiveNode.value)
    }
    else {
        return null
    }
})

const handleClickReset = async () => {
    currentActiveNode.value = currentCourse.value
    stopSim()
    startSim()
}


const handleClickSetRoot = async () => {
    console.log(currentActiveNode.value)
    stopSim()
    startSim()
}




provide('clickCourse', handleClickCourse)
provide('cur', currentShowNode)

provide('reset', handleClickReset)
provide('setRoot', handleClickSetRoot)











</script>

<style scoped></style>