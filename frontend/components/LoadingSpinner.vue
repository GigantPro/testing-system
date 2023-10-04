<template>
    <div id="loading">
        <div class="spinner-border" id="loadingSpinner" role="status">
            <span class="visually-hidden">Загрузка...</span>
        </div>
    </div>
</template>

<style scoped>
#loading{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;

    z-index:99999999;
    background-color: rgba(0, 0, 0, 0.4);

    display: flex;
    justify-content: center;
}

#loadingSpinner {
    margin-top: 25%;
    color: #53774B;
}
</style>
