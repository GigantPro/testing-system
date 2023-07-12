<script setup>
definePageMeta({
  middleware: 'logged-users-only'
})

useHead({
    title: 'Мои курсы | Xiver education',
})

const headers = useRequestHeaders()

const { data: courses_data, error } = await useFetch('http://bakchain:5001/course/me/when_am_i')
</script>


<template>
    <div>
        <h1 class="text-center mt-5 mb-5">Список курсов</h1>
        <div class="container align-items-center justify-content-center items-center">
            <div class="row">
                <div class="col-2 rounded shadow btn-group-vertical mr-5 p-2 second-float" role="group"
                    aria-label="Basic checkbox toggle button group">
                    <h4 class="mb-3">Фильтры</h4>

                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
                        <label class="form-check-label" for="flexSwitchCheckChecked">Учусь</label>
                    </div>
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Преподаю</label>
                    </div>

                </div>
                <div class="col-1"></div>
                <div class="col-9 shadow rounded ml-5 p-3 second-float">
                    Список курсов...
                </div>
            </div>
        </div>
    </div>
</template>


<!-- <script>
export default {
    mounted() {
        
    }
}
</script> -->
