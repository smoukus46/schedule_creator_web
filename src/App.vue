<template>
<body>
  <div>
    <div class="menu">
    <Menu_bar/>
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
