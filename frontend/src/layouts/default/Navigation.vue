<template>
  <v-navigation-drawer v-model="visible" :width="128" app temporary>
    <v-list>
      <v-list-item class="mt-12 mb-12 text-center" v-for="(item, index) in items" :key="index">
        <router-link :to="item.route">
          <v-icon class="icon-link" :icon="item.icon" size="x-large" />
        </router-link>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useAuthStore } from '@/store/auth';
import { mdiNoteSearch, mdiNotePlus, mdiNoteEdit } from '@mdi/js';

const store = useAuthStore();

const visible = ref<boolean>(false);
const items = ref<readonly { icon: string, route: string }[]>([
    { icon: mdiNoteSearch, route: '/' },
    { icon: mdiNotePlus, route: '/post' },
    { icon: mdiNoteEdit, route: '/edit' },
]);

const toggle = () => {
    visible.value = store.active ? !visible.value : false;
};

defineExpose({
  toggle,
});
</script>
