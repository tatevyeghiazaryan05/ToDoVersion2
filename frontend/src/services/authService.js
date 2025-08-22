import axios from 'axios';

const API_BASE_URL = '/api/user/auth';

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

export const authService = {
  async signup(name, email, password) {
    try {
      const response = await api.post('/sign-up', {
        name,
        email,
        password,
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Signup failed');
    }
  },

  async verifyEmail(email, code) {
    try {
      const response = await api.post('/verify', {
        email,
        code,
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Verification failed');
    }
  },

  async login(email, password) {
    try {
      const response = await api.post('/login', {
        email,
        password,
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Login failed');
    }
  },
};
