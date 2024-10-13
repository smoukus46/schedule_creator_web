<template>
<body>
  <div>
    <div class="menu">
      <Menu_bar
          :isTrainerTooltipVisible="isTrainerTooltipVisible"
          :isWorkoutTooltipVisible="isWorkoutTooltipVisible"
          :startTooltipTimer="startTooltipTimer"
          :clearTooltipTimer="clearTooltipTimer"
      />
    </div>
    <div class="table">
      <Table_component/>
    </div>
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

export default {
  components: {Trainer_list, Menu_bar, Table_component},
  data() {
    return {
      isTrainerTooltipVisible: false,
      isWorkoutTooltipVisible: false,
      tooltipTimer: null
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
    }
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
