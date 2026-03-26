import axios from 'axios'

const API_URL = '/api'

export const register = async (userData) => {
  const response = await axios.post(`${API_URL}/register`, userData)
  return response.data
}

export const login = async (userData) => {
  const response = await axios.post(`${API_URL}/login`, userData)
  return response.data
}

export const getProfile = async (access_token) => {
  const response = await axios.get(`${API_URL}/profile`, {
    headers: {
      'Authorization': `Bearer ${access_token}`
    }
  })
  return response.data
}


