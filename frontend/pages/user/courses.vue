<script setup>
definePageMeta({
    middleware: "logged-users-only",
});

useHead({
    title: "Мои курсы | Xiver education",
});

const coursesPlateMsg = ref("");

const { data: courses_data } = await useAsyncData(
    'where_am_i',
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/me/where_am_i"
        else api_url = "/api/course/me/where_am_i"
        return $fetch( 
            api_url,
            { headers: headers },
        )
    },
);

if (!courses_data.value) {
    coursesPlateMsg.value = "Нет курсов, удовлетворяющих вашим условиям.";
}

const onFlagChanged = async () => {
    let filtr = null;

    const studing = document.getElementById("studingSwitch").checked;
    const teaching = document.getElementById("teachingSwitch").checked;

    if (studing && teaching) {
        filtr = "all";
    } else if (studing) {
        filtr = "student";
    } else if (teaching) {
        filtr = "teacher";
    }

    if (filtr) {
        const { data: courses_data } = await useAsyncData(
            'where_am_i',
            () => {
                const headers = useRequestHeaders()

                let api_url = ''
                if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/me/where_am_i"
                else api_url = "/api/course/me/where_am_i"
                return $fetch( 
                    api_url,
                    { headers: headers, query: { role: filtr } },
                )
            },
        );
        courses_data.value = courses_data.value;
        if (courses_data.value) {
            coursesPlateMsg.value = null;
        } else {
            courses_data.value = "Нет курсов, удовлетворяющих вашим условиям.";
        }
    } else {
        coursesPlateMsg.value = "Нет курсов, удовлетворяющих вашим условиям.";
    }
};
</script>


<template>
    <div>
        <h1 class="text-center mt-5 mb-5">Список курсов</h1>
        <div class="container align-items-center justify-content-center items-center">
            <div class="row">
                <div class="col-2 rounded shadow btn-group-vertical mr-5 p-2 second-float justify-content-start" role="group"
                    aria-label="Basic checkbox toggle button group">
                    <h4 class="mb-3">Фильтры</h4>

                    <div class="form-check form-switch">
                        <input id="studingSwitch" class="form-check-input" type="checkbox" role="switch" checked
                            @change="onFlagChanged" />
                        <label class="form-check-label" for="studingSwitch">Учусь</label>
                    </div>
                    <div class="form-check form-switch">
                        <input id="teachingSwitch" class="form-check-input" type="checkbox" role="switch"
                            @change="onFlagChanged" />
                        <label class="form-check-label" for="teachingSwitch">Преподаю</label>
                    </div>
                </div>
                <div class="col-1"></div>
                <div v-if="coursesPlateMsg" class="col-9 shadow rounded ml-5 p-3 second-float">
                    {{ coursesPlateMsg }}
                </div>
                <div v-else class="col-9 shadow rounded ml-5 p-3 second-float">
                    <ListCoursesCarusel :data="courses_data" />
                </div>
            </div>
        </div>
    </div>
</template>
