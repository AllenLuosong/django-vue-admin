<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <template slot="header">API Case</template>
    <d2-crud-x ref="d2Crud" v-bind="_crudProps" v-on="_crudListeners">
      <!-- 自动绑定参数与事件 -->
      <!-- 包含详细参数见：https://gitee.com/greper/d2-crud-plus/blob/master/packages/d2-crud-plus/src/lib/mixins/crud.js#L164-->
      <div slot="header">
        <crud-search
          ref="search"
          :options="crud.searchOptions"
          @submit="handleSearch"
        />
        <el-button-group>
          <el-button size="small" type="primary" @click="addRow"
            ><i class="el-icon-plus" /> 新增</el-button
          >
        </el-button-group>
        <crud-toolbar v-bind="_crudToolbarProps" v-on="_crudToolbarListeners" />
      </div>
    </d2-crud-x>
  </d2-container>
</template>

<script>
import { crudOptions } from './apicase' // 上文的crudOptions配置
import { d2CrudPlus } from 'd2-crud-plus'
import { AddObj, GetList, UpdateObj, DelObj } from './api' // 查询添加修改删除的http请求接口
export default {
  name: 'curd_demo',
  mixins: [d2CrudPlus.crud], // 最核心部分，继承d2CrudPlus.crud
  methods: {
    getCrudOptions () {
      return crudOptions(this)
    },
    pageRequest (query) {
      return GetList(query)
    }, // 数据请求
    addRequest (row) {
      return AddObj(row)
    }, // 添加请求
    updateRequest (row) {
      return UpdateObj(row)
    }, // 修改请求
    delRequest (row) {
      return DelObj(row.id)
    } // 删除请求
  }
}
</script>
