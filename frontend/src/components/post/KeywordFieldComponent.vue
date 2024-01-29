<template>
  <template v-for="index in keywords.map((_, i) => i)" :key="index">
    <v-row align-items="stretch">
      <v-col class="pr-0">
        <v-text-field v-model="keywords[index]" height="56" label="Keyword" :rules="[ v => v.length <= 50 || 'Max 50 characters.' ]" />
      </v-col>
      <v-col class="text-center remove-button">
        <v-btn tabindex="-1" height="56" flat @click="emit('remove', index)">
          <v-icon v-if="index !== 0" :icon="mdiTrashCanOutline" size="x-large" />
        </v-btn>
      </v-col>
    </v-row>
  </template>
</template>

<script lang="ts" setup>
import { mdiTrashCanOutline } from '@mdi/js';

const emit = defineEmits<{
    remove: [ number ],
}>();

defineProps<{
    keywords: string[],
}>();
</script>

<style scoped>
.remove-button {
  max-width: 96px;
}
</style>
