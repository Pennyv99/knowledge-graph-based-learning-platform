<template>
    <div :class="ns.b()">
        <div :class="ns.e('title')">
            <span>智能问答系统</span>
        </div>
        <div :class="ns.e('content-wrapper')">
            <div :class="ns.e('conver-panel')">
                <div v-for="(item, index) in conver"
                    :style="{ alignSelf: item.type === 'human' ? 'flex-end' : 'flex-start' }" :key="'' + index">
                    <span>{{ item.text }}</span>
                </div>
            </div>

            <div :class="ns.e('text')">
                <!-- <el-input type="textarea" resize="none"></el-input> -->
                <textarea v-model="text" :disabled="inputDisabled" @keyup.enter="handleClickSend"></textarea>
            </div>
            <div :class="ns.e('send')">
                <Button @click="handleClickSend" :disabled="inputDisabled">发送</Button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import Button from '@/components/Common/Button.vue';

import { useNamespace } from '@/utils/useNamespace';
import { getPrecourse, getPath, getAnswer } from '@/utils/apis'
import { ref, reactive } from 'vue'
import axios from 'axios'
import test from 'node:test';

interface FormData {
    course: string
    time: string
}

interface sentence {
    type: string,
    text: string
}

const formData = reactive({
    course: '机器学习',
    time: '8',
    major: '计算机科学与技术'
})

const conver = ref<Array<sentence>>([{
    type: 'computer',
    text: '欢迎来到智能问答系统，有什么能为您服务的吗？'
}])


const text = ref('')
const inputDisabled = ref(false)
const handleClickSend = async () => {
    inputDisabled.value = true
    conver.value.push({
        type: 'human',
        text: text.value
    })
    const temp = text.value

    text.value = ''
    //to do
    const ans = await getAnswer(temp)

    conver.value.push({
        type: 'computer',
        text: ans.data.answer
    })

    inputDisabled.value = false
}










const ns = useNamespace('qa')
</script>

<style lang="scss">
@use '@style/mixins/mixins.scss' as *;

@include b(qa) {
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

        // padding-bottom: 40px;
    }


    @include e(content-wrapper) {
        width: 96%;
        height: 80%;
        background-color: white;

        border-radius: 10px;
        margin: 0 auto;
        position: relative;

        box-sizing: border-box;
        padding: 20px;

    }

    @include e(conver-panel) {
        width: 100%;
        height: 500px;
        border-radius: 5px;
        margin: 0 auto;

        box-sizing: border-box;
        padding: 20px;

        display: flex;
        flex-direction: column;


        overflow: scroll;
        scrollbar-width: auto;
        border: 1px black solid;

        div {
            display: inline-block;
            max-width: 500px;
            font-size: 16px;
            padding: 15px;
            border: gray 1px solid;
            flex-grow: 0;
        }



    }

    @include when(human) {
        align-self: flex-end;
    }

    @include when(computer) {
        align-self: flex-start;
    }

    @include e(send) {
        position: absolute;
        right: 20px;
        bottom: 20px;
    }


}

textarea {
    margin-top: 40px;
    padding: 10px 20px;
    box-sizing: border-box;
    width: 100%;
    height: 100px;
    resize: none;

    font-size: 20px;
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
</style>