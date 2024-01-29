<template>
  <v-container>
    <v-card>
      <div v-if="props.items.length > LIMIT" class="text-center">
        <v-pagination v-model="current" :length="Math.ceil(props.items.length / LIMIT)" :total-visible="4" />
      </div>
      <v-card-text>
        <knowledge-response-table-component :items="targetItems()" />
      </v-card-text>
      <div v-if="props.items.length > LIMIT" class="text-center">
        <v-pagination v-model="current" :length="Math.ceil(props.items.length / LIMIT)" :total-visible="4" />
      </div>
    </v-card>
  </v-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import KnowledgeResponseTableComponent from '@/components/search/KnowledgeResponseTableComponent.vue';
import Knowledge from '@/models/schema/libz/Knowledge';

const LIMIT: number = 10;

const current = ref<number>(1);

const targetItems = (): Knowledge[] => {
    const start = (current.value - 1) * LIMIT;
    const end = Math.min(start + LIMIT, props.items.length);
    return props.items.slice(start, end);
};

const props = defineProps<{
    items: Knowledge[],
}>();
</script>
