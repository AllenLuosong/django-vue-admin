<template>
  <d2-container>
    <template slot="header">UI Case
      <el-button-group>
          <el-button size="small" type="primary" @click="updateRequest"
            ><i class="el-icon-edit" /> 更新</el-button
          >
        </el-button-group>
    </template>
  <div>
    <div class="editor-container">
      <yaml-editor  v-model="yamlData" />
    </div>
  </div>
</d2-container>
</template>

<script>
import YamlEditor from '@/components/YamlEditor/index.vue'
import axios from 'axios'
import { UpdateObj } from './api'
export default {
  name: 'YamlEditorDemo',
  components: { YamlEditor },
  axiosConfig: {
    headers: {
      'Content-Type': 'application/x-yaml'
    }
  },
  data () {
    return {
      yamlData: ''
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    getData () {
      axios.get('/test_demo2_case.yaml').then(response => {
        this.yamlData = response.data
      }).catch((error) => {
        console.error('Error get YAML file:', error)
      })
    },
    updateRequest (obj) {
      const formData = new FormData()
      formData.append('yamlFile', this.yamlData)
      UpdateObj(formData).then(response => {
        console.log('UI用例更新状态:', response.msg)
      })
    }
  }
}
</script>
<style scoped>
.editor-container{
  position: relative;
  height: 100%
}
</style>
