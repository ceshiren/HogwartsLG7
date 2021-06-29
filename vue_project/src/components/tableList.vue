
<template>
       <!-- 用例的展示列表 -->
    <!-- 展示列表需要可以编辑 -->
  <v-data-table
    :headers="headers"
    :items="desserts"
    :items-per-page="10"
    class="elevation-1"
  >
  <!-- 需要把原本的actions 改为 operations，因为下面的数据，表头，表体都是使用的operations -->
      <template v-slot:item.opertions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  
  </v-data-table>
</template>

<script>
export default {
    props: ["headers", "desserts"]
}
</script>