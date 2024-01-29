import { defineStore } from 'pinia';
import User from '@/models/schema/libz/User';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        active: import.meta.env.VITE_ENABLE_AUTH === 'false',
        user: { data: {} } as User,
        error: '',
    }),
});
