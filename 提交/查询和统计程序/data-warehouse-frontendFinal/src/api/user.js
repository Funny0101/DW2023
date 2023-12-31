import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/data-warehouse/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/data-warehouse/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/data-warehouse/user/logout',
    method: 'post'
  })
}
