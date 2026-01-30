<template>
    <div :class="[ns.b()]">
        <div :class='ns.e("wrapper")'>

            <IconPanel 
                :msg="msg"
                :src="'@/assets/pics/ship.png'"
                @click="onClickNavIcon"
            ></IconPanel>

            <div :class="[ns.e('items-group')]">
                <div :class="ns.e('item')" v-for="( item, index ) in  items " :key="index" @click="item.func">
                    <span>{{ item.msg }}</span>
                </div>

                <div :class="[ns.e('lang-select-wrapper')]">
                    <span :class="[ns.e('lang-select')]"
                        @click="active = active === 'Chinese' ? 'English' : 'Chinese'">
                        <LanguageOutline></LanguageOutline>
                    </span>
                    <div :class="[ns.e('lang-select-items-wrapper')]">
                        <span :class="[ns.e('lang-select-item'), ns.is('active', active === 'Chinese')]">
                            <Chinese></Chinese>
                        </span>
                        <span :class="[ns.e('lang-select-item'), ns.is('active', active === 'English')]">
                            <English></English>
                        </span>

                    </div>
                </div>
            </div>
        </div>



    </div>
</template>

<script setup lang="ts">
import { useNamespace } from '@/utils/useNamespace';
import { ref, type PropType } from 'vue'
import { useRouter } from 'vue-router';

import { LanguageOutline } from '@vicons/ionicons5'
import Chinese from '@/components/icons/Chinese.vue'
import English from '@/components/icons/English.vue'
import IconPanel from '@/components/icons/IconPanel.vue'

const ns = useNamespace('nav')

interface Item {
    msg: string,
    func?: () => void
}

const props = defineProps({
    items: {
        type: Object as PropType<Item>,
    }
})

const router = useRouter()


// data
const src = ref('@/assets/pics/ship.png')
const msg = ref('智慧学航')

const onClickNavIcon = () => {
    router.push('/guide')
}

const active = ref('Chinese')


</script>
