<template>
  <div class="table-space">
    <table>
      <caption>
        <div class="btn-div">
          <button class="table-btn">
            <img class="btn-icon" src="../assets/journal.svg" width="16" height="16" alt="Показать расписание на выбранный месяц"/>
            <b>Показать расписание на выбранный месяц </b>
          </button>
          <button class="table-btn" disabled>
            <img class="btn-icon" src="../assets/disk.svg" width="16" height="16" alt="Сохранить созданное расписание"/>
            <b>Сохранить созданное расписание</b>
          </button>
          <button class="table-btn">
            <img class="btn-icon" src="../assets/export.svg" width="16" height="16" alt="Экспортировать расписание в Excel"/>
            <b>Экспортировать расписание в Excel</b>
          </button>
        </div>
        <div class="datepicker-container" ref="datepickerContainer">
          <div class="validation-symbol">*</div>
          <input
              type="text"
              required
              class="datepicker-input"
              v-model="formattedDate"
              placeholder="&#128197;Выберите месяц и год"
              readonly
              @click="togglePopup"
          />
          <div class="validation-error" hidden>Поле обязательно для заполнения</div>
          <div v-if="showPopup" class="datepicker">
            <div class="month-picker">
              <span class="prev-year" @click="prevYear">&#10094;</span>
              <span class="year-display">{{ selectedYear }}</span>
              <span class="next-year" @click="nextYear">&#10095;</span>
            </div>
            <div class="months-grid">
              <div
                  class="month"
                  v-for="(month, index) in months"
                  :key="index"
                  :class="{ 'selected-month': selectedMonth === index }"
                  @click="selectMonth(index)"
              >
                {{ month }}
              </div>
            </div>
          </div>
        </div>
      </caption>
      <thead>
      <tr>
        <th class="time-header"></th>
        <th class="day-header">Понедельник</th>
        <th class="day-header">Вторник</th>
        <th class="day-header">Среда</th>
        <th class="day-header">Четверг</th>
        <th class="day-header">Пятница</th>
        <th class="day-header">Суббота</th>
        <th class="day-header">Воскресенье</th>
      </tr>
      </thead>
      <tbody>
        <tr id="1">
          <th id="1">
            <select class="time">
              <option value="9:00 - 10:00" selected>9:00 - 10:00</option>
              <option value="10:00 - 11:00">10:00 - 11:00</option>
              <option value="11:00 - 12:00">11:00 - 12:00</option>
              <option value="12:00 - 13:00">12:00 - 13:00</option>
              <option value="13:00 - 14:00">13:00 - 14:00</option>
              <option value="14:00 - 15:00">14:00 - 15:00</option>
              <option value="15:00 - 16:00">15:00 - 16:00</option>
              <option value="16:00 - 17:00">16:00 - 17:00</option>
              <option value="17:00 - 18:00">17:00 - 18:00</option>
              <option value="18:00 - 19:00">18:00 - 19:00</option>
              <option value="19:00 - 20:00">19:00 - 20:00</option>
              <option value="20:00 - 21:00">20:00 - 21:00</option>
            </select>
          </th>
          <td id="1.1">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id ="1.2">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id="1.3">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id="1.4">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id="1.5">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id="1.6">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <td id="1.7">
            <input @input="textareaColoring" type="color" class="trainer-color" value="#ffffff"/>
            <textarea rows="3" class="workout-textarea"></textarea>
          </td>
          <button class="row-btn">
            <img id="delete-row-btn" src="../assets/white-xmark.svg" width="22" height="22"/>
          </button>
        </tr>
        <br>
        <button class="row-btn">
          <img id="add-row-btn" src="../assets/white-add.svg" width="22" height="22"/>
        </button>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {

  },
  data() {
    return {
      selectedYear: new Date().getFullYear(),
      selectedMonth: null,
      showPopup: false,
      months: [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
      ],
    };
  },
  computed: {
    formattedDate() {
      if (this.selectedMonth !== null) {
        return `${this.months[this.selectedMonth]} ${this.selectedYear}`;
      }
      return "";
    },
  },
  methods: {
    togglePopup() {
      this.showPopup = !this.showPopup;
    },
    selectMonth(index) {
      this.selectedMonth = index;
      this.showPopup = false;
    },
    prevYear() {
      this.selectedYear--;
    },
    nextYear() {
      this.selectedYear++;
    },
    handleClickOutside(event) {
      const datepickerContainer = this.$refs.datepickerContainer;
      // Проверяем, был ли клик вне контейнера датапикера
      if (datepickerContainer && !datepickerContainer.contains(event.target)) {
        this.showPopup = false;
      }
    },
    textareaColoring(event) {
      event.target.nextSibling.style.backgroundColor = event.target.value;
    },
  },
  mounted() {
    // Добавляем обработчик события при монтировании компонента
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeDestroy() {
    // Удаляем обработчик события перед разрушением компонента
    document.removeEventListener("click", this.handleClickOutside);
  }
};
</script>

<style scoped>
.table-space {
  width: 100%;
  height: 930px;
  overflow-x: hidden;
  background-image: url("https://avatars.mds.yandex.net/get-sprav-products/13074932/2a0000018e7a6f0a4300154eddee4449b6e7/M_height");
  background-position: center;
  background-repeat: no-repeat;
}

.table-space::-webkit-scrollbar {
  width: 7px;
}

.table-space::-webkit-scrollbar-thumb:active {
  background: #b376ab;
}

