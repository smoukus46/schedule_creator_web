<template>
  <Trainer_list/>
  <Workout_list/>
</template>

<script>
import Trainer_list from "@/components/trainer_list.vue";
import Workout_list from "@/components/workout_list.vue";
//import Workout_table from "@/components/workout_table.vue";

export default {
  components: {Trainer_list, Workout_list},
  props: {

  }
}
</script>

<style scoped>

</style>