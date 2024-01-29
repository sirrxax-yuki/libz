<template>
  <v-app>
    <v-main>
      <v-container class="mt-16">
        Login Error.
        <v-container>
          {{ message }}
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from 'vue';
import { useAuthStore } from '@/store/auth';

const store = useAuthStore();

const message = ref<string>('');

watchEffect(() => {
    message.value = store.error;
});
</script>
