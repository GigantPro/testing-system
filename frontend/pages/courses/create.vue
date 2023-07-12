<script setup>
useHead({
    title: 'Создать свой курс | Xiver education',
})

const router = useRouter()

const data = ref("")
const pending = ref("")
const error = ref("")

const course_name_state = ref("")
const course_name_error_msg = ref("")

const course_desc_state = ref("")
const course_desc_error_msg = ref("")

const onFormSubmit = async (e) => {
    e.preventDefault()
    const title_inp = document.getElementById('course-title-input')
    const description_inp = document.getElementById('course-desc-input')

    let flag = true
    if (!title_inp.value) {
        course_name_state.value = "is-invalid"
        course_name_error_msg.value = "Поле не может быть пустым!"
        flag = false
    }
    if (!description_inp.value) {
        course_desc_state.value = "is-invalid"
        course_desc_error_msg.value = "Поле не может быть пустым!"
        flag = false
    }
    if (!flag) {
        return
    }

    const { data: data_src, pending: pending_src, error: error_src } = await useFetch('/api/course/create', {
        headers: useRequestHeaders(),
        server: false,
        method: 'POST',
        body: new URLSearchParams({
            'title': title_inp.value,
            'description': description_inp.value
        })

    })
    pending.value = pending_src
    data.value = data_src
    error.value = error_src

    console.log(data_src.value);
    if (data_src.value.message === "success") {
        await router.push('/user/courses')
        await router.go()
    }
}
</script>


<template>
    <form class="row justify-content-center text-center mt-5 mb-5" @submit.prevent="onFormSubmit">
        <div v-if="!pending.value" class="col-xxl-5 col-xl-6 col-lg-10 col-md-11 col-sm-12">
            <h1 class="mb-5">Создание нового курса</h1>
            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + course_name_state">
                    <input type="text" :class="'form-control ' + course_name_state" id="course-title-input"
                        placeholder="Название">
                    <label class="input-required" for="course-title-input">Название нового курса (не более 64
                        символов)</label>
                </div>
                <div class="invalid-feedback">
                    {{ course_name_error_msg }}
                </div>
            </div>
            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + course_desc_state">
                    <textarea type="text" :class="'form-control ' + course_desc_state" id="course-desc-input"
                        placeholder="Описание" style="height: 100px"></textarea>
                    <label class="input-required" for="course-desc-input">Описание курса</label>
                </div>
                <div class="invalid-feedback">
                    {{ course_desc_error_msg }}
                </div>
            </div>
            <div class="text-center">
                <button type="submit" class="btn btn-dark rounded border-white"
                    style="margin: 1.5rem auto 3rem auto;">Создать</button>
            </div>
        </div>
        <div v-else-if="pending.value" class="d-flex justify-content-center">
            <div class="spinner-grow text-success" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div v-else class="col-xxl-5 col-xl-6 col-lg-10 col-md-11 col-sm-12 text-center text-danger">
            Произошла какая-то ошибка, повторите позже!
        </div>
    </form>
</template>