.table-space::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: rgb(205,103,195);
  background: linear-gradient(240deg, rgba(205,103,195,1) 0%, rgba(186,83,176,1) 70%);
}

.btn-div {
  margin-left: 0;
  margin-bottom: 10px;
  margin-top: -30px;
}

.table-btn {
  font-family: Rubik, sans-serif;
  font-size: 1em;
  width: 365px;
  margin: 20px;
  height: 30px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 3px;
  box-shadow: -2px 4px 10px 0 rgba(5, 5, 5, 0.5);
  user-select: none;
}

.table-btn:hover {
  background: #ab3e9e;
  opacity: 0.8;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

.table-btn:active {
  background: #b376ab;
  transform: scale(0.99);
}

.table-btn:disabled {
  background-color: #777;
  cursor: default;
  pointer-events: none;
  transform: none;
  opacity: 0.6;
  user-select: none;
}

.btn-icon {
  margin-right: 7px;
  margin-bottom: -2px;
}

.month-picker {
  margin-bottom: 15px;
}

.datepicker-container {
  position: relative;
  display: inline-block;
}

.datepicker-input {
  width: 300px;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-family: Rubik, sans-serif;
  font-size: 16px;
  text-align: center;
  cursor: pointer;
  outline: none;
  background: #CD67A4;
  color: #fff;
  box-shadow: -2px 4px 10px 0 rgba(5, 5, 5, 0.5);
}

.datepicker-input::-webkit-input-placeholder {
  color:#fff;
}

.datepicker-input:hover {
  background: #e376d3;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

.validation-symbol {
  color: red;
  margin-left: 330px;
  margin-bottom: -10px;
}

.validation-error {
  color: red;
  margin-top: -5px;
  font-size: 14px;
}

.datepicker {
  position: absolute;
  top: 55px;
  left: 9px;
  background-color: #870b79;
  color: #fff;
  border-radius: 5px;
  box-shadow: -2px 4px 10px 0 rgba(5, 5, 5, 0.5);
  padding: 10px;
  z-index: 10;
  width: 300px;
  font-family: Rubik, sans-serif;
}

.month-picker {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}

.month-picker span {
  cursor: pointer;
  font-size: 18px;
  user-select: none;
}

.prev-year:active, .next-year:active{
  transform: scale(0.9);
}

.months-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.month {
  text-align: center;
  padding: 10px;
  cursor: pointer;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-family: Rubik, sans-serif;
  user-select: none;
}

.month:hover {
  background-color: #e376d3;
}

.selected-month {
  background-color: #ab5789;
  color: white;
}

table {
  width: 98%;
  table-layout: auto;
  border-collapse: separate;
  border-spacing: 5px;
  text-align: center;
  margin: 10px;
}

.time-header {
  width: 97px;
  user-select: none;
 }

.day-header {
  position: sticky;
  z-index: 2;
  top: 0;
  width: 180px;
  border-radius: 5px;
  background: rgb(214,212,214,1);
  cursor: default;
  user-select: none;
}

td {
  width: 180px;
  max-height: 60px;
  padding: 10px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.192);
  backdrop-filter: blur(10px);
  outline: none;
  box-shadow: -2px 2px 5px 0 rgba(5, 5, 5, 0.5);
}

th {
  padding: 10px;
  outline: none;
}

.workout-textarea {
  width: 89%;
  height: 100%;
  max-width: 180px;
  max-height: 600px;
  padding: 3px;
  margin-left: 0;
  resize: none;
  border: none;
  border-radius: 0 5px 5px 0;
  outline: none;
  text-align: left;
  background: rgba(255, 255, 255, 0);
  position: relative;
  z-index: 1;
  font-family: Rubik, sans-serif;
  font-size: 16px;
}

.workout-textarea::-webkit-scrollbar {
  width: 7px;
}

.workout-textarea::-webkit-scrollbar-thumb:active {
  background: #b376ab;
}

.workout-textarea::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: rgb(205,103,195);
  background: linear-gradient(240deg, rgba(205,103,195,1) 0%, rgba(186,83,176,1) 70%);
}

.trainer-color {
  -webkit-appearance: none; /* Отключение стандартного стиля (для WebKit-браузеров) */
  border-left: none;
  border-top: none;
  border-bottom: none;
  border-right: 1px solid black;
  border-radius: 5px 0 0 5px;
  padding: 0;
  cursor: pointer;
  width: 11px;
  height: 63px;
}

.trainer-color::-webkit-color-swatch {
  border: none;
}

.trainer-color::-webkit-color-swatch-wrapper {
  padding: 0;
}

.row-btn {
  font-family: Rubik, sans-serif;
  font-size: 1em;
  width: 22px;
  margin: 0;
  height: 22px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 50%;
  box-shadow: -2px 4px 10px 0 rgba(5, 5, 5, 0.5);
}

.row-btn:hover {
  background: #ab3e9e;
  opacity: 0.8;
  box-shadow: 0 2px 15px rgba(5, 5, 5, 0.5);
}

.row-btn:active {
  background: #b376ab;
  transform: scale(0.95);
}

#delete-row-btn {
  margin-top: -1px;
  margin-left: -6px;
}

#add-row-btn {
  margin-top: -1px;
  margin-left: -6px;
}

.time {
  width: 107px;
  border: none;
  outline: none;
  padding: 0;
  background: transparent;
  color:#000;
  font-family: Rubik, sans-serif;
  font-weight: bold;
  text-align: center;
  font-size: 14px;
}

.time option {
  background-color: #870b79;
  color: #fff;
}

</style>