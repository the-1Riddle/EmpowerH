<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import Header from './components/Header.vue'
  import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <Header msg="You did it!" />
  </header>

  <!-- the body content -->
  <RouterView />

  <footer>
    <Footer msg="You did it!" />
  </footer>
</template>


<script>
export default {
  mounted() {
    // Custom Bootstrap validation
    (() => {
      'use strict';
      const forms = document.querySelectorAll('.needs-validation');
      Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    })();

    // Show menu
    const showMenu = (toggleId, navId) => {
      const toggle = document.getElementById(toggleId);
      const nav = document.getElementById(navId);
      if (toggle && nav) {
        toggle.addEventListener('click', () => {
          nav.classList.toggle('show-menu');
        });
      }
    };
    showMenu('nav-toggle', 'nav-menu');

    // Close menu on link click
    const navLink = document.querySelectorAll('.nav__link');
    function linkAction() {
      const navMenu = document.getElementById('nav-menu');
      if (navMenu) {
        navMenu.classList.remove('show-menu');
      }
    }
    navLink.forEach(n => n.addEventListener('click', linkAction));

    // Scroll sections active link
    const sections = document.querySelectorAll('section[id]');
    function scrollActive() {
      const scrollY = window.pageYOffset;
      sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionId = current.getAttribute('id');
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link');
        } else {
          document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link');
        }
      });
    }
    window.addEventListener('scroll', scrollActive);

    // Change background header
    function scrollHeader() {
      const nav = document.getElementById('header');
      if (this.scrollY >= 200) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header');
    }
    window.addEventListener('scroll', scrollHeader);

    // Show scroll top
    function scrollTop() {
      const scrollTop = document.getElementById('scroll-top');
      if (this.scrollY >= 560) scrollTop.classList.add('show-scroll'); else scrollTop.classList.remove('show-scroll');
    }
    window.addEventListener('scroll', scrollTop);

    // Dark light theme
    const themeButton = document.getElementById('theme-button');
    const darkTheme = 'dark-theme';
    const iconTheme = 'bx-sun';
    const selectedTheme = localStorage.getItem('selected-theme');
    const selectedIcon = localStorage.getItem('selected-icon');
    const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
    const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx-moon' : 'bx-sun';
    if (selectedTheme) {
      document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
      themeButton.classList[selectedIcon === 'bx-moon' ? 'add' : 'remove'](iconTheme);
    }
    themeButton.addEventListener('click', () => {
      document.body.classList.toggle(darkTheme);
      themeButton.classList.toggle(iconTheme);
      localStorage.setItem('selected-theme', getCurrentTheme());
      localStorage.setItem('selected-icon', getCurrentIcon());
    });

    // Scroll reveal animation
    const sr = ScrollReveal({
      origin: 'top',
      distance: '30px',
      duration: 2000,
      reset: true
    });
    sr.reveal(`.home__data, .home__img,
      .about__data, .about__img,
      .services__content, .menu__content,
      .app__data, .app__img,
      .contact__data, .contact__button,
      .footer__content`, {
      interval: 200
    });
  },
  beforeDestroy() {
    // Clean up event listeners
    window.removeEventListener('scroll', scrollActive);
    window.removeEventListener('scroll', scrollHeader);
    window.removeEventListener('scroll', scrollTop);
    const navLink = document.querySelectorAll('.nav__link');
    navLink.forEach(n => n.removeEventListener('click', linkAction));
  }
};
</script>

<style scoped>
</style>
