import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

apiClient.interceptors.request.use(
  config => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default {
  getPosts() {
    return apiClient.get('/posts/');
  },
  getPostById(postId) {
    return apiClient.get(`/posts/${postId}`);
  },
  createPost(postData, config) {
    return apiClient.post('/posts/', postData, config);
  },
  deletePost(postId) {
    return apiClient.delete(`/posts/${postId}`);
  },
  getUsers() {
    return apiClient.get('/users/');
  },
  getUserByEmail(email) {
    return apiClient.get(`/users/email/${email}`);
  },
  async createUser(userData) {
    try {
      const response = await apiClient.post('/users/', userData);
      return response;
    } catch (error) {
      console.error('API Error:', error.response);
      throw error;
    }
  },
  deleteUser(userId) {
    return apiClient.delete(`/users/${userId}`);
  },
  getComments(postId) {
    return apiClient.get(`/comments?post_id=${postId}`);
  },
  createComment(commentData) {
    const { user_email, ...data } = commentData;
    return apiClient.post(`/comments/?user_email=${encodeURIComponent(user_email)}`, data);
  },
  deleteComment(commentId) {
    return apiClient.delete(`/comments/${commentId}`);
  },
  loginUser(loginData) {
    const params = new URLSearchParams();
    params.append('username', loginData.username);
    params.append('password', loginData.password);
    return apiClient.post('/token', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
    .then(response => {
      // Store the access token in localStorage
      localStorage.setItem('access_token', response.data.access_token);
      return response;
    })
    .catch(error => {
      console.error("Login API call failed", error);
      throw error;
    });
  },
  getUserDetails() {
    return apiClient.get('/users/me/')
    .catch(error => {
      console.error("Get user details API call failed", error);
      throw error;
    });
  },
  signupUser(signupData) {
    return apiClient.post('/users/', signupData);
  },
  contactForm(formData, config) {
    return apiClient.post('/contact-mail/', formData, config);
  },
  updatePassword(userEmail, passwordData) {
    return apiClient.post(`/password-update`, { email: userEmail, ...passwordData });
  }
};
