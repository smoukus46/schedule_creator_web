<template>
  <div v-if="isErrorModalVisible" id="modal" class="modal">
    <div class="modal-content">
      {{ errorText }}
      <button id="closeModal" @click="closeErrorModal">
        <img class="closeModalBtn" src="../assets/white-xmark.svg" width="21" height="21"/>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    errorText: {
      type: String,
      required: true
    },
    isErrorModalVisible: {
      type: Boolean,
      required: true
    },
    showErrorModal: {
      type: Function,
      required: true
    },
    closeErrorModal: {
      type: Function,
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

#closeModal {
  position: absolute;
  width: 19px;
  height: 19px;
  top: 4px;
  right: 3px;
  background: #870b79;
  border: none;
  border-radius: 50%;
}

.closeModalBtn {
  margin-left: -7px;
  margin-top: -2px;
}

.closeModalBtn:hover {
  background: #ab3e9e;
  border-radius: 50%;
  opacity: 0.8;
  box-shadow: 0 2px 15px rgba(5, 5, 5, 0.5);
}

.closeModalBtn:active {
  background: #b376ab;
  transform: scale(0.95);
}
</style>