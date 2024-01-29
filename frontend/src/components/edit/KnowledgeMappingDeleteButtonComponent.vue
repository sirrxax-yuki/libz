<template>
  <v-menu location="top">
    <template v-slot:activator="{ props }">
      <v-btn v-bind="props" color="alert">
        <v-icon :icon="mdiTrashCanOutline" />
      </v-btn>
    </template>
    <v-list>
      <v-list-item>
        <v-icon :icon="mdiTrashCanOutline" size="x-large" color="alert" @click.stop="emit('remove')" />
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script lang="ts" setup>
import { mdiTrashCanOutline } from '@mdi/js';

const emit = defineEmits<{
    remove: [],
}>();
</script>
