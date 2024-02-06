<template>
  <v-container>
    <loading-circle-component :loading="loading" />
    <v-container>
      <v-card class="py-2">
        <v-card-text>
          <v-text-field v-model="keyword" label="Keyword" @keypress.enter="onSearch" :rules="[ v => v.length <= 50 || 'Max 50 characters.', v => !!v || 'Keyword is required.' ]" />
        </v-card-text>
        <v-container>
          <v-btn class="text-transform-none" height="48" color="monochrome" block :disabled="lock()" @click="onSearch">
            <v-icon :icon="mdiMagnify" size="x-large" />
          </v-btn>
        </v-container>
      </v-card>
    </v-container>
    <search-result-pagenation-component v-if="showResult" :items="knowledges" />
    <notification ref="notification" />
  </v-container>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from 'vue';
import { useAuthStore } from '@/store/auth';
import { useKnowledgeStore } from '@/store/knowledge';
import { mdiMagnify } from '@mdi/js';
import axios, { AxiosResponse, AxiosError } from 'axios';
import SearchResultPagenationComponent from '@/components/search/SearchResultPagenationComponent.vue';
import LoadingCircleComponent from '@/components/common/LoadingCircleComponent.vue';
import Notification from '@/components/common/NotificationComponent.vue';
import SearchResponse from '@/models/schema/libz/SearchResponse';
import Knowledge from '@/models/schema/libz/Knowledge';

const store = {
    auth: useAuthStore(),
    knowledge: useKnowledgeStore(),
};
const notification = ref<InstanceType<typeof Notification> | null>(null);
  
const loading = ref<boolean>(false);
const showResult = ref<boolean>(false);

const keyword = ref<string>('');
const knowledges = ref<Knowledge[]>([]);

const lock = (): boolean => {
    return loading.value || !keyword.value;
};

const onSearch = () => {
    if (lock()) {
        return;
    }
    showResult.value = false;
    loading.value = true;
    const request = {
        user: store.auth.user,
        keyword: keyword.value,
    };
    const start = Date.now();
    axios.post('/api/search', request)
    .then((response: AxiosResponse<SearchResponse>) => {
        store.knowledge.search.keyword = keyword.value;  
        store.knowledge.search.knowledges = response.data.results;
        console.log(`/api/search : ${Date.now() - start} sec.`);
        if (response.data.results.length !== 0) {
            showResult.value = true;
        }
        else {
            notification.value?.popupInfo("Not Found.");
        }
    })
    .catch((e: AxiosError) => notification.value?.popupError(e))
    .finally(() => loading.value = false);
};

watchEffect(() => {
    knowledges.value = store.knowledge.search.knowledges;
});
</script>
