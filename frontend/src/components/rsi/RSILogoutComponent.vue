<template>
  <v-app>
    <v-main>
      <v-container class="mt-16">
        Logout.
        <RSIAuthController ref="controller" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import RSIAuthController from '@/components/rsi/RSIAuthController.vue';

const controller = ref<InstanceType<typeof RSIAuthController> | null>(null);

const logout = async (): Promise<void> => {
    controller.value!.revokeAccessToken().then(() => {
        // RSI Auth must access via redirect, not GET request.  
        const codeVerifier = controller.value!.createCodeVerifier();
        location.href = controller.value!.createLogoutURL(codeVerifier);
    });
};

onMounted(() => {
    logout();
});
</script>
