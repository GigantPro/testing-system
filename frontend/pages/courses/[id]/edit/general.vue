<script setup>
const route = useRoute()

const pending = ref(false)
const refresh = ref(false)

const title = ref(null)
const description = ref(null)

watch(refresh, async (val) => {
    if (!val) return
    const { data: course_data } = useAsyncData(
        'course_data_' + route.params.id,
        () => {
            const headers = useRequestHeaders()

            let api_url = ''
            if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/get/"
            else api_url = "/api/course/get/"

            api_url = api_url + route.params.id

            return $fetch(
                api_url,
                { headers: headers },
            )
        },
    );
    watch(course_data, (course_data) => {
        console.log(course_data);
        title.value = course_data.title
        description.value = course_data.description
    })
    refresh.value = false
})

refresh.value = true

// Functions
const onSaveChanges = async (e) => {
    pending.value = true
    const titleInput = document.getElementById('titleInput')
    const descriptonInput = document.getElementById('descriptonInput')
    const { data: server_answer, error } = useAsyncData(
        'course_update_' + route.params.id,
        () => {
            const headers = useRequestHeaders()

            const api_url = '/api/course/update'
            return $fetch(
                api_url,
                {
                    headers: headers,
                    method: "POST",
                    body: {
                        id: route.params.id,
                        title: titleInput.value,
                        description: descriptonInput.value
                    }
                },
            )
        },
    );
    const successNotifyElem = document.getElementById('successNotify')
    const successNotify = new bootstrap.Toast(successNotifyElem)
    watch(server_answer, (server_answer) => {
        successNotify.show()
        refresh.value = true
        pending.value = false
    })
    watch(error, (error) => {
        refresh.value = true
        pending.value = false
    })
}
</script>


<template>
    <div>
        <h3 class="text-center">Основные настройки</h3>
        <div>
            <label class="form-label" for="titleInput">Название курса</label>
            <div class="input-group mb-3">
                <input :value="title" type="text" class="form-control" placeholder="Название курса"
                    aria-label="Название курса" aria-describedby="buttonUpdateTitle" id="titleInput">
                <button class="btn btn-outline-secondary" type="button" id="buttonUpdateTitle"
                    @click="onSaveChanges">Сохранить</button>
            </div>
            <label class="form-label" for="descriptonInput">Описание курса</label>
            <div class="input-group mb-3">
                <textarea :value="description" type="text" class="form-control" placeholder="Описание курса"
                    aria-label="Описание курса" aria-describedby="buttonUpdateDescription" id="descriptonInput"></textarea>
                <button class="btn btn-outline-secondary" type="button" id="buttonUpdateDescription"
                    @click="onSaveChanges">Сохранить</button>
            </div>
        </div>

        <div class="position-fixed bottom-0 end-0 p-3" aria-atomic="true" style="z-index: 11">
            <div id="successNotify" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <img src="~/assets/brand.png" id="successNotifyImg" class="rounded me-2" alt="...">
                    <strong class="me-auto">Система</strong>
                    <small>Только что</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Закрыть"></button>
                </div>
                <div class="toast-body">
                    Изменения успешно сохранены!
                </div>
            </div>
        </div>
        <LoadingSpinner v-if="pending" />
    </div>
</template>

<style scoped>
#successNotifyImg {
    width: 10%;
}
</style>
