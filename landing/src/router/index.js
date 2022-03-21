import { createRouter, createWebHistory } from "vue-router";
import HomeSection from "../components/HomeSection.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeSection,
        }
    ],
});

export default router;
