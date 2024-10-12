<template>
  <div class="workout-div">
    <input placeholder="Введите название тренировки"/>
    <button class="add-workout">&#x2713;</button>
    <div class="workout-list">
      <ul>
        <li>
          Аэрорастяжка
          <button class="delete-workout"></button>
        </li>
        <li>
          Аэрорастяжка с переворотом, подворотом и перелетом
          <button class="delete-workout"></button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: {
  }
}
</script>

<style scoped>
.workout-list {
  max-height: 220px;
  margin-top: 10px;
  overflow-x: auto;
}

.workout-div {
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

.add-workout {
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

.add-workout:hover {
  background: #ab3e9e;
  opacity: 0.8;
  box-shadow: 0 4px 15px rgba(5, 5, 5, 0.5);
}

.add-workout:active {
  background: #b376ab;
  transform: scale(0.99);
}

.delete-workout {
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

.delete-workout:hover {
  opacity: 0.8;
}

.delete-workout:active {
  transform: translateY(-50%) scale(0.85);
}
</style>