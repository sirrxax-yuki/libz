<template>
  <v-app>
    <app-bar @toggle="toggle" />
    <v-main>
      <navigation ref="navigation" />
      <libz-view class="mt-4" />
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import AppBar from './AppBar.vue';
import Navigation from './Navigation.vue';
import LibzView from './View.vue';

const navigation = ref<InstanceType<typeof Navigation> | null>(null);

const toggle = () => {
    navigation.value?.toggle();
};
</script>
