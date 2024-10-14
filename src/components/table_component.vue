<template>
  <Workout_table
      :showModal="showModal"
      :showErrorModal="showErrorModal"
      :closeLoadingModal="closeLoadingModal"
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
    showErrorModal: {
      type: Function,
      required: true
    },
    closeLoadingModal: {
      type: Function,
      required: true
    }
  }
}
</script>

<style scoped>

</style>