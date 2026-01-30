import GuideView from '@/views/Guide/GuideView.vue'
import HomeView from '@/views/Home/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            redirect: '/guide'
        },
        {
            path: '/guide',
            name: 'guide',
            component: GuideView
        },
        {
            path: '/home',
            name: 'home',
            component: HomeView
        }
    ]
})



export default router
