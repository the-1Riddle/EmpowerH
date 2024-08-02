<template>

    <main class="l-main">
        <!--========== HOME ==========-->
        <section class="services section bd-container" id="services">
            <div style="text-align: center;">
                <div class="home__data">
                    <h1 class="home__title">Contributions</h1>
                </div>
                <br>
                <p></p>
            </div>
        </section>

        <section class="section1 bd-container">
            <div class="container">
                <div class="left_block">
                    <h2 class="section-title" style="text-align: left;">Contribute To EmpowerHer</h2>
                </div>
                <div class="right_block">
                    <p>EmpowerHer is a community-driven platform that relies on the contributions of its members to grow and thrive. We welcome contributions from all members of the community, regardless of their background or experience level. From building features to writing blogs, you can contribute to our community and help make EmpowerHer a better place for everyone.</p>
                </div>
            </div>
        </section>

        <!---- Contributions -----
        <section class="menu section bd-container" id="Chat">
            <div class="post-list menu__container bd-grid">
                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Community Chart </h3>
                        <p>
                            Join our community chat to connect with other members and share your thoughts and experiences.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Forum </h3>
                        <p>
                            Search for discussions or start your own on topics that matter to you.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Report an Issue </h3>
                        <p>
                            Help empowerHer by reporting bugs or issues you encounter on the platform.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>
            </div>
        </section>
        <--- Contributions End --->

        <!---- Whatever lol ---->
        <section class="about section bd-container" id="about">
            <div class="about__container  bd-grid">
                <div class="about__data">
                    <span class="section-subtitle about__initial">Suggestions</span>
                    <h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
                    <p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                    <a href="#" class="button">Explore history</a>
                </div>

                <img src="./Untitled1.jpg" alt="" class="about__img">
            </div>
        </section>
        <!---- Whatever lol End ---->

        <!---- Contributions -----
        <section class="menu section bd-container" id="Wellness">
            <div class="post-list menu__container bd-grid">
                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Community Content </h3>
                        <p>
                            Write blogs or articles on topics that matter to you and share them with the community.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Training </h3>
                        <p>
                            Train and hold events to help other members learn new skills and grow their knowledge.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Platform Development </h3>
                        <p>
                            Help make empowerHer better by contributing to our code base and improving our platform.
                        </p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">Take Action</router-link>
                    </div>
                </div>
            </div>
        </section>
        <--- Contributions End --->

    </main>

</template>