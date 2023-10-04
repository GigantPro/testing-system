<script setup>
definePageMeta({
  middleware: 'unlogged-users-only'
})

const route = useRoute()
const router = useRouter()

const prefix = route.query.auth === 'registration' ? 'Регистрация' : 'Вход'
useHead({
    title: prefix + ' | Xiver education',
})

if (!route.query.auth) {
    route.query.auth = 'login'
    useHead({
        title: 'Вход | Xiver education',
    })
}



const default_err_msg = "Поле не может быть пустым!"

const name_state = ref("")
const surname_state = ref("")
const email_state = ref("")
const username_state = ref("")
const password_state = ref("")
const second_password_state = ref("")

const name_err_message = ref("")
const surname_err_message = ref("")
const email_err_message = ref("")
const username_err_message = ref("")
const password_err_message = ref("")
const second_err_message = ref("")

const loading = ref(false)


const onFormSubmit = async (values, actions) => {
    const name_inp = document.getElementById('name-input')
    const surname_inp = document.getElementById('surname-input')
    const email_inp = document.getElementById('email-input')
    const username_inp = document.getElementById('username-inp')
    const password_inp = document.getElementById('password-input')
    const repeat_password = document.getElementById('repeat-password')


    let flag = true
    if (!email_inp.value) {
        email_state.value = "is-invalid"
        email_err_message.value = default_err_msg
        flag = false
    } else {
        email_state.value = "is-valid"
        email_err_message.value = ""
    }
    if (!password_inp.value) {
        password_state.value = "is-invalid"
        password_err_message.value = default_err_msg
        flag = false
    } else {
        password_state.value = "is-valid"
        password_err_message.value = ""
    }
    if (route.query.auth === 'registration') {
        if (password_inp.value.length < 8) {
            password_state.value = "is-invalid"
            password_err_message.value = "Пароль должен быть не менее 8 символов!"
            flag = false
        } else {
            password_state.value = "is-valid"
            password_err_message.value = ""
        }
        if (!name_inp.value) {
            name_state.value = "is-invalid"
            name_err_message.value = default_err_msg
            flag = false
        } else {
            name_state.value = "is-valid"
            name_err_message.value = ""
        }
        if (!surname_inp.value) {
            surname_state.value = "is-invalid"
            surname_err_message.value = default_err_msg
            flag = false
        } else {
            surname_state.value = "is-valid"
            surname_err_message.value = ""
        }
        if (!username_inp.value) {
            username_state.value = "is-invalid"
            username_err_message.value = default_err_msg
            flag = false
        } else {
            const dataTwice = $fetch('/api/user/username/' + username_inp.value)
            console.log(dataTwice);
            if (dataTwice["detail"] === "REGISTER_USER_ALREADY_EXISTS") {
                flag = false
                username_state.value = "is-invalid"
                username_err_message.value = "Этот пользователь уже существует!"
            } else if (!dataTwice["detail"]) {
                username_state.value = "is-valid"
                username_err_message.value = ""
            }
        }
        if (repeat_password.value != password_inp.value || !repeat_password.value) {
            password_state.value = "is-invalid"
            second_password_state.value = "is-invalid"
            password_err_message.value = "Пароли не совпадают!"
            second_err_message.value = "Пароли не совпадают!"
            flag = false
        } else {
            second_password_state.value = "is-valid"
            second_err_message.value = ""
        }
    }

    if (flag && route.query.auth === 'registration') {
        loading.value = true
        // const {data: data_s, pending: pending_s, error_s} = await useFetch(
        //     '/api/auth/register',
        //     {
        //         headers: { "Content-type": "application/json" },
        //         method: 'POST',
        //         body: {
        //             email: email_inp.value,
        //             password: password_inp.value,
        //             username: username_inp.value,
        //             name: name_inp.value,
        //             surname: surname_inp.value,
        //             role_id: 0,
        //         }
        //     }
        // )

        // name_state.value = ''
        // name_err_message.value = ''
        // password_state.value = ''
        // password_err_message.value = ''

        // await useFetch(
        //     '/api/auth/login',
        //     {
        //         headers: { "Content-type": "application/x-www-form-urlencoded" },
        //         method: 'POST',
        //         body: new URLSearchParams({
        //             'username': email_inp.value,
        //             'password': password_inp.value,
        //         })
        //     }
        // )
        // await router.push('/')
        // await router.go()
    } else if (flag && route.query.auth === 'login') {  // Fix me: указание правильности / неправильности логина и пароля
        // await useFetch(
        //     '/api/auth/login',
        //     {
        //         headers: { "Content-type": "application/x-www-form-urlencoded" },
        //         method: 'POST',
        //         body: new URLSearchParams({
        //             'username': email_inp.value,
        //             'password': password_inp.value,
        //         })
        //     }
        // )
        // await router.push('/')
        // await router.go()
    }
}

