<template>
    <div class="d-block align-items-center justify-content-center vh-10" id="indexContent">
        <div class="text-center header_info" id="indexContent">
            <h1 class="display-7 fw-bold">Xiver.Education</h1>
            <p/>
            <h3>Платформа для <u>удобства</u> и <u>оптимизации</u> взаимодействия между <p />
            <u>учеником</u> и <u>учителем</u></h3>
        </div>
        <div class="login_registration text-center d-block align-items-center pt-2 pb-2">
            <p><u>Чтобы начать обучение, войдите в аккаунт</u></p>
            <p id="welcome_login_btn"><NuxtLink to="/auth?auth=login" class="btn btn-secondary rounded login_btn">Войти</NuxtLink></p> <!-- Fix me: Надо, чтобы кнопка была по размеру зарегистрироваться -->
            <p id="welcome_registration_btn"><NuxtLink to="/auth?auth=registration" class="registration_btn">Зарегистрироваться</NuxtLink></p>
        </div>
        <div class="top_courses text-reset">
            <h4 class="display-7 text-center top_courses_text">Популярные курсы</h4>
            <CoursesCarusel />
        </div>
        <ModalDevelopingWarning />
    </div>
</template>

<style scoped>
p {
    padding: .3rem;
}

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

#indexContent {
    line-height: 1.5;
}
</style>
