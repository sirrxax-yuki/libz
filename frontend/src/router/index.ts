import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { useAuthStore } from '@/store/auth';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        name: 'Search',
        path: '',
        meta: { requiresAuth: true },
        component: () => import('@/views/Search.vue'),
      },
      {
        name: 'Post',
        path: '/post',
        meta: { requiresAuth: true },
        component: () => import('@/views/Post.vue'),
      },
      {
        name: 'Edit',
        path: '/edit',
        meta: { requiresAuth: true },
        component: () => import('@/views/Edit.vue'),
      },
    ],
  },
  {
    name: 'Login',
    path: '/login',
    component: () => import('@/components/rsi/RSILoginComponent.vue'),
  },
  {
    name: 'LoginRedirect',
    path: '/login/redirect',
    component: () => import('@/components/rsi/RSILoginRedirectComponent.vue'),
  },
  {
    name: 'Logout',
    path: '/logout',
    component: () => import('@/components/rsi/RSILogoutComponent.vue'),
  },
  {
    name: 'LoginError',
    path: '/login/error',
    component: () => import('@/components/rsi/RSILoginErrorComponent.vue'),
  },
  {
    name: 'NotFound',
    path: '/:pathMatch(.*)*',
    component: () => import('@/views/NotFound.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Setup redirect.
router.beforeResolve(async (to, from, next) => {
  if (to.matched.some((r) => r.meta.requiresAuth)) {
    if (import.meta.env.VITE_ENABLE_AUTH !== 'false' && !useAuthStore().active) {
      return next({ path: '/login' });
    }
  }
  return next();
});

export default router;
