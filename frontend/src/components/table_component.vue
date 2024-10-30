<template>
  <Workout_table
      :tableRows="tableRows"
      :showModal="showModal"
      :showErrorModal="showErrorModal"
      :closeLoadingModal="closeLoadingModal"
      :draggedItem="draggedItem"
  />
</template>

<script>
import Workout_table from "@/components/workout_table.vue";

export default {
  components: {Workout_table},
  props: {
    tableRows: {
      type: Array,
      required: true
    },
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
    },
    draggedItem: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

</style>