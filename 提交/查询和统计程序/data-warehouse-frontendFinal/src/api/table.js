import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/data-warehouse/table/list',
    method: 'get',
    params
  })
}
