<template>
  <div class="table-space">
    <div>
      <button class="save-btn"><b>Сохранить расписание</b></button>
      <button class="export-btn"><b>Экспортировать расписание в Excel</b></button>
    </div>
    <table>
      <caption>
      <div class="month-picker">
        <input type="month" id="month-input">
      </div>
      </caption>
      <thead>
      <tr>
        <th class="time"></th>
        <th>Понедельник</th>
        <th>Вторник</th>
        <th>Среда</th>
        <th>Четверг</th>
        <th>Пятница</th>
        <th>Суббота</th>
        <th>Воскресенье</th>
      </tr>
      </thead>
      <tbody>
        <tr>
          <th contenteditable="true">10:00 - 11:00</th>
          <td contenteditable="true">Лера - Aero</td>
          <td contenteditable="true"></td>
          <td contenteditable="true">Настя -</td>
          <td contenteditable="true"></td>
          <td contenteditable="true"></td>
          <td contenteditable="true"></td>
          <td contenteditable="true"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
  }
}
</script>

<style scoped>
.table-space {
  width: 82%;
  height: 930px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.192);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(43, 43, 43, 0.568);
  margin-left: 330px;
  margin-top: -514px;
  overflow: auto;
}

.save-btn {
  font-family: Rubik, sans-serif;
  font-size: 1em;
  margin-left: 10%;
  width: 40%;
  height: 25px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 3px;
}

.save-btn:hover {
  background: #ab3e9e;
  opacity: 0.8;
}

.save-btn:active {
  background: #b376ab;
  transform: scale(0.99);
}

.export-btn {
  font-family: Rubik, sans-serif;
  font-size: 1em;
  margin: 10px;
  width: 40%;
  height: 25px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 3px;
}

.export-btn:hover {
  background: #ab3e9e;
  opacity: 0.8;
}

.export-btn:active {
  background: #b376ab;
  transform: scale(0.99);
}

.month-picker {
  margin-bottom: 15px;
}

table {
  width: 98%;
  border-top: 1px solid rgb(43, 129, 17);
  border-collapse: collapse;
  text-align: center;
  margin: 10px;
}
.time {
  width: 100px;
}

td {
  text-align: left;
  padding: 10px;
  border: 3px solid rgb(43, 129, 17);
}
th {
  text-align: center;
  padding: 10px;
  border: 3px solid rgb(43, 129, 17);
}

</style>