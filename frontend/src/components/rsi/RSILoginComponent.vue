<template>
  <v-app>
    <v-main>
      <v-container class="mt-16">
        Login...
        <RSIAuthController ref="controller" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import RSIAuthController from '@/components/rsi/RSIAuthController.vue';

const router = useRouter();
const controller = ref<InstanceType<typeof RSIAuthController> | null>(null);

const login = async (): Promise<void> => {
    if (await controller.value!.introspectRefreshToken()) {
        await controller.value!.updateAccessToken();
        await controller.value!.requestUserInfo();
        router.push('/');
    }
    else {
        // RSI Auth must access via redirect, not GET request.
        const codeVerifier = controller.value!.createCodeVerifier();
        location.href = controller.value!.createAuthorizeURL(codeVerifier);
    }
};

onMounted(() => {
    login();
});
</script>