</script>


<template>
    <form class="row justify-content-center" @submit.prevent="onFormSubmit">
        <div v-if="$route.query.auth == 'registration'" class="items-center col-xxl-5 col-xl-6 col-lg-10 col-md-11 col-sm-12">
            <h1 class="text-center" style="margin: 3rem auto 2rem auto;">Регистрация</h1>

            <div :v-bind="name_state" class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + name_state">
                    <input type="text" :class="'form-control ' + name_state" id="name-input" placeholder="Иван">
                    <label class="input-required" for="name-input">Имя</label>
                </div>
                <div class="invalid-feedback">{{ name_err_message }}</div>
            </div>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + surname_state">
                    <input type="text" :class="'form-control ' + surname_state" id="surname-input" placeholder="Петров">
                    <label class="input-required" for="surname-input">Фамилия</label>
                </div>
                <div class="invalid-feedback">
                    {{ surname_err_message }}
                </div>
            </div>

            <div class="input-group has-validation mb-3">
                <span class="input-group-text">@</span>
                <div :class="'shadow form-floating ' + username_state">
                    <input type="text" :class="'form-control ' + username_state" id="username-inp" placeholder="Username">
                    <!-- ! Fix me: проверка на существующий юзернейм -->
                    <label class="input-required" for="username-inp">Имя пользователя</label>
                </div>
                <div class="invalid-feedback">{{ username_err_message }}</div>
            </div>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + email_state">
                    <input type="email" :class="'form-control ' + email_state" id="email-input"
                        placeholder="name@example.com">
                    <label class="input-required" for="email-input">Адрес электронной почты</label>
                </div>
                <div class="invalid-feedback">
                    {{ email_err_message }}
                </div>
            </div>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + password_state">
                    <input type="password" :class="'form-control ' + password_state" id="password-input"
                        placeholder="Пароль">
                    <label class="input-required" for="password-input">Пароль</label>
                </div>
                <div class="invalid-feedback">
                    {{ password_err_message }}
                </div>
            </div>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + second_password_state">
                    <input type="password" :class="'form-control ' + second_password_state" id="repeat-password"
                        placeholder="Пароль">
                    <label class="input-required" for="repeat-password">Подтвердите пароль</label>
                </div>
                <div class="invalid-feedback">
                    {{ second_err_message }}
                </div>
            </div>

            <div class="text-center">
                <a href="/auth?auth=login">Войти</a>
            </div>
            
            <div class="text-center">
                <button type="submit" class="btn btn-dark rounded border-white" style="margin: 1.5rem auto 3rem auto;"
                    @click="onRegistration">Зарегистрироваться</button>
            </div>
        </div>
        <div v-else class="text-center items-center col-xxl-5 col-xl-6 col-lg-10 col-md-11 col-sm-12">
            <h1 style="margin: 3rem auto 2rem auto;">Вход</h1>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + email_state">
                    <input type="email" :class="'form-control ' + email_state" id="email-input"
                        placeholder="name@example.com">
                    <label class="input-required" for="email-input">Адрес электронной почты</label>
                </div>
                <div class="invalid-feedback">
                    {{ email_err_message }}
                </div>
            </div>

            <div class="input-group has-validation mb-3">
                <div :class="'shadow form-floating ' + password_state">
                    <input type="password" :class="'form-control ' + password_state" id="password-input"
                        placeholder="Пароль">
                    <label class="input-required" for="password-input">Пароль</label>
                </div>
                <div class="invalid-feedback">
                    {{ password_err_message }}
                </div>
            </div>

            <div class="text-center">
                <a href="/auth?auth=registration">Зарегистрироваться</a>
            </div>
            
            <div class="text-center">
                <button type="submit" class="btn btn-dark rounded border-white" style="margin: 1.5rem auto 3rem auto;"
                    @click="onLogin">Войти</button>
            </div>
        </div>
        <LoadingSpinner v-if="loading" />
    </form>
</template>
