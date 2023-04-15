<template>
  <d2-container>
    <template slot="header">请选择用例文件
      <el-select v-model="selectedFile" placeholder="选择文件" @change="loadFile">
      <el-option v-for="file in files" :key="file" :label="file" :value="file"></el-option>
    </el-select>
    <el-button class="d2-ml-5" type="primary" round @click="updateFile">
      更新用例文件
    </el-button>
    </template>
    <div class="editor-container">
      <yaml-editor  v-model="yamlData"/>
    </div>
</d2-container>
</template>

<script>
import YamlEditor from '@/components/YamlEditor/index.vue'
import axios from 'axios'
import { UpdateObj } from './api'
import { Message } from 'element-ui'

export default {
  name: 'Uicase',
  components: { YamlEditor },
  data () {
    return {
      selectedFile: 'test_demo2_case.yaml',
      files: ['test_demo2_case.yaml', 'test_demo3_case.yaml', 'test_demo4_case.yaml'],
      yamlData: ''
    }
  },
  mounted () {
    this.loadFile()
  },
  methods: {
    loadFile () {
      axios.get(`/${this.selectedFile}`).then(response => {
        this.yamlData = response.data
      }).catch((error) => {
        console.error('Error get YAML file:', error)
      })
    },
    updateFile () {
      const formData = new FormData()
      formData.append('yamlFile', this.yamlData)
      UpdateObj(formData).then(response => {
        const retcode = response.code
        if (retcode === 2000) {
          Message({
            message: response.msg,
            type: 'success',
            duration: 3 * 1000
          })
        } else {
          Message({
            message: response.msg,
            type: 'error',
            duration: 3 * 1000
          })
        }
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
