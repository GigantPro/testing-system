<template>
    <div class="d-block align-items-center justify-content-center vh-10">
        <div class="text-center header_info">
            <h1 class="display-7 fw-bold">Xiver.Education</h1>
            <h3>Платформа для <u>удобства</u> и <u>оптимизации</u> взаимодействия между</h3>
            <h3><u>учеником</u> и <u>учителем</u></h3>
        </div>
        <hr style="">
        <div class="login_registration text-center d-block align-items-center">
            <p><u>Чтобы начать обучение, войдите в аккаунт</u></p>
            <p id="welcome_login_btn"><NuxtLink to="/auth/login" class="btn btn-primary rounded login_btn">Войти</NuxtLink></p> <!-- Fix me: Надо, чтобы кнопка была по размеру зарегистрироваться -->
            <p id="welcome_registration_btn"><NuxtLink to="/auth/registration" class="registration_btn">Зарегистрироваться</NuxtLink></p>
        </div>
        <div class="top_courses text-reset">
            <h4 class="display-7 text-center top_courses_text">Популярные курсы</h4>
            <ClientOnly fallback="Loading courses cards">
                <CoursesCarusel />
            </ClientOnly>
        </div>
    </div>
</template>

<style scoped>
.header_info {
    margin: 5rem auto 1.5rem auto;
}

.login_btn {
    background: #53774B;
}
.registration_btn {
    color: rgba(0, 0, 0, 0.45);
}

.top_courses_text {
    margin: 3rem auto 1.5rem auto;
    font-family: Inter;
    font-size: 16px;
    font-weight: 400;
    line-height: 19px;
    letter-spacing: 0.3em;
}
</style>
