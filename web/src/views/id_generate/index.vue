<template>
  <d2-container>
    <el-row>
      <el-col :span="2">
        <label for='numOfRecords'>生成条数:</label>
        <el-input type='number' id='numOfRecords' placeholder="生成条数" v-model='numOfRecords'></el-input>
      </el-col>
      <el-col :span="4">
        <label>开始年份:</label>
        <el-date-picker
          v-model="startYear"
          type="year"
          value='startYear'
          placeholder="选择年份">
        </el-date-picker>
      </el-col>
      <el-col :span="4">
        <label>结束年份:</label>
        <el-date-picker
          v-model="endYear"
          type="year"
          value='endyear'
          placeholder="选择年份">
        </el-date-picker>
      </el-col>
    </el-row>
    <el-button  class="d2-ml-5" type="primary" round @click='generateTable'>生成</el-button>
      <d2-crud-x :columns="columns" :data="records">
    </d2-crud-x>
  </d2-container>
</template>

<script>
import { provinceArray, monthArray, dayArray, familyNamesArray, givenNamesArray } from './crud'

export default {
  data () {
    return {
      prefixCardNo: '602907',
      columns: [
        {
          title: '姓名',
          key: 'name'
        },
        {
          title: '身份证号',
          key: 'idNum'
        },
        {
          title: '手机号',
          key: 'mobileNum'
        },
        {
          title: '卡号',
          key: 'cardNo'
        }
      ],
      numOfRecords: 5,
      startYear: '1990',
      endYear: '2005',
      records: []
    }
  },
  mounted () {
    this.generateTable()
  },
  methods: {
    random (max, min) {
      return Math.floor(Math.random() * (max - min + 1) + min)
    },
    generateTable () {
      this.records = []
      for (let i = 0; i < this.numOfRecords; i++) {
        const record = {
          name: this.generateName(),
          idNum: this.generateId(),
          mobileNum: this.generatePhone(),
          cardNo: this.generateCardNum()
        }
        this.records.push(record)
      }
    },
    generateId () {
      const startStr = new Date(this.startYear)
      const startYearStr = startStr.getFullYear()
      const endeStr = new Date(this.endYear)
      const endYearStr = endeStr.getFullYear()
      const randomIndex = Math.floor(Math.random() * provinceArray.length)
      const randomElement = provinceArray[randomIndex] // 随机输出一个6位数的行政区域值
      const birthday = this.random(Number(startYearStr), Number(endYearStr)) + monthArray[this.random(0, monthArray.length - 1)] + dayArray[this.random(0, dayArray.length - 1)]
      let id = randomElement + birthday + ''
      // 生成前17位数字
      for (let i = 0; i < 3; i++) {
        id += Math.floor(Math.random() * 10)
      }
      // 生成最后一位校验码
      let sum = 0
      for (let i = 0; i < 17; i++) {
        sum += parseInt(id[i]) * (Math.pow(2, 17 - i) % 11)
      }
      const checksum = (12 - (sum % 11)) % 11
      if (checksum === 10) {
        id += 'X'
      } else {
        id += checksum
      }
      return id
    },
    generatePhone () {
      const prefixMobileNumArray = ['13', '14', '15', '16', '17', '18', '19']
      return prefixMobileNumArray[Math.floor(Math.random() * prefixMobileNumArray.length)] + Math.floor(Math.random() * 899999999 + 100000000)
    },
    generateCardNum () {
      return this.prefixCardNo + Math.floor(Math.random() * 899999999 + 1000000000)
    },
    generateName () {
      const familyName = familyNamesArray[Math.floor(Math.random() * familyNamesArray.length)]
      const givenName = givenNamesArray[Math.floor(Math.random() * givenNamesArray.length)]
      return familyName + givenName
    }
  }
}
</script>
