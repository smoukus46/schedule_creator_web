<template>
  <div v-if="isLoadingModalVisible" id="modal" class="modal">
    <div class="modal-content">
      <p>Расписание {{ modalText }}, пожалуйста, подождите</p>
      <div class="loader"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modalText: {
      type: String,
      required: true
    },
    isLoadingModalVisible: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Полупрозрачное затемнение */
}

.modal-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

/* Прелоадер (анимированный круг) */
.loader {
  border: 8px solid #f3f3f3; /* Light grey */
  border-top: 8px solid #ab3e9e; /* Blue */
  border-radius: 50%;
  margin-left: 40%;
  width: 60px;
  height: 60px;
  animation: spin 1.5s linear infinite;
  margin-bottom: 10px;
}

/* Анимация вращения прелоадера */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>