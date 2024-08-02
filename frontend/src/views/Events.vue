<template>

    <main class="l-main">
        <!--========== HOME ==========-->
        <section class="services section bd-container" id="services">
            <div style="text-align: center;">
                <div class="home__data">
                    <h1 class="home__title"> Events</h1>
                </div>
                <br>
                <p></p>
            </div>
        </section>
        <section class="section1 bd-container">
            <ul class="nav nav-pills">
            	<li class="nav-item">
                	<a class="nav-link active" aria-current="page" href="#">Overview</a>
            	</li>
            	<li class="nav-item">
                	<a class="nav-link" href="#">Upcoming</a>
            	</li>
            	<li class="nav-item">
                	<a class="nav-link" href="#">Past Events</a>
            	</li>
            </ul>
        </section>

        <section class="section1 bd-container">
            <div class="container">
                <div class="left_block">
                    <h2 class="section-title" style="text-align: left;">EmpowerHer Events</h2>
                </div>
                <div class="right_block">
                    <p>
                    	Welcome to connect with the EmpowerHer team at conferences, meetups, and other events online and in-person year-round across the globe. We are excited to meet you and share our mission to empower and uplift all women. Join us at our next event and become part of our community.
                    </p>
                </div>
            </div>
        </section>

        <!---- Contributions -----
        <section class="menu section bd-container" id="Wellness">
            <h2 class="section-title" style="text-align: left;">Upcoming Events</h2>
            <hr>
            <div class="post-list menu__container bd-grid">
                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Upcoming Events 1 </h3>
                        <p>
                            Join our community chat to connect with other members and share your thoughts and experiences.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Upcoming Events 2</h3>
                        <p>
                            Search for discussions or start your own on topics that matter to you.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Upcoming Events 3 </h3>
                        <p>
                            Help empowerHer by reporting bugs or issues you encounter on the platform.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>
            </div>
            <br>
            <div class="content-subtitle">
                <a href="#"><span class="content-subtitle"> View More »</span></a>
            </div>
        </section>
        <--- Contributions End --->

        <!---- Whatever lol ---->
        <section class="about section1 bd-container" id="about">
            <div class="about__container  bd-grid">
                <div class="about__data">
                    <span class="section-subtitle about__initial">Suggestions</span>
                    <h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
                    <p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                </div>

                <img src="./Untitled1.jpg" alt="" class="about__img">
            </div>
        </section>

        <section class="about section1 bd-container" id="about">
            <div class="about__container  bd-grid">
                <div class="about__data">
                    <span class="section-subtitle about__initial">Suggestions</span>
                    <h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
                    <p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                </div>
            </div>

            <img src="./Untitled1.jpg" alt="" class="home__img">
        </section>

        <!---- Whatever lol End ---->

        <!---- Contributions -----
        <section class="menu section1 bd-container" id="Wellness">
            <h2 class="section-title" style="text-align: left;">Past Events</h2>
            <hr>
            <div class="post-list menu__container bd-grid">
                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Past Event 1 </h3>
                        <p>
                            Write blogs or articles on topics that matter to you and share them with the community.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Past Event 2 </h3>
                        <p>
                            Train and hold events to help other members learn new skills and grow their knowledge.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Past Event 3 </h3>
                        <p>
                            Help make empowerHer better by contributing to our code base and improving our platform.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>
            </div>
            <br>
            <div class="content-subtitle">
                <a href="#"><span class="content-subtitle"> View More »</span></a>
            </div>
        </section>
        <--- Contributions End --->
    </main>

</template>