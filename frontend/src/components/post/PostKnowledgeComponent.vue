<template>
  <v-container>
    <v-card class="pa-2">
      <v-card-text>
        <v-table>
          <thead class="table-header">
            <tr>
              <td class="text-left hide-on-smartphone" width="30%">{{ TABLE_HEADER_KEYWORD }}</td>
              <td class="text-left">{{ TABLE_HEADER_KNOWLEDGE }}</td>
            </tr>
          </thead>
          <tbody class="table-record-01">
            <tr v-for="(keyword, index) in item.keywords" :key="index">
              <td class="px-6 text-left hide-on-smartphone">
                {{ keyword }}
              </td>
              <td v-if="index === 0" class="px-6 text-left" :rowspan="item.keywords.length">
                <knowledge-text-component :text="item.knowledge" />
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts" setup>
import KnowledgeTextComponent from '@/components/common/KnowledgeTextComponent.vue';

const TABLE_HEADER_KEYWORD = 'Keyword';
const TABLE_HEADER_KNOWLEDGE = 'Knowlegde';

defineProps<{
    item: { keywords: readonly string[], knowledge: string },
}>();
</script>
