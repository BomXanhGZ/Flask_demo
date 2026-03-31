import router from '../router/index'

const getProfile = (token) => {
  // Lưu một object user tạm thời chứa token để ProfileView.vue có thể sử dụng (vì ProfileView đang mong đợi user.access_token)
  localStorage.setItem('user', JSON.stringify({ access_token: token }))
  router.push('/profile')
}

export default getProfile