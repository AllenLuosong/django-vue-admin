import { request } from '@/api/service'
export const urlPrefix = '/api/uicase/'

export function GetList () {
  return request({
    url: urlPrefix,
    method: 'get'
  })
}

export function UpdateObj (obj) {
  return request({
    url: urlPrefix + '1' + '/',
    method: 'put',
    data: obj,
    Headers: { 'Content-Type': 'multipart/form-data' }
  })
}
