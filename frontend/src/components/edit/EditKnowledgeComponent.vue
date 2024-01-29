<template>
  <v-container>
    <div v-if="props.items.length > LIMIT" class="text-center">
      <v-pagination v-model="current" :length="Math.ceil(props.items.length / LIMIT)" :total-visible="4" />
    </div>
    <template v-for="(mapping, index) in targetItems()" :key="index">
      <v-card class="pa-2 mb-6">
        <v-card-text>
          <knowledge-mapping-table-component
            :item="mapping"
            @edit="edit()"
            @remove="emit('remove', mapping.knowledge.knowledge_id)"
          />
        </v-card-text>
      </v-card>
    </template>
    <div v-if="props.items.length > LIMIT" class="text-center">
      <v-pagination v-model="current" :length="Math.ceil(props.items.length / LIMIT)" :total-visible="4" />
    </div>
  </v-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import KnowledgeMappingTableComponent from '@/components/edit/KnowledgeMappingTableComponent.vue';
import KnowledgeMapping from '@/models/schema/libz/KnowledgeMapping';

const LIMIT: number = 10;

const current = ref<number>(1);

const targetItems = (): KnowledgeMapping[] => {
    const start = (current.value - 1) * LIMIT;
    const end = Math.min(start + LIMIT, props.items.length);
    return props.items.slice(start, end);
};

const edit = () => {
    // TOOD
};

const emit = defineEmits<{
    remove: [ number ],
}>();

const props = defineProps<{
    items: readonly KnowledgeMapping[],
}>();
</script>
