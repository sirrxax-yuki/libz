<template>
  <v-container>
    <loading-circle-component :loading="loading" />
    <edit-knowledge-component v-if="showResult" :items="knowledges" @remove="onRemove" />
    <notification-component ref="notification" />
  </v-container>
</template>

<script lang="ts" setup>
import { ref, onMounted, watchEffect } from 'vue';
import { useAuthStore } from '@/store/auth';
import { useKnowledgeStore } from '@/store/knowledge';
import axios, { AxiosResponse, AxiosError } from 'axios';
import EditKnowledgeComponent from '@/components/edit/EditKnowledgeComponent.vue';
import LoadingCircleComponent from '@/components/common/LoadingCircleComponent.vue';
import NotificationComponent from '@/components/common/NotificationComponent.vue';
import ListResponse from '@/models/schema/libz/ListResponse';
import DeleteResponse from '@/models/schema/libz/DeleteResponse';
import KnowledgeMapping from '@/models/schema/libz/KnowledgeMapping';

const store = {
    auth: useAuthStore(),
    knowledge: useKnowledgeStore(),
};
const notification = ref<InstanceType<typeof NotificationComponent> | null>(null);

const loading = ref<boolean>(false);
const showResult = ref<boolean>(false);

const knowledges = ref<readonly KnowledgeMapping[]>([]);

const lock = (): boolean => {
    return loading.value;
};

const fetchKnowledges = (): void => {
    if (lock()) {
        return;
    }
    showResult.value = false;
    loading.value = true;
    const request = {
        user: store.auth.user,
    };
    axios.post('/api/list', request)
    .then((response: AxiosResponse<ListResponse>) => {
        store.knowledge.list.mappings = response.data.results;
        if (response.data.results.length !== 0) {
            showResult.value = true;
        }
        else {
            notification.value?.popupInfo("No Items.");
        }
    })
    .catch((e: AxiosError) => notification.value?.popupError(e))
    .finally(() => loading.value = false);
};

const onRemove = (knowledgeID: number) => {
    if (lock()) {
        return;
    }
    showResult.value = false;
    loading.value = true;
    const request = {
        user: store.auth.user,
        knowledge_id: knowledgeID,
    };
    axios.delete('/api/delete', { data: request })
    .then((response: AxiosResponse<DeleteResponse>) => {
        store.knowledge.list.mappings = response.data.update;
        if (response.data.update.length !== 0) {
            showResult.value = true;
        }
        else {
            notification.value?.popupInfo("No Items.");
        }
    })
    .catch((e: AxiosError) => notification.value?.popupError(e))
    .finally(() => loading.value = false);
};

onMounted(() => {
    fetchKnowledges();
});

watchEffect(() => {
    knowledges.value = store.knowledge.list.mappings;
});
</script>
