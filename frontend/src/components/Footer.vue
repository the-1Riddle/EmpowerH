<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <!------------ FOOTER ------------>
  <footer class="footer section bd-container">

    <!-- footer -->

    <div class="footer-area">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6">
            <div class="footer-box about-widget">
              <h2 class="widget-title">Why us</h2>
              <p>Join our community today and become part of a supportive network of women who empower and uplift each other. Together, let's create a brighter future for all.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="footer-box get-in-touch">
              <h2 class="widget-title">Get in Touch</h2>
              <ul>
                <li>34/8, East Karapul, Rabango, SA.</li>
                <li>support@empowerher.com</li>
                <li>+00 111 222 3333</li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="footer-box pages">
              <h2 class="widget-title">Pages</h2>
              <ul>
                <li><a href="/" class="footer__link">Home</a></li>
                <li><a href="about" class="footer__link">About</a></li>
                <li><a href="contact" class="footer__link">Contact</a></li>
                <li><a href="privacy-policy" class="footer__link">Privacy Policy</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <div class="footer-box subscribe">
              <h2 class="widget-title">Subscribe</h2>
              <p>Subscribe to our mailing list to get the latest updates.</p>
              <br>
              <form action="/home">
                <div class="input-group mb-3">
                  <input type="email" class="form-control" placeholder="Email" aria-label="Recipient's username" aria-describedby="basic-addon2" required>
                  <span class="input-group-text" id="basic-addon2">Subscribe</span>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- end footer -->

    <!-- copyright -->
    <div class="copyright">
      <div class="container">
        <div class="row footer__copy">
          <div class="col-lg-6 col-md-12">
            <p>Copyrights &copy; 2024 - <a href="https://empowerherr.tech/">EmpowerHer</a>,  All Rights Reserved.</p>
          </div>
          <div class="col-lg-6 text-right col-md-12">
            <div class="social-icons">
              <ul>
                <li><a href="https://twitter.com/empowerHerr" target="_blank"><i class="bx bxl-twitter"></i></a></li>
                <li><a href="https://instagram.com/empowerHerr" target="_blank"><i class="bx bxl-instagram"></i></a></li>
                <li><a href="https://linkedin.com/in/empowerHerr" target="_blank"><i class="bx bxl-linkedin"></i></a></li>
                <li><a href="https://dribble.com/empowerHerr" target="_blank"><i class="bx bxl-dribbble"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- end copyright -->
  </footer>
</template>

<style scoped>

</style>
