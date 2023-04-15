
<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <d2-crud-x
      ref="d2Crud"
      v-bind="_crudProps"
      v-on="_crudListeners"
      crud.options.tableType="vxe-table"
      view-title="详情"
      :rowHandle="rowHandle"
      :edit-template="editTemplate"
      @row-edit="handleRowEdit"
    >
      <div slot="header">
        <crud-search
          ref="search"
          :options="crud.searchOptions"
          @submit="handleSearch"
        />
      </div>
    </d2-crud-x>
  </d2-container>
</template>

<script>
import * as api from './api'
import { crudOptions } from './crud'
import { d2CrudPlus } from 'd2-crud-plus'
import axios from 'axios'
import YamlEditor from '@/components/YamlEditor/index.vue'

export default {
  name: 'file',
  // components: { YamlEditor },
  mixins: [d2CrudPlus.crud],
  data () {
    return {
      yamlDataValue: '{ abc: "123" }',
      rowHandle: {
        columnHeader: '操作',
        width: 110,
        edit: {
          icon: 'el-icon-edit',
          text: '详情',
          size: 'small',
          fixed: 'right'
        }
      },
      editTemplate: {
        name: {
          title: '文件名称',
          value: '3242',
          component: {
            span: 12
          }
        },
        content: {
          title: '用例内容',
          value: '',
          component: {
            // 插槽,实现文本编辑
            render (h) {
              return h('div', [
                h(YamlEditor, {
                  // ref: 'yaml-editor',
                  props: {
                    value: '{ abc: "123" }'
                  }
                  // on: {
                  //   change: this.updateCode
                  // }
                })
              ])
            }
          }
        }
      }
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    updateCode (value) {
      this.code = value
    },
    getData () {
      return new Promise(resolve => {
        axios.get('/test_demo2_case.yaml').then(response => {
          this.yamlDataValue = response.data
          // console.log(this.yamlDataValue)
          resolve(this.yamlDataValue)
        })
      })
    },
    getCrudOptions () {
      return crudOptions(this)
    },
    pageRequest (query) {
      return api.GetList(query)
    },
    addRequest (row) {
      console.log('api', api)
      return api.AddObj(row)
    },
    updateRequest (row) {
      console.log('----', row)
      return api.UpdateObj(row)
    },
    delRequest (row) {
      return api.DelObj(row.id)
    }
  }
}
</script>

<style lang="scss">
.yxtInput {
  .el-form-item__label {
    color: #49a1ff;
  }
}
.editor-container{
  position: relative;
  height: 100%
}
</style>
