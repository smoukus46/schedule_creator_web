<template>
  <Trainer_list
      :isTrainerTooltipVisible="isTrainerTooltipVisible"
      :trainer_list="trainer_list"
      :startTooltipTimer="startTooltipTimer"
      :clearTooltipTimer="clearTooltipTimer"
      :getInfo="getInfo"
      :createLiElem="createLiElem"
      :deleteData="deleteData"
      :onDragStart="onDragStart"
  />
  <Workout_list
      :isWorkoutTooltipVisible="isWorkoutTooltipVisible"
      :workout_list="workout_list"
      :startTooltipTimer="startTooltipTimer"
      :clearTooltipTimer="clearTooltipTimer"
      :getInfo="getInfo"
      :createLiElem="createLiElem"
      :deleteData="deleteData"
      :onDragStart="onDragStart"
  />
</template>

<script>
import Trainer_list from "@/components/trainer_list.vue";
import Workout_list from "@/components/workout_list.vue";

export default {
  components: {Trainer_list, Workout_list},
  props: {
    isTrainerTooltipVisible: {
      type: Boolean,
      required: true
    },
    isWorkoutTooltipVisible: {
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
    getInfo: {
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
    onDragStart: {
      type: Function,
      required: true
    },
    trainer_list: {
      type: Array,
      required: true
    },
    workout_list: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>