<template>
  <Workout_table
      :showModal="showModal"
      :closeModal="closeModal"
  />
</template>

<script>
import Workout_table from "@/components/workout_table.vue";

export default {
  components: {Workout_table},
  props: {
    showModal: {
      type: Function,
      required: true
    },
    closeModal: {
      type: Function,
      required: true
    }
  }
}
</script>

<style scoped>

</style>