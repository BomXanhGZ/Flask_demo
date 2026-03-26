import axios from 'axios'

const API_URL = '/api'

export const createUser = async (userData) => {
  const response = await axios.post(`${API_URL}/register`, userData)
  return response.data
}

export const login = async (userData) => {
  const response = await axios.post(`${API_URL}/login`, userData)
  return response.data
}

export const getProfile = async (id) => {
  const response = await axios.get(`${API_URL}/profile/${id}`)
  return response.data
}


