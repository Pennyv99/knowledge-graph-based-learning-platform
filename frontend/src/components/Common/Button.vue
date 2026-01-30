<template>
    <div :class="ns.b()">

        <span :class="ns.e('label')">
            <slot></slot>

        </span>
    </div>
</template>

<script setup lang="ts">

import { useNamespace } from '@/utils/useNamespace';


const ns = useNamespace('button')
</script>

<style lang="scss">
@use '@style/mixins/mixins.scss' as *;

@include b(button) {
    width: 120px;
    height: 40px;

    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;

    background-color: $color-main-active;
    border: 2px solid $color-main;

    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    border-radius: 10px;
    font-weight: bold;
    color: $color-main;

    &:hover {
        background-color: $color-main-hover;
        cursor: pointer;
    }

    &:active {
        background-color: $color-sub;

    }


    margin: 5px 10px;

}
</style>