import vuetify from './vuetify';
import pinia from '../store';
import router from '../router';
import toast from './toast';
import type { App } from 'vue';

export function registerPlugins (app: App) {
  app
    .use(vuetify)
    .use(router)
    .use(pinia)
    .use(toast)
}
