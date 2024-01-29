<template>
  <v-dialog v-model="dialog" persistent width="100vw">
    <v-progress-circular :indeterminate="loading" class="mx-auto" :size="80" color="monochirome" />
  </v-dialog>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from 'vue';

const dialog = ref<boolean>(false);

const props = defineProps<{
    loading: boolean,
}>();

watchEffect(() => {
    dialog.value = props.loading;
});
</script>
