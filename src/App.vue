<template>
<body>
  <div>
    <div class="menu">
      <Menu_bar
          :isTrainerTooltipVisible="isTrainerTooltipVisible"
          :isWorkoutTooltipVisible="isWorkoutTooltipVisible"
          :workout_list="workout_list"
          :trainer_list="trainer_list"
          :startTooltipTimer="startTooltipTimer"
          :clearTooltipTimer="clearTooltipTimer"
          :getInfo="getInfo"
          :createLiElem="createLiElem"
          :deleteData="deleteData"
          :onDragStart="onDragStart"
          :addTrainerColor="addTrainerColor"
      />
    </div>
    <div class="table">
      <Table_component
          :tableRows="tableRows"
          :showModal="showModal"
          :showErrorModal="showErrorModal"
          :closeLoadingModal="closeLoadingModal"
          :draggedItem="draggedItem"
      />
    </div>
  </div>
  <div>
    <Loading_modal
        :modalText="modalText"
        :isLoadingModalVisible="isLoadingModalVisible"
    />
  </div>
  <div>
    <Error_modal
        :errorText="errorText"
        :isErrorModalVisible="isErrorModalVisible"
        :showErrorModal="showErrorModal"
        :closeErrorModal="closeErrorModal"
    />
  </div>
  <div class="frame">
    <iframe allow="clipboard-write" src="https://music.yandex.ru/iframe/playlist/nikita.yakovlev46/3">
    </iframe>
  </div>
</body>
</template>

<script>
import Menu_bar from "@/components/menu_bar.vue";
import Table_component from "@/components/table_component.vue";
import Trainer_list from "@/components/trainer_list.vue";
import Loading_modal from "@/components/loading_modal.vue";
import Error_modal from "@/components/error_modal.vue";

export default {
  components: {Trainer_list, Menu_bar, Table_component, Loading_modal, Error_modal},
  data() {
    return {
      errorText: "",
      modalText: "",
      isErrorModalVisible: false,
      isLoadingModalVisible: false,
      isTrainerTooltipVisible: false,
      isWorkoutTooltipVisible: false,
      draggedItem: {name: null, color: null},
      tooltipTimer: null,
      workout_list: [],
      trainer_list: [],
      tableRows: [],
    }
  },
  methods: {
    // Начинаем таймер, который покажет тултип через 2 секунды
    startTooltipTimer(elem) {
      this.tooltipTimer = setTimeout(() => {
        if(elem === 'trainer') {
          this.isTrainerTooltipVisible = true; // Скрываем тултип
        } else if(elem === 'workout') {
          this.isWorkoutTooltipVisible = true;
        }
      }, 1000); // 2 секунды
    },
    // Очищаем таймер и скрываем тултип, если мышь покидает элемент
    clearTooltipTimer(elem) {
      clearTimeout(this.tooltipTimer); // Сброс таймера
      if(elem === 'trainer') {
        this.isTrainerTooltipVisible = false; // Скрываем тултип
      } else if(elem === 'workout') {
        this.isWorkoutTooltipVisible = false;
      }
    },
    showModal(modalText) {
      this.isLoadingModalVisible = true;
      this.modalText = modalText;
    },
    showErrorModal(errorText) {
      this.isErrorModalVisible = true;
      this.errorText = errorText;
    },
    closeLoadingModal() {
      this.isLoadingModalVisible = false;
    },
    closeErrorModal() {
      this.isErrorModalVisible = false;
    },
    async getInfo(listType, elemURL) {
      try {

        const response = await fetch(`/api/${elemURL}`, {
          method: "GET",
          headers: { "Accept": "application/json" }
        });

        if (response.ok === true) {
          const data = await response.json();

          for(let index = 0; index < data.length; index++) {
            listType.push(data[index]);
          }

        } else {
          console.error('Ошибка при загрузке данных');
        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса', error);
      }
    },
    async createLiElem(listType, elemURL) {
      try {
        const input = event.target.previousSibling;
        const value = input.value;

        const response = await fetch(`/api/${elemURL}`, {
          method: "POST",
          headers: { "Accept": "application/json", "Content-Type": "application/json" },
          body: JSON.stringify({
            name: value
          })
        });

        if (response.ok === true) {
          const data = await response.json();
          listType.push(data);
          input.value = '';
        } else {
          console.error('Ошибка при добавлении данных');
        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса', error);
      }
    },
    async deleteData(event, elemURL, id) {
      try {

        const response = await fetch(`/api/${elemURL}/${id}`, {
          method: "DELETE",
          headers: { "Accept": "application/json" }
        });

        if (response.ok === true) {
          event.target.parentNode.remove();
        } else {
          console.error('Ошибка при удалении данных');
        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса', error);
      }
    },
    onDragStart(event, objectName, objectColor) {
      this.draggedItem.name = objectName;
      this.draggedItem.color = objectColor;
    },
    addTrainerColor(event, index) {
      this.trainer_list[index].color = event.target.value;
    }
  },
  mounted() {
    this.getInfo(this.trainer_list, 'trainerList');
    this.getInfo(this.workout_list, 'workoutList');
  }
}
</script>

<style scoped>
.menu {
  width: 323px;
  height: 0;
}

.table {
  width: 1578px;
  height: 930px;
  margin-left: 330px;
}

.frame {
  width:322px;
  margin-top: -200px;
  margin-left: 7px;
}

iframe {
  margin-top: -100px;
  width:322px;
  height:300px;
  border:none;
  border-radius: 5px;
}
</style>
