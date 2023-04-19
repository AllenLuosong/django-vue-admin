export const crudOptions = vm => {
  return {
    options: {
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      rowKey: 'id'
    },
    viewOptions: {
      componentType: 'row'
    },
    pageOptions: {
      compact: true // 是否紧凑型页面
    },
    rowHandle: {
      width: 200,
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      },
      fixed: 'right' // 右边固定列
    },
    indexRow: {
      // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      fixed: 'left',
      width: 100
    },
    formOptions: {
      defaultSpan: 20, // 默认的表单 span
      maxHeight: true,
      labelWidth: '30%',
      width: '50%'
    },
    columns: [{
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 120,
      fixed: 'left',
      form: {
        disabled: true
      }
    },
    {
      title: 'CaseNo',
      key: 'CaseNo',
      sortable: true,
      treeNode: true,
      type: 'input',
      fixed: 'left',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: 'CaseNo必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入CaseNo'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: 'Summary',
      key: 'Summary',
      sortable: true,
      search: {
        component: {
          props: {
            clearable: true
          }
        }
      },
      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: 'Summary必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入Summary'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: 'Domain',
      key: 'Domain',
      sortable: true,
      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: 'Domain必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入Domain'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: 'InterfacePath',
      key: 'InterfacePath',
      sortable: true,
      type: 'input',
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: 'InterfacePath必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入InterfacePath'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: 'IsExecute',
      key: 'IsExecute',
      sortable: true,
      type: 'select',
      dict: {
        data: [{ label: 'Y', value: 'Y' }, { label: 'N', value: 'N' }]
      },
      form: {
        editDisabled: false,
        rules: [
          // 表单校验规则
          { required: true, message: 'IsExecute必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请选择IsExecute'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }
    ].concat(vm.commonEndColumns())
  }
}
