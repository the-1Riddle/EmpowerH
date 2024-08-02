<template>

    <main class="l-main">
        <!--========== HOME ==========-->
        <section class="services section bd-container" id="services">
            <div style="text-align: center;">
                <div class="home__data">
                    <h1 class="home__title">EmpowerHer Blog</h1>
                </div>
            </div>
            <br>
            <hr>
            <ul class="nav-list">
                <li class="nav-item nav-left"><a href="/Wellness" class="nav__link">Wellness</a></li>
                <li class="nav-item nav-center"><a href="#Awareness" class="nav__link">Sexual Awareness</a></li>
                <li class="nav-item nav-right"><a href="/gender-violence" class="nav__link">Gender Violence</a></li>
            </ul>
            <hr>
        </section>

        <section class="section1 bd-container">
            <div class="container">
                <div class="left_block">
                    <p>Articles About</p>
                    <h2 class="section-title" style="text-align: left;">Sexual Awareness</h2>
                </div>
                <div class="separator"></div>
                <div class="right_block">
                    <p><b>Empowering Girls, One Conversation at a Time</b><br>
                    At Sexual Awareness for Girls, we are dedicated to providing knowledge, support, and empowerment to girls on their journey of understanding their bodies, boundaries, and safety. Let's explore together!.</p>
                </div>
            </div>
        </section>
        
        <!---- Popular Post ---->
        <section class="about section1 bd-container" id="about">
            <div class="about__container  bd-grid">
                <div class="about__data">
                    <span class="section-subtitle about__initial">Popular Post</span>
                    <h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
                    <p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                    <a href="#" class="button">Explore history</a>
                </div>

                <img src="./Untitled1.jpg" alt="" class="about__img">
            </div>
        </section>
        <!---- Popular Post End ---->

        <!-- Contents from the previouse version -->
        <section id="introduction">
            <h2>Welcome to Sexual Awareness for Girls!</h2>
            <p class="intro">
                <b>Empowering Girls, One Conversation at a Time</b><br>
                At Sexual Awareness for Girls, we are dedicated to providing knowledge, support, and empowerment to girls on their journey of understanding their bodies, boundaries, and safety. Let's explore together!
            </p>
        </section>

        <section id="topics">
            <h2>Topics We'll Cover</h2>
            <ul>
                <li><a href="#body-autonomy">Body Autonomy and Boundaries</a></li>
                <li><a href="#anatomy">Understanding Female Reproductive Anatomy</a></li>
                <li><a href="#puberty">Understanding Puberty</a></li>
                <li><a href="#consent">Understanding Consent</a></li>
                <li><a href="#healthy-relationships">Building Healthy Relationships</a></li>
                <li><a href="#self-care">Self-Care and Self-Love</a></li>
            </ul>
        </section>

        <section id="body-autonomy">
            <h2>Body Autonomy and Boundaries</h2>
            <p>
                Body autonomy is the right to have control over your own body. In this section, you will learn how to set boundaries, communicate them assertively, and respect the boundaries of others.
            </p>
        </section>

        <section id="anatomy">
            <h2>Understanding Female Reproductive Anatomy</h2>
            <p>
                Explore the fascinating world of female reproductive anatomy. This section provides diagrams and explanations suitable for your age group, helping you understand your body better.
            </p>
        </section>

        <section id="puberty">
            <h2>Understanding Puberty</h2>
            <p>
                Puberty is a time of significant physical and emotional changes. In this section, you will discover what to expect during puberty and learn how to navigate these changes with confidence.
            </p>
        </section>

        <section id="consent">
            <h2>Understanding Consent</h2>
            <p>
                Consent is a crucial aspect of healthy relationships. Here, you will learn about the importance of consent, how to recognize and respect boundaries, and how to communicate your desires and limits effectively.
            </p>
        </section>

        <section id="healthy-relationships">
            <h2>Building Healthy Relationships</h2>
            <p>
                Healthy relationships are built on trust, respect, and effective communication. This section will help you understand what makes a relationship healthy, identify red flags, and cultivate positive connections with others.
            </p>
        </section>

        <section id="self-care">
            <h2>Self-Care and Self-Love</h2>
            <p>
                Taking care of yourself is essential for your overall well-being and happiness. Explore the importance of self-care, self-love, and self-acceptance in this section, and discover practical ways to prioritize your own needs.
            </p>
        </section>
        <!-- Contents from the previouse version End -->

        <!---- Sexual Awareness -----
        <section class="menu section1 bd-container" id="Wellness">
            <div class="post-list menu__container bd-grid">
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

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Post title </h3>
                        <div class="post-meta">
                            <span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
                            <span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> 23-02-2025</span>
                        </div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Post title </h3>
                        <div class="post-meta">
                            <span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author - </span>
                            <span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
                        </div>
                        <p>{{ getPostDescription(post) }}</p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
                    </div>
                </div>
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

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Post title </h3>
                        <div class="post-meta">
                            <span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author</span>
                            <span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> 23-02-2025</span>
                        </div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
                    </div>
                </div>

                <div v-for="post in paginatedPosts" :key="post.id" class="post-card">
                    <img src="./Untitled1.jpg" alt="Post image" class="post-image"/>
                    <div class="post-content">
                        <h3>Post title </h3>
                        <div class="post-meta">
                            <span class="author"><span class="material-symbols-outlined" style="position:relative; top:4px;">person</span> Author - </span>
                            <span class="date"><span class="material-symbols-outlined" style="position:relative; top:4px;">calendar_month</span> {{ formatDate(post.created_at) }}</span>
                        </div>
                        <p>{{ getPostDescription(post) }}</p>
                        <router-link :to="{ name: 'postpage', params: { id: post.id } }" class="read-more">read more »</router-link>
                    </div>
                </div>
            </div>
        </section>
        <--- Sexual Awareness End --->

    </main>

</template>