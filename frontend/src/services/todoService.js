import axios from 'axios';

const API_BASE_URL = '/api/todo';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const todoService = {
  async getAllTodos() {
    try {
      const response = await api.get('/get/all/todo');
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch todos');
    }
  },

  async getTodoById(todoId) {
    try {
      const response = await api.get(`/get/todo/${todoId}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch todo');
    }
  },

  async createTodo(todoData) {
    try {
      const response = await api.post('/add/todo', todoData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to create todo');
    }
  },

  async updateTodo(todoId, todoData) {
    try {
      const response = await api.put(`/change/${todoId}`, todoData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to update todo');
    }
  },

  async deleteTodo(todoId) {
    try {
      const response = await api.delete(`/delete/todo/${todoId}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete todo');
    }
  },
};
