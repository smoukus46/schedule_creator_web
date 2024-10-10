<template>
<body>
<Menu_bar/>
<Table_component/>
</body>
</template>

<script>
import Menu_bar from "@/components/menu_bar.vue";
import Table_component from "@/components/table_component.vue";

export default {
  components: {Menu_bar, Table_component},
  data() {
    return {
      amount: 0
    }
  }
}
</script>

<style scoped>

</style>
