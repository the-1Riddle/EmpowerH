<template>
  <header class="l-header" id="header">
    <nav class="nav bd-container">
      <a href="/" class="nav__logo">EmpowerHer</a>

      <div class="nav__menu nav-center" id="nav-menu">
        <ul class="nav__list">
          <li class="nav__item dropdown dropdown-toggle"><a href="#" class="nav__link active-link">Platform</a>
            <div class="dropdown-content">
              <div class="dropdown-column">
                <h4>PAGES</h4>
                <a href="/About">About Us</a>
                <a href="/Contact">Contact Us</a>
                <a href="/Privacy-Policy">Privacy Policy</a>
                <a href="/terms-and-conditions">Terms & Conditions</a>
              </div>
            </div>
          </li>
          <li class="nav__item dropdown dropdown-toggle"><a href="#" class="nav__link">Partners</a>
            <div class="dropdown-content">
              <div class="dropdown-column">
                <h4>PARTNERS</h4>
                <a href="/BecomePartner">Become A Partner</a>
                <a href="/PartnerPrograms">Partner Our Programs</a>
              </div>
            </div>
          </li>
          <li class="nav__item dropdown dropdown-toggle">
            <a href="#" class="nav__link">Resources</a>
            <div class="dropdown-content">
              <div class="dropdown-column">
                <h4>RESOURCES</h4>
                <a href="/Blog">Blog</a>
                <a href="/Events">Events</a>
                <a href="#">Demo</a>
                <a href="#">Products</a>
              </div>
              <div class="dropdown-column">
                <h4>Community</h4>
                <a href="#">Join Community</a>
                <a href="#">Contribute</a>
                <a href="/Forum">Forum</a>
                <a href="#">Chat</a>
              </div>
            </div>
          </li>
          <li class="nav__item"><a href="#" class="nav__link position-relative"><i class="bi bi-bell-fill"></i>
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-success">
              <!-- number of notifications goes here -->
              <span class="visually-hidden">unread messages</span>
            </span>
            Notifications
          </a>
        </li>
        <!--li class="nav__item"><a href="/Login" class="nav__link">Login</a></li-->
        <li class="nav__item nav_right dropdown dropdown-toggle"><a href="/Account" class="nav__link">Account</a>
          <div class="dropdown-content">
            <div class="dropdown-column">
              <h4>ACCOUNT</h4>
              <a href="/Account">My Profile</a>
              <a href="#">Chat An Expert</a>
              <a href="#">Settings</a>
              <a href="#">Logout</a>
            </div>
          </div>
        </li>
        <li><i class='bx bx-moon change-theme' id="theme-button"></i></li>
      </ul>
    </div>

    <div class="nav__toggle" id="nav-toggle">
      <i class='bx bx-menu'></i>
    </div>
    </nav>
  </header>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
