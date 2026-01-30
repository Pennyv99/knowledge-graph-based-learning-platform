import type { ExtractPropTypes } from 'vue'

export interface Node {
    id: string
    label: string
    properties: {
        name: string
        description: string
    }
}

export interface Link {
    source: string
    target: string
    type: string
}

export const colors = {
    课程: '#902921',
    章节: '#294853',
    节: '#837451',
    小节: '#f8ad19'
}

export const radius = {
    课程: 50,
    章节: 40,
    节: 30,
    小节: 25
}
