<template>
    <div>
        <Nav :items="items"></Nav>
        <Main desc="开始您的个性化学习之旅！"></Main>
    </div>
</template>

<script setup lang="ts">
import Nav from '@/components/Guide/Nav.vue';
import Main from '@/components/Guide/Main.vue';
import { useRouter } from 'vue-router'

const router = useRouter()

router.beforeEach((to, from) => {
    if (to.hash) {
        const elem = document.querySelector(to.hash)
        if (elem) {
            elem.scrollIntoView({ behavior: 'smooth' })
        }
    }
})

// const items = ['开始', '知识图谱', '智能问答', '路径推荐']


const items = [
    {
        msg: '开始',
        func: () => {
            router.push("#start")
        }
    },
    {
        msg: '知识图谱',
        func: () => {
            router.push("#kg")
        }
    },
    {
        msg: '智能问答',
        func: () => {
            router.push("#qa")
        }
    },
    {
        msg: '路径推荐',
        func: () => {
            router.push("#path")

        }
    }
]


</script>

<style scoped></style>