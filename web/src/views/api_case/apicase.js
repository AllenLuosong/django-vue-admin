export const crudOptions = vm => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false
    },
    rowHandle: {
      width: 140,
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
      }
    },
    indexRow: {
      // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },
    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 24, // 默认的表单 span
      width: '35%'
    },
    columns: [{
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 90,
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
      form: {
        editDisabled: true,
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
        editDisabled: true,
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
        editDisabled: true,
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
        editDisabled: true,
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
      type: 'input',
      form: {
        editDisabled: true,
        rules: [
          // 表单校验规则
          { required: true, message: 'IsExecute必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入IsExecute'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }
    ].concat(vm.commonEndColumns())
  }
}
