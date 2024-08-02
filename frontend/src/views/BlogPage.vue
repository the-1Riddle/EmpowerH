<template>

    <main class="l-main">
        <!--========== HOME ==========-->
        <section class="services section bd-container" id="services">
            <div style="text-align: center;">
                <div class="home__data">
                    <h1 class="home__title">Single Article</h1>
                </div>
            </div>
        </section>

        <!---------- Blog Body ----------->
        <section class="section1 bd-container">
            <div class="mt-150 mb-150">
              <div class="container">
                <div class="row">
                  <div class="col-lg-8">
                    <div class="single-article-section" v-if="post">
                      <div class="single-article-text">
                        <div v-if="post.image">
                          <img :src="getImageUrl(post.image)" alt="Post Image" class="post-image"/>
                        </div>
                        <p class="blog-meta">
                          <br>
                          <span class="author"><i class="bi bi-person-fill"></i> Author - {{ fetchUserByEmail(post.user_email).user_name }} &emsp;</span>
                          <span class="date"><i class="bi bi-calendar4-week"></i> {{ formatDate(post.created_at) }} </span>
                        </p>
                        <div class="post-options" v-if="post.user_email === currentUser">
                          <a @click="togglePostOptions"><strong> . . . </strong></a>
                          <div v-if="showPostOptions" class="options-menu">
                            <button @click="deletePost">Delete</button>
                          </div>
                        </div>
                        <h2 class="section-title">{{ post.post_title }}</h2>
                        <p>{{ post.post_desc }}</p>
                      </div>

                      <div class="comments-list-wrap">
                        <h3 class="comment-count-title">{{ comments.length }} Comments</h3>
                        <div class="comment-list">
                          <div v-for="comment in comments" :key="comment.id" class="single-comment-body">
                            <div class="comment-user-avater">
                              <img src="../../assets/img/user-image.svg" alt="User Avatar" style="width: 50px;">
                            </div>
                            <div class="comment-text-body">
                              <h4>{{ fetchUserByEmail(comment.user_email).user_name }} &emsp;<span class="comment-date">{{ formatDate(post.created_at) }}</span></h4>
                              <p>{{ comment.comments_data }}</p>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div class="comment-template">
                    	<div class="dropdown">
                    		<a href="#" type="button" class="section-subtitle dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
                    		  Comment
                    		</a>
	                    	<div class="dropdown-menu">
		                        <form @submit.prevent="handleSubmit" class="px-2 py-3">
		                        	<h4 style="text-align: center;">Leave a comment</h4>
		                        	<p>If you have a comment don't hesitate to send us your opinion.</p>
		                        	<br>
		                        	<div class="mb-3">
		                        		<p><textarea v-model="newComment.comments_data" class="form-control" id="floatingTextarea2" rows="10" placeholder="Your Message" required></textarea></p>
		                        		<br>
		                        		<p><input type="submit" class="btn btn-primary" value="Submit"></p>
		                        	</div>
		                        </form>
	                    	</div>
                    	</div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4">
                    <div class="sidebar-section">
                      <div class="recent-posts">
                        <h4>Recent Posts</h4>
                        <ul>
                          <!-- Loop and display the first 5 recent posts -->
                          <li v-for="recentPost in recentPosts.slice(0, 5)" :key="recentPost.id"><a :href="`/postpage/${recentPost.id}`">{{ recentPost.post_title }}</a></li>
                        </ul>
                      </div>
                      <div class="tag-section">
                        <h4>Tags</h4>
                        <ul>
                          <!-- Add tags manually -->
                          <li><a href="/gender-violence">Gender Violence</a></li>
                          <li><a href="/sexual-awareness">Sexual Awareness</a></li>
                          <li><a href="/wellness">Wellness</a></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </section>
        <!---------- Blog Body End ----------->

    </main>

</template>

<script>
import { ref, onMounted } from 'vue';
import api from '../api';

export default {
  setup() {
    const userName = ref('');
    const currentUser = ref('');

    const fetchUserDetails = async () => {
      try {
        const response = await api.getUserDetails();
        userName.value = response.data.user_name;
        currentUser.value = response.data.user_email;
      } catch (error) {
        console.error("Failed to fetch user details:", error);
      }
    };

    onMounted(() => {
      fetchUserDetails();
    });

    return {
      userName,
      currentUser
    };
  },
  data() {
    return {
      post: null,
      comments: [],
      newComment: {
        user_email: '',
        comments_data: '',
      },
      users: [],
      showPostOptions: false,
      showCommentOptions: {},
      recentPosts: []
    };
  },
  async created() {
    const postId = this.$route.params.id;
    await this.fetchPost(postId);
    await this.fetchComments(postId);
    await this.fetchUsers();
    await this.fetchRecentPosts();
  },
  watch: {
    currentUser(newEmail) {
      this.newComment.user_email = newEmail;
    }
  },
  methods: {
    async fetchPost(postId) {
      try {
        const response = await api.getPostById(postId);
        this.post = response.data;
      } catch (error) {
        console.error('Error fetching post:', error);
      }
    },
    async fetchComments(postId) {
      try {
        const response = await api.getComments(postId);
        this.comments = response.data;
      } catch (error) {
        console.error('Error fetching comments:', error);
      }
    },
    async fetchUsers() {
      try {
        const response = await api.getUsers();
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async fetchRecentPosts() {
      try {
        const response = await api.getPosts();
        this.recentPosts = response.data;
      } catch (error) {
        console.error('Error fetching recent posts:', error);
      }
    },
    fetchUserByEmail(userEmail) {
      return this.users.find(user => user.user_email === userEmail) || {};
    },
    getImageUrl(imagePath) {
      const baseUrl = 'http://localhost:8000';
      return `${baseUrl}/static/Pictures/${imagePath}`;
    },
    handleSubmit() {
      console.log('Form submitted with:', this.newComment);
      this.addComment();
    },
    async addComment() {
      try {
        const postId = this.post.id;
        const commentData = {
          post_id: postId,
          ...this.newComment,
        };
        console.log('Submitting new comment:', commentData);
        const response = await api.createComment(commentData);
        console.log('Comment creation response:', response);
        await this.fetchComments(postId);
        this.newComment = { user_email: this.currentUser, comments_data: '' };
      } catch (error) {
        console.error('Error adding comment:', error);
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    togglePostOptions() {
      this.showPostOptions = !this.showPostOptions;
    },
    async deletePost() {
      try {
        await api.deletePost(this.post.id);
        this.$router.push({ name: 'posts' });
      } catch (error) {
        console.error('Error deleting post:', error);
      }
    },
    toggleCommentOptions(commentId) {
      this.$set(this.showCommentOptions, commentId, !this.showCommentOptions[commentId]);
    },
    async deleteComment(commentId) {
      try {
        await api.deleteComment(commentId);
        this.comments = this.comments.filter(comment => comment.id !== commentId);
      } catch (error) {
        console.error('Error deleting comment:', error);
      }
    }
  }
};
</script>