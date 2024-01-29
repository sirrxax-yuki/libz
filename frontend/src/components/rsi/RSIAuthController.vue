<template>
  <div>
  </div>
</template>

<script lang="ts" setup>

// Handle access to store, local-storage, and model from RSI component.

import { useRouter } from "vue-router";
import { useAuthStore } from '@/store/auth';
import rsi from '@/models/util/rsi-auth';

const router = useRouter();
const store = useAuthStore();

const commonHandler = async (operation: Function): Promise<void> => {
    try {
        await operation();
    }
    catch (e: any) {
        errorHandler(rsi.errorHandler(e));
    }
};

const errorHandler = (errorMessage: string): void => {
    store.error = errorMessage;
    router.push('/login/error');
};

const requestUserInfo = async (): Promise<void> => {
    await commonHandler(async () => {
        const accessToken = localStorage.getItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_ACCESS_TOKEN);
        if (!accessToken) {
            throw new Error("RSI Access-Token Expired.");
        }
        store.user.data = await rsi.requestUserInfo(accessToken);
        store.active = true;
    });
};

const requestToken = async (authorizationCode: string): Promise<void> => {
    await commonHandler(async () => {
        const codeVerifier = localStorage.getItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_CODE_VERIFIER);
        if (!codeVerifier) {
            throw new Error("RSI Authorization Expired.");
        }
        const token = await rsi.requestToken(codeVerifier, authorizationCode);
        localStorage.setItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_ACCESS_TOKEN, token.access_token);
        localStorage.setItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_REFRESH_TOKEN, token.refresh_token);
    });
};

const introspectRefreshToken = async (): Promise<boolean> => {
    const refreshToken = localStorage.getItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_REFRESH_TOKEN);
    return refreshToken != null && await rsi.introspectToken(refreshToken);
};

const updateAccessToken = async (): Promise<void> => {
    const refreshToken = localStorage.getItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_REFRESH_TOKEN);
    if (!refreshToken) {
        throw new Error("RSI Refresh-Token Expired.");
    }
    await commonHandler(async () => {
        const token = await rsi.updateAccessToken(refreshToken);
        localStorage.setItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_ACCESS_TOKEN, token.access_token);
    });
};

const revokeAccessToken = async (): Promise<void> => {
    const accessToken = localStorage.getItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_ACCESS_TOKEN);
    localStorage.removeItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_ACCESS_TOKEN);
    localStorage.removeItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_REFRESH_TOKEN);
    localStorage.removeItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_CODE_VERIFIER);
    if (accessToken) {
        await commonHandler(async () => {
            await rsi.revokeAccessToken(accessToken);
        });
    }
};

const createAuthorizeURL = (codeVerifier: string): string => {
    return rsi.createAuthorizeURL(codeVerifier);
};

const createLogoutURL = (codeVerifier: string): string => {
    return rsi.createLogoutURL(codeVerifier);
};

const createCodeVerifier = (): string => {
    const codeVerifier = rsi.createCodeVerifier();
    localStorage.setItem(import.meta.env.VITE_LOCAL_STORAGE_KEY_CODE_VERIFIER, codeVerifier);
    return codeVerifier;
};

defineExpose({
    requestUserInfo,
    requestToken,
    introspectRefreshToken,
    updateAccessToken,
    revokeAccessToken,
    createAuthorizeURL,
    createLogoutURL,
    createCodeVerifier,
    errorHandler,
});
</script>
