<template>
  <div class="table-space">
    <table>
      <caption>
        <div class="btn-div">
          <button class="table-btn" @click="getTable">
            <img
                class="btn-icon"
                src="../assets/journal.svg"
                width="16"
                height="16"
                alt="Показать расписание на выбранный месяц"
            />
            <b>Показать расписание на выбранный месяц </b>
          </button>
          <button
              id="save-button"
              class="table-btn"
              :disabled="!canSave"
              @click="submitTable"
          >
            <img
                class="btn-icon"
                src="../assets/disk.svg"
                width="16"
                height="16"
                alt="Сохранить созданное расписание"
            />
            <b>Сохранить созданное расписание</b>
          </button>
          <button class="table-btn" @click="downloadSchedule()">
            <img
                class="btn-icon"
                src="../assets/export.svg"
                width="16"
                height="16"
                alt="Экспортировать расписание в Excel"
            />
            <b>Выгрузить файл с расписанием</b>
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
          <div v-if="isValidationMessageVisible" class="validation-error">Поле обязательно для заполнения</div>
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
      <tbody @input="checkRows">
        <tr v-for="(row, rowIndex) in tableRows" :key="rowIndex">
          <th>
            <select v-model="row.time" class="time">
              <option value="9:00 - 10:00">9:00 - 10:00</option>
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
          <td
              v-for="(cell, cellIndex) in row.cells"
              :key="cellIndex"
          >
            <textarea
                rows="3"
                v-model="cell.text"
                class="workout-textarea"
                @dragenter="onDragEnter"
                @dragover="onDragOver"
                @dragleave="onDragLeave"
                @drop="onDrop($event, rowIndex, cellIndex)"
            ></textarea>
          </td>
          <button class="row-btn" @click="deleteRow(rowIndex)">
            <img id="delete-row-btn" src="../assets/white-xmark.svg" width="22" height="22"/>
          </button>
        </tr>
        <button class="row-btn" @click="addRow">
          <img id="add-row-btn" src="../assets/white-add.svg" width="22" height="22"/>
        </button>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    tableRows: {
      type: Array,
      required: true
    },
    showModal: {
      type: Function,
      required: true
    },
    showErrorModal: {
      type: Function,
      required: true
    },
    closeLoadingModal: {
      type: Function,
      required: true
    },
    draggedItem: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      canSave: false,
      isValidationMessageVisible: false,
      selectedYear: new Date().getFullYear(),
      selectedMonth: null,
      showPopup: false,
      months: [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
      ]
    };
  },
  computed: {
    formattedDate() {
      if (this.selectedMonth !== null) {
        return `${this.months[this.selectedMonth]} ${this.selectedYear}`;
      }
      return "";
    }
  },
  methods: {
    async downloadSchedule() {
      try {
        const response = await fetch('/api/download-schedule', {
          method: "GET",
        });

        if (!response.ok) {
          throw new Error('Ошибка при загрузке файла');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = 'Расписание_тренировок.xlsx';

        document.body.appendChild(a);
        a.click();

        a.remove();
      } catch (error) {
        console.error('Ошибка при загрузке файлов', error)
      }
    },
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
    textareaColoring(event='') {
      if (event.type === 'drop') {

        if(this.draggedItem.color) {
          event.target.style.backgroundColor = this.draggedItem.color;
          event.target.parentNode.style.backgroundColor = this.draggedItem.color;
        }
      } else {

        const trList = document.getElementsByTagName('tr');

        for(let index = 0; index < this.tableRows[index].cells.length; index++) {

          for(let i = 0; i < this.tableRows[index].cells.length; i++) {

            trList[index + 1].cells[i + 1].style.backgroundColor = this.tableRows[index].cells[i].color;
          }
        }
      }
    },
    showValidationError(modalMessage) {
      const input = document.querySelector('.datepicker-input');

      if(input.value === '') {
        this.isValidationMessageVisible = true;

        return false;
      } else {
        this.isValidationMessageVisible = false;

        this.showModal(modalMessage);

        return true;
      }
    },
    checkRows() {
      if(this.tableRows.length >= 1) {
        this.canSave = this.tableRows.every(row => {

          return (
              row.time !== '' &&
              row.cells.every(cell => cell.text !== '')
          );
        });
      } else {
        this.canSave = false;
      }
    },
    addRow() {
      this.tableRows.push({
        time: '',
        cells: Array.from({ length: 7 }, () => ({ color: '#ffffff31', text: '' }))
      });
      this.checkRows();
    },
    deleteRow(index) {
      this.tableRows.splice(index, 1);
      this.checkRows();
    },
    onDrop(event, rowIndex, cellIndex) {
      event.preventDefault();

      event.target.parentNode.classList.remove('highlight');

      const cell = this.tableRows[rowIndex].cells[cellIndex];

      if (cell.text !== '') {
        cell.text += ' - ' + this.draggedItem.name;
        if (this.draggedItem.color) {
          cell.color = this.draggedItem.color;
        }

        this.textareaColoring(event);

        this.draggedItem.name = null;
        this.draggedItem.color = null;
      } else {
        cell.text = this.draggedItem.name;
        cell.color = this.draggedItem.color;

        this.textareaColoring(event);

        this.draggedItem.name = null;
        this.draggedItem.color = null;
      }

      this.checkRows();
    },
    onDragEnter(event) {
      event.preventDefault();
      event.target.parentNode.classList.add('highlight');
    },
    onDragOver(event) {
      event.preventDefault();
    },
    onDragLeave(event) {
      event.target.parentNode.classList.remove('highlight');
    },
    async getTable() {
      try {
        if(this.showValidationError('загружается')) {
          const input = document.querySelector('.datepicker-input');
          const response = await fetch(`/api/get-table/${input.value}`);

          if (response.ok) {
            const data = await response.json();

            this.closeLoadingModal();

            for(let index = 0; index < data.table_data.length; index++) {
              this.tableRows.push(data.table_data[index]);
            }

            await this.$nextTick(() => {
              this.textareaColoring();
            });
          } else {
            this.closeLoadingModal();
            this.showErrorModal('Ошибка при получении данных');

            console.error('Ошибка при получении данных:', response.statusText);
          }
        }
      } catch (error) {
        this.closeLoadingModal();

        console.error('Ошибка:', error, error.statusCode);
      }
    },
    async submitTable() {
      try {
        if(this.showValidationError('сохраняется')) {
          const input = document.querySelector('.datepicker-input');

          const response = await fetch(`/api/save-table/${input.value}`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              rows: this.tableRows
            }),
          });

          if (response.ok) {
            const result = await response.json();

            if (result.message === "Расписание на такой месяц уже сущетствует") {

              await this.editTable();

            } else {
              this.closeLoadingModal();
              this.showErrorModal('Данные успешно отправлены');

              console.log('Данные успешно отправлены:', result);
            }
          }
        }
      } catch (error) {
        this.closeLoadingModal();

        this.showErrorModal(error);

        console.error('Ошибка:', error);
      }
    },
    async editTable() {
      try {
        const input = document.querySelector('.datepicker-input');

        const response = await fetch(`/api/save-table/${input.value}`, {

          method: "PUT",
          headers: {"Accept": "application/json", "Content-Type": "application/json"},
          body: JSON.stringify({
            rows: this.tableRows
          })
        });

        if (response.ok === true) {
          const data = await response.json();

          this.closeLoadingModal();

          this.showErrorModal('Данные успешно отправлены');
        } else {
          this.closeLoadingModal();
          this.showErrorModal('Ошибка при отправке данных');

          console.error('Ошибка при отправке данных:', response.statusText);
        }
      } catch (error) {
        this.closeLoadingModal();

        console.error('Ошибка:', error);
      }
    }
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
  background-color: rgba(255, 255, 255, 0.192);
  backdrop-filter: blur(10px);
  outline: none;
  box-shadow: -2px 2px 5px 0 rgba(5, 5, 5, 0.5);
}

th {
  padding: 10px;
  outline: none;
}

.workout-textarea {
  width: 100%;
  height: 100%;
  padding: 3px;
  margin-left: -3px;
  resize: none;
  border: none;
  border-radius: 5px;
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

.highlight {
  border-color: green;
  background-color: lightgreen;
}

</style>