<template>
  <v-table>
    <thead class="table-header">
      <tr>
        <td class="text-left">{{ TABLE_HEADER_KNOWLEDGE }}</td>
        <td class="text-left hide-on-smartphone" width="25%">{{ TABLE_HEADER_USERNAME }}</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in items" :key="index" :class="`table-record-${index % 2 === 0 ? '01' : '02'}`">
        <td class="text-left">
          <knowledge-text-component :text="item.contents" />
        </td>
        <td class="text-left hide-on-smartphone">
          {{ item.user_name }}
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script lang="ts" setup>
import KnowledgeTextComponent from '@/components/common/KnowledgeTextComponent.vue';
import Knowledge from '@/models/schema/libz/Knowledge';

const TABLE_HEADER_KNOWLEDGE: string = 'Knowledge';
const TABLE_HEADER_USERNAME: string = 'Posted By';

defineProps<{
    items: readonly Knowledge[],
}>();
</script>
