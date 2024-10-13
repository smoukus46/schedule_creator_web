<template>
  <Trainer_list
      :isTrainerTooltipVisible="isTrainerTooltipVisible"
      :startTooltipTimer="startTooltipTimer"
      :clearTooltipTimer="clearTooltipTimer"
  />
  <Workout_list
      :isWorkoutTooltipVisible="isWorkoutTooltipVisible"
      :startTooltipTimer="startTooltipTimer"
      :clearTooltipTimer="clearTooltipTimer"
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
    }
  }
}
</script>

<style scoped>

</style>