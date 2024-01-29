<template>
  <v-app>
    <v-main>
      <v-container class="mt-16">
        Login Redirect.
        <RSIAuthController ref="controller" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from "vue-router";
import RSIAuthController from '@/components/rsi/RSIAuthController.vue';

const route = useRoute();
const router = useRouter();
const controller = ref<InstanceType<typeof RSIAuthController> | null>(null);

const initialize = async (): Promise<void> => {
    await controller.value!.requestToken(route.query.code!.toString());
    await controller.value!.requestUserInfo();
    router.push('/');
};

onMounted(() => {
    if (!route.query.error) {
        initialize();
    }
    else {
        controller.value!.errorHandler("RSI Authentication Error.");
    }
});
</script>
