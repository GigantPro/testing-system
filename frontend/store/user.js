import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore('user', () => {
    const user = ref({
        name: '123',
        sername: '456'
    })
});

