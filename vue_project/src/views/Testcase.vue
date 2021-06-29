
<template>
<div>
    <!-- 新增用例按钮， 点击可以弹出编辑框，做新增用例操作 -->
<template>
    <!-- 添加data-app="true" 解决vuetifybug -->
  <v-row justify="center" data-app="true">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          新增用例
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">新增用例</span>
        </v-card-title>
        <!-- 需要修改弹窗的文本区域 -->
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="测试用例名称"
                  required
                  v-model="caseData.name"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="测试步骤"
                  v-model = "caseData.steps"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="备注"
                  persistent-hint
                  required
                  v-model = "caseData.description"

                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"

          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="addCase()"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
 <tableList
  :headers="headers"
  :desserts="desserts"
 ></tableList>
</div>
</template>

<script>
import tableList from "../components/tableList"
  export default {
    components:{tableList},
    // 每次刷新页面的时候调用这个钩子函数
    mounted(){
      this.selectCase()

    },
    methods: {
        addCase(){
            this.dialog = false
            console.log(this.caseData)
            this.$api.testcase.addTestcase(this.caseData).then((result) => {
              console.log(result)
            })
        },
        selectCase(){
          console.log("查找用例")
            this.$api.testcase.selectTescase().then((result) => {
                this.desserts = result.data
            })
        }
    },
    data () {
      return {
        caseData: {
          name: "",
          steps: "",
          description: "",
        },
        dialog: false,
        //   headers 代表表头， 表头的value 和表体的 key值对应
        headers: [
          {
            text: '测试用例名称',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: '测试步骤', value: 'steps' },
          { text: '备注', value: 'description' },
          { text: '操作', value: 'opertions' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            steps: 159,
            description: 6.0,
            opertions: 24,

          },
          {
            name: 'Ice cream sandwich',
            steps: 237,
            description: 9.0,
            opertions: 37,

          },

        ],
      }
    },
  }
</script>