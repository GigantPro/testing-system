<template>
    <div class="modal fade" id="pageDevelopingWarningModal" tabindex="-1" aria-labelledby="pageDevelopingWarningModalLabel">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-danger" id="pageDevelopingWarningModalLabel">Сайт находится в разработке!</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Эта страница <b>находится в разработке!</b> Это <b>не окончательный вид, а лишь примерное ее представление!</b>
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
        const modal = new bootstrap.Modal(document.getElementById('pageDevelopingWarningModal'))
        modal.show()
    }
}
</script>
