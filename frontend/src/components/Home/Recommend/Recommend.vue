<template>
    <div :class="ns.b()">
        <div :class="ns.e('title')">
            <span>智能学习路径推荐系统</span>
        </div>
        <div :class="ns.e('content-wrapper')" v-if="courseVisible">
            <el-form :model="formData">
                <el-form-item prop="course" label="想学习的课程">
                    <el-input v-model="formData.course"></el-input>
                </el-form-item>
                <el-form-item prop="time" label="预期学习周期">
                    <el-input v-model="formData.time">
                        <template #append>
                            <span>周</span>
                        </template>
                    </el-input>
                </el-form-item>
                <Button @click="handleClickGetPrecourse">提交</Button>
            </el-form>


            <div :class="ns.e('courses')" v-if="precourse.length > 0">
                <div :class="ns.e('course-title')">
                    <span>请选择已经学习过的课程</span>
                </div>

                <el-checkbox-group v-model="selectedCourses">
                    <el-checkbox v-for="course in precourse" :label="course" :value="course" :key="course">
                    </el-checkbox>
                </el-checkbox-group>

                <div :class="ns.e('get-path')">
                    <Button @click="handleClickGetPath">
                        提交
                    </Button>
                </div>
            </div>

        </div>

        <div :class="ns.e('path')" v-if="!courseVisible">
            <div :class="ns.e('path-header')">
                <span>根据您的学期情况，推荐学习路径为：
                    <span v-for="(item, index) in pathCourse" :key="item">
                        <span v-if="index !== 0">-></span>{{ item }}
                    </span>
                </span>
                <span>为您规划的学习计划表：</span>
            </div>

            <div :class="ns.e('path-table')">
                <el-table :data="path" border>
                    <el-table-column prop="time" label="时间" align="center"></el-table-column>
                    <el-table-column prop="course" label="课程" align="center"></el-table-column>
                    <el-table-column prop="knowledge" label="知识点" align="center"></el-table-column>
                </el-table>
                <div>

                </div>
            </div>

        </div>

    </div>
</template>

<script setup lang="ts">
import Button from '@/components/Common/Button.vue';

import { useNamespace } from '@/utils/useNamespace';
import { getPrecourse, getPath } from '@/utils/apis'
import { ref, reactive } from 'vue'
import axios from 'axios'
import KnowledgeGraph from '../KG/KnowledgeGraph.vue';

interface FormData {
    course: string
    time: string
}

const formData = reactive({
    course: '机器学习',
    time: '8',
    major: '计算机科学与技术'
})

const courseVisible = ref(true)

const precourse = ref([])
const selectedCourses = ref([])

const pathCourse = ref([])

const handleClickGetPrecourse = async () => {
    const body = {
        course: formData.course,
        time: formData.time + '周',
        major: formData.major
    }
    console.log("click get precourse", body)
    const resp = await getPrecourse(body)
    console.log(resp)
    precourse.value = resp.precourse


    precourse.value.knowledge = precourse.value.knowledge.map(item => {
        return item.replace('<br>', '')
    })

}

const path = ref([


])
const pre = []

const handleClickGetPath = async () => {
    const pre: Array<String> = []
    path.value = []
    pre.push(...selectedCourses.value)
    const body = {
        course: formData.course,
        time: formData.time + '周',
        major: formData.major,
        precourse: pre
    }
    console.log("click get path", body)
    const raw = await getPath(body)
    console.log(raw)
    pathCourse.value = raw.course.filter((item, index, array) => {
        return array.indexOf(item) === index
    })


    const len = raw.time.length

    for (let i = 0; i < len; i++) {
        path.value.push({})
        path.value[i].time = raw.time[i]
        path.value[i].course = raw.course[i]
        path.value[i].knowledge = raw.knowledge[i]
    }

    console.log(path.value)

    courseVisible.value = false
}



const ns = useNamespace('recommend')
</script>

<style lang="scss">
@use '@style/mixins/mixins.scss' as *;

@include b(recommend) {
    width: 1400px;
    height: 900px;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 30px;

    background-color: rgb(228, 228, 228);
    margin-top: 200px;


    @include e(title) {
        width: 100%;
        height: 60px;
        font-size: 40px;
        display: flex;
        align-items: center;
        align-self: flex-start;

        padding-bottom: 40px;
    }

    @include e(content-wrapper) {
        width: 94%;
        height: 80%;
        background-color: white;

        margin: 0 auto;



        .el-form {
            display: flex;
            align-items: center;
            justify-content: space-around;
        }

        .el-form-item {
            margin: 0;
        }

        .el-form-item__label {
            font-size: 20px;
        }

        .el-input {
            width: 300px;
            height: 40px;
        }

        .el-input__inner {
            font-size: 16px;
        }



    }



    @include e(courses) {
        background-color: $color-main;
        width: 90%;
        height: 90%;

        box-sizing: border-box;
        padding: 20px;
        margin: 0 auto;

        position: relative;

    }

    @include e(course-title) {
        font-size: 40px;
        color: $color-white;
    }

    @include e(path) {
        width: 94%;
        height: 80%;
        display: flex;
        flex-direction: column;
        margin: 0 auto;

    }

    @include e(path-header) {
        font-size: 32px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        height: 130px;
    }

    @include e(path-table) {
        width: 100%;
        display: flex;
        flex-direction: column;


        align-items: center;
    }

    @include e(get-path) {
        position: absolute;
        right: 20px;
        bottom: 20px;
    }
}



.el-checkbox__label {
    font-size: 40px;
    color: $color-white;
}

.el-checkbox {
    width: 40%;
    height: 50px;
}

.el-checkbox__inner {
    width: 20px;
    height: 20px;

    &::after {
        left: 5px;
        height: 12px;
    }

}



.el-table__inner-wrapper {

    th,
    td {
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        background-color: rgb(239, 239, 239);
    }
}
</style>