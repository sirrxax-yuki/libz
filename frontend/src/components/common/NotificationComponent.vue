<template>
  <div>
  </div>
</template>

<script lang="ts" setup>
import { useToast } from 'vue-toast-notification';
import { AxiosError } from 'axios';
import ErrorResponse from '@/models/schema/libz/ErrorResponse';

const toast = useToast();

const popupInfo = (message: string) => {
    toast.info(message, { position: 'top' });
};

const popupError = (exception: AxiosError) => {
    const error = exception.response?.data as ErrorResponse;
    toast.error(error ? `${error.message} (${error.code})` : "Unknown error.", { position: 'top', duration: 0 });
};

defineExpose({
    popupInfo,
    popupError,
});
</script>
