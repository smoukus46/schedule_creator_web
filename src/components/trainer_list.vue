<template>
  <div class="trainer-div">
    <input class="add-trainer-input" placeholder="Введите имя тренера">
    <button
        class="add-trainer"
        @mouseenter="startTooltipTimer('trainer')"
        @mouseleave="clearTooltipTimer('trainer')"
        @click="createLiElem(this.ulElem, this.trainer_input, 'trainerList')">
      &#x2713;
    </button>
    <div v-if="isTrainerTooltipVisible" class="add-trainer-tooltip">Добавить тренера</div>
    <div class="trainer-list">
      <ul id="trainerUL">
        <li v-for="(trainer, index) in trainer_list" :key="index">
        {{ trainer.name }}
          <button class="delete-trainer" @click="deleteData()"></button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      ulElem: document.querySelector('#trainerUL'),
      trainer_input: document.querySelector('.add-trainer-input')
    }
  },
  props: {
    isTrainerTooltipVisible: {
      type: Boolean,
      required: true
    },
    startTooltipTimer: {
      type: Function,
      required: true
    },
    clearTooltipTimer: {
      type: Function,
      required: true
    },
    createLiElem: {
      type: Function,
      required: true
    },
    deleteData: {
      type: Function,
      required: true
    },
    trainer_list: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.trainer-list {
  max-height: 220px;
  margin-top: 10px;
  overflow-x: auto;
}

.trainer-div {
  width: 323px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.192);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(43, 43, 43, 0.568);
  margin-top: 12px;
  margin-left: 5px;
  overflow-x: auto;
}

div::-webkit-scrollbar {
  width: 7px;
}

div::-webkit-scrollbar-thumb:active {
  background: #b376ab;
}

div::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: rgb(205,103,195);
  background: linear-gradient(240deg, rgba(205,103,195,1) 0%, rgba(186,83,176,1) 70%);
}

ul {
  width: 307px;
  list-style: none;
  padding: 2px;
  margin-top: 0;
  margin-bottom: 0;
  margin-left: 5px;
  text-align: center;
  border-radius: 3px;
}

li {
  position: relative;
  padding-right: 20px;
  padding-left: 10px;
  font-size: 20px;
  background: #CD67A4;
  color: #fff;
  cursor: pointer;
  border-radius: 3px;
  margin-bottom: 4px;
  max-width: 316px;
  overflow: hidden;
  text-overflow: ellipsis;
  overflow-wrap: break-word;
  white-space: normal;
  user-select: none;
}

li:hover {
  background: #e376d3;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

input {
  outline: none;
  width: 275px;
  height: 23px;
  margin-left: 6px;
  text-align: center;
  font-size: 19px;
  font-family: Rubik, sans-serif;
  border-radius: 3px;
  border: 0;
  background: #CD67A4;
  color: #fff;
}

input:hover {
  background: #e376d3;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

input:focus {
  background: #ab5789;
}

input::-webkit-input-placeholder {
  color:#fff;
  text-align: center;
}

.add-trainer {
  font-family: Rubik, sans-serif;
  font-size: 1em;
  margin-top: 3px;
  margin-left: 4px;
  width: 25px;
  height: 25px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 3px;
  box-shadow: -2px 2px 10px 0 rgba(5, 5, 5, 0.5);
}

.add-trainer:hover {
  background: #ab3e9e;
  opacity: 0.8;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

.add-trainer:active {
  background: #b376ab;
  transform: scale(0.95);
}

.delete-trainer {
  width: 16px;
  height: 16px;
  border: none;
  background: none;
  background-image: url('../assets/white-xmark.svg');
  background-size: cover;
  position: absolute;
  top: 50%;
  right: 5px;
  transform: translateY(-50%);
}

.delete-trainer:hover {
  opacity: 0.8;
}

.delete-trainer:active {
  transform: translateY(-50%) scale(0.85);
}

.add-trainer-tooltip {
  position: absolute;
  top: 27px;
  left: 140px;
  padding: 5px;
  background-color: #fff;
  color: black;
  border-radius: 4px;
  border: 1px solid black;
  z-index: 1;
}
</style>