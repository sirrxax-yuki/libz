<template>
  <v-container>
    <loading-circle-component :loading="loading" />
    <v-container>
      <v-card class="py-2">
        <v-card-text>
          <keyword-field-component v-model:keywords="keywords" @remove="removeKeywordField" />
        </v-card-text>
        <v-card-text>
          <v-btn class="text-transform-none" tabindex="-1" height="48" block @click="appendKeywordField">
            <v-icon :icon="mdiPlus" size="x-large" />
          </v-btn>
        </v-card-text>
        <v-card-text>
          <v-divider class="my-4"></v-divider>
        </v-card-text>
        <v-card-text>
          <v-textarea v-model="knowledge" label="Knowledge" counter :rules="[ v => v.length <= 300 || 'Max 300 characters.' ]" />
        </v-card-text>
        <v-container>
          <v-btn class="text-transform-none" height="48" color="monochrome" block :disabled="lock()" @click="onPost">
            <v-icon :icon="mdiSendVariant" size="x-large" />
          </v-btn>
        </v-container>
      </v-card>
    </v-container>
    <post-knowledge-component v-if="showResult" :item="posted" />
    <notification ref="notification" />
  </v-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useAuthStore } from '@/store/auth';
import { mdiPlus, mdiSendVariant } from '@mdi/js';
import axios, { AxiosError } from 'axios';
import KeywordFieldComponent from '@/components/post/KeywordFieldComponent.vue';
import PostKnowledgeComponent from '@/components/post/PostKnowledgeComponent.vue';
import LoadingCircleComponent from '@/components/common/LoadingCircleComponent.vue';
import Notification from '@/components/common/NotificationComponent.vue';
import PostRequest from '@/models/schema/libz/PostRequest';

const store = useAuthStore();
const notification = ref<InstanceType<typeof Notification> | null>(null);
  
const loading = ref<boolean>(false);
const showResult = ref<boolean>(false);

const keywords = ref<string[]>([ '' ]);
const knowledge = ref<string>('');
const posted = ref<{ keywords: readonly string[], knowledge: string }>({
    keywords: [],
    knowledge: '',
});

const lock = (): boolean => {
    return loading.value || keywords.value.some((k) => !k) || !knowledge.value;
};

const appendKeywordField = () => {
    keywords.value.push('');
};

const removeKeywordField = (index: number) => {
    keywords.value.splice(index, 1);
};

const clear = () => {
    keywords.value = keywords.value.map(() => '');
    knowledge.value = '';
};

const onPost = () => {
    if (lock()) {
        return;
    }
    showResult.value = false;
    loading.value = true;
    const request: PostRequest = {
        user: store.user,
        keywords: keywords.value,
        knowledge: knowledge.value.trim().replaceAll('\n+', '\n'),
        knowledge_type: 'text',
        private: false,
    };
    axios.post('/api/post', request)
    .then(() => {
        posted.value.keywords = keywords.value.map((k) => k);
        posted.value.knowledge = knowledge.value;
        showResult.value = true;
        clear();
    })
    .catch((e: AxiosError) => notification.value?.popupError(e))
    .finally(() => loading.value = false);
};
</script>
