import { defineStore } from 'pinia';
import Knowledge from '@/models/schema/libz/Knowledge';
import KnowledgeMapping from '@/models/schema/libz/KnowledgeMapping';

export const useKnowledgeStore = defineStore('knowledge', {
    state: () => ({
        search: {
            keyword: '',
            knowledges: [] as Knowledge[],
        },
        post: {
            keywords: [] as string[],
            knowledge: '',
        },
        list: {
            mappings: [] as KnowledgeMapping[],
        },
    }),
});
