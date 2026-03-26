import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || '/api/v1'

export const getUsers = async () => {
  const response = await axios.get(`${API_URL}/users`)
  return response.data
}

export const createUser = async (userData) => {
  const response = await axios.post(`${API_URL}/users`, userData)
  return response.data
}
