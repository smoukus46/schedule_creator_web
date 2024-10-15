<template>
  <Workout_table
      :tableRows="tableRows"
      :showModal="showModal"
      :showErrorModal="showErrorModal"
      :closeLoadingModal="closeLoadingModal"
      :onDrop="onDrop"
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
    onDrop: {
      type: Function,
      required: true
    }
  }
}
</script>

<style scoped>

</style>