<template>

	<main class="l-main">
		<!------------ HOME ------------>
		<section class="services section bd-container" id="services">
			<div style="text-align: center;">
				<div class="home__data">
					<h1 class="home__title">EmpowerHer Blog</h1>
				</div>
			</div>
			<br>
			<hr>
			<ul class="nav-list">
				<li class="nav-item nav-left"><a href="#Wellness" class="nav__link">Wellness</a></li>
				<li class="nav-item nav-center"><a href="#Awareness" class="nav__link">Sexual Awareness</a></li>
				<li class="nav-item nav-right"><a href="#Gender" class="nav__link">Gender Violence</a></li>
			</ul>
			<hr>
		</section>

		<!---- Popular Post ---->
		<section class="about section bd-container" id="about">
			<div class="about__container  bd-grid">
				<div class="about__data">
					<span class="section-subtitle about__initial">Popular Post</span>
					<h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
					<p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
					<a href="#" class="button">Explore history</a>
				</div>

				<img src="../assets/img/about.jpg" alt="" class="about__img">
			</div>
		</section>
		<!---- Popular Post End ---->

		<!---- Wellness ----->
		<section class="menu section bd-container" id="Wellness">
			<h2 class="section-title" style="text-align: left;">Wellness</h2>
			<hr>

			<div class="menu__container bd-grid">
				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>
			</div>
			<br>
			<div class="content-subtitle">
				<a href="/Wellness"><span class="content-subtitle"> Read More »</span></a>
			</div>
		</section>
		<!--- Wellness End --->

		<!---- Sexual Awareness ---->
		<section class="menu section bd-container" id="Awareness">
			<h2 class="section-title" style="text-align: left;">Sexual Awareness</h2>
			<hr>

			<div class="menu__container bd-grid">
				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>
			</div>
			<br>
			<div class="content-subtitle">
				<a href="/sexual-awareness"><span class="content-subtitle"> Read More »</span></a>
			</div>
		</section>
		<!---- Sexual Awareness End ---->

		<!---- Gender Violence ---->
		<section class="menu section bd-container" id="Gender">
			<h2 class="section-title" style="text-align: left;">Gender Violence</h2>
			<hr>

			<div class="menu__container bd-grid">
				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>

				<div>
					<div v-for="post in paginatedPosts" :key="post.id" class="post-card">
						<img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
						<div class="post-content">
							<h3>Post title </h3>
							<div class="post-meta">
								<span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
								<span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
							</div>
							<p>{{ getPostDescription(post) }}</p>
							<router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
						</div>
					</div>
				</div>
			</div>
			<br>
			<div class="content-subtitle">
				<a href="/gender-violence"><span class="content-subtitle"> Read More »</span></a>
			</div>
		</section>
		<!---- Gender Violence End ---->
	</main>

</template>


<script>
import api from '../api';

export default {
  data() {
    return {
      posts: [],
      currentPage: 1,
      postsPerPage: 12,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.posts.length / this.postsPerPage);
    },
    paginatedPosts() {
      const start = (this.currentPage - 1) * this.postsPerPage;
      const end = start + this.postsPerPage;
      return this.posts.slice(start, end);
    },
  },
  async created() {
    await this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await api.getPosts();
        this.posts = response.data;
      } catch (error) {
        console.error('Error fetching posts:', error);
        alert('Error fetching posts. Please try again later.');
      }
    },
    getImageUrl(imagePath) {
      return `http://localhost:8000/static/Pictures/${imagePath}`;
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    getPostDescription(post) {
      if (post.image) {
        return this.getPlaceholderText(post.post_desc, 15);
      } else {
        return this.getPlaceholderText(post.post_desc, 45);
      }
    },
    getPlaceholderText(text, numWords) {
      const words = text.split(' ');
      return words.length > numWords ? words.slice(0, numWords).join(' ') + '...' : text;
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    goToPage(page) {
      this.currentPage = page;
    },
  },
};
</script>