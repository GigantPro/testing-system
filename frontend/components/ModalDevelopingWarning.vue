<template>
    <div class="modal fade" id="developingWarningModal" tabindex="-1" aria-labelledby="developingWarningModalLabel">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-danger" id="developingWarningModalLabel">Сайт находится в разработке!</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Сайт на данный момент находится <b>в процессе разработки</b>, поэтому есть баги, недоделки и т.д.
                    <b>Так же может честиться база данных</b>, из-за чего <b>могут слетать аккаунты и другие ваши изменения</b>,
                    поэтому просим вас пока воспринимать этот сайт как примерные наметки того, что будет в конце. <p>Enjoy!</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Я понимаю</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted() {
        const modal = new bootstrap.Modal(document.getElementById('developingWarningModal'))
        modal.show()
    }
}
</script>
