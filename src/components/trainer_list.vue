<template>
<div class="trainer-div">
  <div class="trainer-list"><ul>
    <li>
      Лера
      <button class="delete-trainer"></button>
    </li>
    <li>
      Диана
      <button class="delete-trainer"></button>
    </li>
    <li>
      Женя
      <button class="delete-trainer"></button>
    </li>
    <li>
      Ира
      <button class="delete-trainer"></button>
    </li>
    <li>
      Наташа
      <button class="delete-trainer"></button>
    </li>
    <li>
      Лена
      <button class="delete-trainer"></button>
    </li>
    <li>
      Света
      <button class="delete-trainer"></button>
    </li>
    <li>
      Настя
      <button class="delete-trainer"></button>
    </li>
  </ul>
  </div>
    <input placeholder="Введите имя тренера"><br>
    <button class="add-trainer"><b>Добавить тренера</b></button>
</div>
</template>

<script>
export default {
  props: {
  }
}
</script>

<style scoped>
.trainer-list {
  height: 75%;
  overflow-x: auto;
}

.trainer-div {
  width: 316px;
  height: 250px;
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
  list-style: none;
  padding: 0;
  margin-top: 0;
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
  margin-bottom: 2px;
  max-width: 316px;
  overflow: hidden;
  text-overflow: ellipsis;
  overflow-wrap: break-word;
  white-space: normal;
}

li:hover {
  background: #e376d3;
}

input {
  outline: none;
  width: 98.6%;
  height: 23px;
  margin-top: 5px;
  text-align: center;
  font-size: 1em;
  font-family: Rubik, sans-serif;
  border-radius: 3px;
  border: 0;
  background: #CD67A4;
  color: #fff;
}

input:hover {
  background: #e376d3;
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
  width: 100%;
  height: 25px;
  position: relative;
  color: #fff;
  cursor: pointer;
  background: #870b79 ;
  border: 0;
  border-radius: 3px;
}

.add-trainer:hover {
  background: #ab3e9e;
  opacity: 0.8;
}

.add-trainer:active {
  background: #b376ab;
  transform: scale(0.99);
}

.delete-trainer {
  width: 16px;
  height: 16px;
  border: none;
  background: none;
  background-image: url('../assets/delete_icon.png');
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
</style>