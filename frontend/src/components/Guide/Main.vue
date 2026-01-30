<template>
    <div :class="[
        ns.b(),
        ns.is('login', showLogin)
    ]" id="start">
        <div :class="ns.e('content-wrapper')">
            <div :class="[ns.e('title')]">
                <span>{{ title }}</span>
            </div>
            <div :class="[ns.e('sub-title')]">
                <span>Smart Navigation</span>
                <img src="@/assets/pics/ship.png" width="50">
            </div>
            <div :class="[ns.e('desc')]">
                <span>{{ desc }}</span>
            </div>

            <div :class="[ns.e('button-group')]">
                <el-form-item>
                    <el-button type="primary" round :size="buttonSize" @click='buttonClick'>开始航行</el-button>
                </el-form-item>


            </div>
        </div>

        <div :class="[
            ns.e('kg'),
            ns.e('content-wrapper')
        ]" id="kg">
            <div>
                <h1>知识图谱</h1>
                <div style="width: 1000px; padding-left: 100px;"> “智慧学航”学习系统中的知识图谱模块是一张庞大而精密的网络，
                    囊括了计算机专业大学期间的所有课程内容。它以精准的结点和边缘连接了
                    各个课程，为学生提供了一个清晰的知识结构。无论是基础的数据结构与算法，还是
                    高级的人工智能和分布式系统，知识图谱都将这些概念有机地串联在一起，帮助学生
                    理解知识之间的关联性。通过这个模块，学生可以系统地学习各门课程，深入了解计算机科学的精髓，
                    为未来的学习和职业发展打下坚实的基础。
                </div>

            </div>
        </div>

        <div :class="[
            ns.e('qa'),
            ns.e('content-wrapper')
        ]" id="qa">
            <div>
                <h1>智能问答</h1>
                <div style="width: 1000px; padding-left: 100px;">“智慧学航”学系统系统中的智能问答模块是一项强大的工具，利用先进的人工智能技术为学生
                    提供个性化、高效的学习支持。该模块结合了知识图谱涵盖的广泛领域，能够理解学生提出的问题，并针对性
                    地提供详细且迅速准确的解答和解决方案。这种个性化的学习体验，不仅能够提高学生的学习效率，
                    还能够激发学生的学习兴趣，帮助学生更好地掌握计算机专业课程的核心知识。
                </div>
            </div>
        </div>

        <div :class="[
            ns.e('path'),
            ns.e('content-wrapper')

        ]" id="path">
            <div>
                <h1>路径推荐</h1>

                <div style="width: 1000px; padding-left: 100px;">“智慧学航”学习系统中的路径推荐模块旨在为学习者提供专业、科学的学习路径，帮助用户有效地掌握知识和技能，不断
                    提升自己的知识水平和技能。</div>


            </div>
        </div>






        <div :class="[ns.e('image-wrapper')]">

        </div>

    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace';
import { useRouter } from 'vue-router'
import LoginPanel from '@/components/Login/LoginPanel.vue'
import { ref } from 'vue'

const props = defineProps({
    title: {
        type: String,
        default: '智慧学航'
    },
    desc: {
        type: String,
        default: '这是一段关于智慧学航的描述'
    }
})

const ns = useNamespace('main')
const buttonSize = ref('large')
const showLogin = ref(false)

const router = useRouter()

const buttonClick = () => {
    router.push('/home')
}

</script>

<style scoped></style>