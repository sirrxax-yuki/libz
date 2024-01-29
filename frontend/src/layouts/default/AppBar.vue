<template>
  <v-app-bar class="px-3" app dark>
    <v-app-bar-nav-icon tabindex="-1" @click.stop="emit('toggle')" />
    <router-link class="mt-1 ml-8 text-decoration-none title" tabindex="-1" to="/">
      Libz Search
    </router-link>
    <template v-slot:append>
      <v-menu location="bottom">
        <template v-slot:activator="{ props }">
          <v-icon v-if="ENABLE_LOGOUT" v-bind="props" class="mx-4" tabindex="-1" :icon="mdiCog" size="x-large" />
        </template>
        <v-list min-width="96">
          <v-list-item class="mt-4 mb-4 text-center">
            <router-link to="/logout">
              <v-icon class="icon-link" :icon="mdiLogout" size="large" />
            </router-link>
          </v-list-item>
        </v-list>
      </v-menu>
    </template>
  </v-app-bar>
</template>

<script lang="ts" setup>
import { mdiCog, mdiLogout } from '@mdi/js';

const ENABLE_LOGOUT = import.meta.env.VITE_ENABLE_AUTH !== 'false';

const emit = defineEmits<{
    toggle: [],
}>();
</script>

<style scoped>
.title {
  font-family: 'Arrancar', monospace;
  font-size: 1.6rem;
  color: rgb(var(--v-theme-basetext));
}
</style>
