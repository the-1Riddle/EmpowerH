import { createRouter, createWebHistory } from 'vue-router'
import Signup from '../views/Signup.vue';
import Login from '../views/Login.vue';
import Home from '../views/Home.vue';
import Blog from '../views/Blog.vue';
import Wellness from '../views/Wellness.vue';
import SexualAwareness from '../views/SexualAwareness.vue';
import GenderViolence from '../views/GenderViolence.vue';
import BlogPage from '../views/BlogPage.vue';
import PrivacyPolicy from '../views/PrivacyPolicy.vue';
import TermsAndConditions from '../views/TermsAndConditions.vue';
import Account from '../views/Account.vue';
import About from '../views/About.vue';
import Contact from '../views/Contact.vue';
import Forum from '../views/Forum.vue';
import ForumPage from '../views/ForumPage.vue';
import Events from '../views/Events.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/signup', name: 'signup', component: Signup },
    { path: '/login', name: 'login', component: Login },
    { path: '/', name: 'home', component: Home },
    { path: '/blog', name: 'blog', component: Blog },
    { path: '/blogpage/:id', name: 'blogpage', component: BlogPage },
    { path: '/sexual-awareness', name: 'sexual-awareness', component: SexualAwareness },
    { path: '/gender-violence', name: 'gender-violence', component: GenderViolence },
    { path: '/privacy-policy', name: 'privacy-policy', component: PrivacyPolicy },
    { path: '/terms-and-conditions', name: 'terms-and-conditions', component: TermsAndConditions },
    { path: '/wellness', name: 'wellness', component: Wellness },
    { path: '/account', name: 'account', component: Account },
    { path: '/about', name: 'about', component: About },
    { path: '/contact', name: 'contact', component: Contact },
    { path: '/forum', name: 'forum', component: Forum },
    { path: '/forumpage', name: 'forumpage', component: ForumPage },
    { path: '/events', name: 'events', component: Events },
  ]
})

export default router
