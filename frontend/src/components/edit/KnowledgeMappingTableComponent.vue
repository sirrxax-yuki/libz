<template>
  <v-table>
    <thead class="table-header">
      <tr>
        <td class="text-left hide-on-smartphone" width="30%">{{ TABLE_HEADER_KEYWORD }}</td>
        <td class="text-left">{{ TABLE_HEADER_KNOWLEDGE }}</td>
        <td class="text-center" width="96">
          <v-btn v-if="false" color="primary" @click.stop="emit('edit')">
            <v-icon :icon="mdiPencil" />
          </v-btn>
        </td>
        <td class="text-center" width="96">
          <knowledge-mapping-delete-button-component @remove="emit('remove')" />
        </td>
      </tr>
    </thead>
    <tbody class="table-record-01">
      <tr v-for="(keyword, index) in item.keywords" :key="index">
        <td class="px-6 text-left hide-on-smartphone">
          {{ keyword }}
        </td>
        <td v-if="index === 0" class="px-6 text-left" :rowspan="item.keywords.length" colspan="3">
          <knowledge-text-component :text="item.knowledge.contents" />
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script lang="ts" setup>
import { mdiPencil } from '@mdi/js';
import KnowledgeTextComponent from '@/components/common/KnowledgeTextComponent.vue';
import KnowledgeMappingDeleteButtonComponent from '@/components/edit/KnowledgeMappingDeleteButtonComponent.vue';
import KnowledgeMapping from '@/models/schema/libz/KnowledgeMapping';

const TABLE_HEADER_KEYWORD = 'Keyword';
const TABLE_HEADER_KNOWLEDGE = 'Knowlegde';

const emit = defineEmits<{
    edit: [],
    remove: [],
}>();

defineProps<{
    item: KnowledgeMapping,
}>();
</script>
