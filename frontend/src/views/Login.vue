<template>

	<body style="background-color: #E9E9E9;">
	    <div class="circles h-100 w-100 d-none d-sm-none d-md-block">
	        <span class="circle1"></span>
	        <span class="circle2"></span>
	        <span class="circle3"></span>
	        <span class="circle4"></span>
	    </div>
	    <div
	        class="mx-auto col-11 col-sm-10 col-md-6 col-lg-7 col-xl-6 position-relative p-0 h-100 d-flex align-items-center">

	        <div class="row auth h-auto w-100 m-0 rounded bg-white">
	            <div
	                class="auth-info bg-primary col-5 d-none d-sm-none d-md-none d-lg-block d-flex flex-0 flex-column align-items-center justify-content-start p-3">
	                <a href="/" class="text-decoration-none">
	                    <img class="w-50 ms-5 mt-5 position-relative" src="../assets/logo.svg" alt="">
	                </a>
	                <h6 class="text-white mt-5 pt-5 fw-light text-center"><span class="text-white fw-bold fs-5">Skill
	                        Sphere</span>
	                    connects skilled individuals with businesses and entrepreneurs who need their expertise, fostering a
	                    community of collaboration and growth
	                </h6>

	            </div>
	            <div class="col bg-white p-4">
	                <div class="row mt-3 w-100">
	                    <h3 class=" text-primary fw-bold mt-0 mt-md-1">Sign In</h3>
	                    <form class="w-100 pe-0 mb-5" action="">
	                        <div class="form-group w-100 mt-4">
	                            <div class="input mb-1 mb-md-2 mb-sm-1">
	                                <label for="email" class="d-block">Email Address</label>
	                                <input class="w-100 rounded mt-2" placeholder="Email Address" type="text" required>
	                            </div>
	                            <div class="input mb-2">
	                                <label for="pswd" class="d-block">Password</label>
	                                <input class="w-100 rounded mt-2" placeholder="Password" type="password" required>
	                            </div>
	                            <div class="input mb-2">
	                                <input class="btn btn-primary w-100 rounded mt-2" type="submit" value="Login" required>
	                            </div>
	                            <a class="forget-link fs-8" href="/">Forget password?</a>

	                            <p class="text-center mt-3 mt-md-5">New user?
	                                <a href="/signup" class="fw-bold text-primary text-decoration-none">Create
	                                    Account</a>
	                            </p>
	                        </div>

	                    </form>
	                </div>
	            </div>
	        </div>
	    </div>
	</body>

</template>


<script>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api';

export default {
  setup() {
    const router = useRouter();
    
    const formData = reactive({
      username: '',
      password: '',
    });

    const errors = reactive({
      username: '',
      password: '',
    });

    const submit = async () => {
      try {
        console.log("Submitting login data:", formData);
        const response = await api.loginUser({
          username: formData.username,
          password: formData.password,
        });
        console.log("Login response:", response);
        if (response.data) {
          alert('You\'ve successfully logged in');
          localStorage.setItem('user-info', response.data.access_token);
          router.push({ name: 'home' });
        }
      } catch (error) {
        console.error("Login error:", error);
        alert('Login failed. Please check your credentials and try again.');
      }
    };

    return {
      formData,
      errors,
      submit,
    };
  },
  mounted() {
    let user = localStorage.getItem('user-info');
    if (user) {
      this.$router.push({ name: 'home' });
    }
  },
};
</script>

<style scoped>
	* {
	    padding: 0;
	    margin: 0;
	    box-sizing: border-box;
	    font-family: 'Inter', sans-serif;
	}


	html,
	body {
	    width: 100%;
	    height: 100%;
	    margin: 0;
	    padding: 0;
	    position: relative;
	    overflow-x: hidden;
	}

	body::-webkit-scrollbar {
	    display: none;
	}

	.lg-header{
	    z-index: 1000 !important;
	    padding-left: 120px !important;
	    background: linear-gradient(to left, rgb(199, 15, 24), rgb(90, 0, 5));
	}
	.top-dp{
	    display: inline-block;
	    text-align: center;
	    cursor: pointer;
	    padding: 5px 8px 8px;
	    text-decoration: none;
	    color: #ffffff;
	    border: 2px solid #ffffff;;
	    width: 40px;
	    height: 40px;
	    border-radius: 50%;
	}
	.company-init{
	    font-size: 3.2rem;
	    display: flex;
	    align-items: center;
	    justify-content: center;
	    cursor: pointer;
	    text-decoration: none;
	    color: #000000;
	    border: 2px solid #C70F19;;
	    width: 100px;
	    height: 100px;
	    border-radius: 50%;
	}

	.content{    
	    position: relative;
	    display: flex;
	    flex-flow: column wrap;
	}

	@media screen and (min-width: 768px) {
	    .content{
	        padding-left: 70px;
	    }
	}


	/* ===============================================GLOBAL=============================================== */
	.bg-primary {
	    background-color: #C70F19 !important;
	}

	.text-primary {
	    color: #C70F19 !important;
	}

	.bg-rounded {
	    border-radius: 25px;
	}

	.bg-secondary {
	    background-color: #FFF5F6 !important;
	}

	/* =================================AUTHENTICAYIONS================================ */
	.circles {
	    position: absolute;
	}

	.circles span {
	    display: inline-block;
	    position: absolute;
	}

	.circles span:first-child {
	    width: 100px;
	    height: 100px;
	    background: rgb(255, 255, 255);
	    border-radius: 50%;
	    left: 22%;
	    top: 10%;
	}

	.circles span:first-child::after {
	    content: "";
	    position: absolute;
	    width: 50px;
	    height: 50px;
	    background: #C70F19;
	    border-radius: 50%;
	    left: 950px;
	    top: 100%;
	}

	.circles span:nth-child(2) {
	    width: 100px;
	    height: 100px;
	    left: 18%;
	    bottom: 16%;
	    border: 10px solid #C70F19;
	    border-radius: 50%;
	}

	.circles span:nth-child(3) {
	    width: 70px;
	    height: 70px;
	    left: 22%;
	    bottom: 60px;
	    border: 5px solid #ffffff;
	    border-radius: 50%;
	}

	.circles span:nth-child(4) {
	    width: 70px;
	    height: 70px;
	    left: 80%;
	    top: 30%;
	    border: 5px solid #ffffff;
	    border-radius: 50%;
	}

	.circles span:nth-child(4)::before {
	    content: "";
	    position: absolute;
	    top: -200px;
	    left: -250px;
	    border: 15px solid #ffffff;
	    border-radius: 50%;
	    width: 250px;
	    height: 250px;
	}



	.auth {
	    overflow: hidden;
	    box-shadow: 1px 1px 15px rgba(128, 128, 128, 0.24);
	    height: 80vh !important;
	}

	.auth::-webkit-scrollbar {
	    display: none;
	}

	.auth-info {
	    position: relative;
	    overflow: hidden;
	}

	.auth-info img {
	    z-index: 110;
	}

	.auth-info::after {
	    content: "";
	    display: inline-block;
	    width: 500px;
	    height: 500px;
	    position: absolute;
	    /* top: 0; */
	    left: -40px;
	    bottom: 400px;
	    background-color: #ffffff1a;
	    border-radius: 50%;
	}

	.form-fieldset {
	    height: 100%;
	    overflow: hidden;
	    overflow-y: scroll;
	}

	.form-fieldset::-webkit-scrollbar {
	    display: none;
	}

	.reg-bar {
	    bottom: -25px;
	    background-color: #fff;
	    padding: 10px;
	}

	.form-group {
	    gap: 8px;
	}

	.form-group input,
	.form-group select {
	    border: none;
	    border: 1px solid #181818;
	    padding: 7px;
	    font-size: 14px;
	    color: #181818;
	    background-color: #FFF5F6;
	    text-indent: 5px;
	    outline: none;
	}

	.otp-input {
	    gap: 15px;
	}

	input[type="number"] {
	    /* padding-left: 12px; */
	    min-width: 42px;
	    -moz-appearance: textfield;
	    -webkit-appearance: textfield;
	    appearance: textfield;
	}

	input[type=number]::-webkit-inner-spin-button,
	input[type=number]::-webkit-outer-spin-button {
	    -webkit-appearance: none;
	}

	.comp-decribe {
	    border: none;
	    outline: none;
	    border: solid 1px #1C1B1F;
	    resize: none;
	}

	.comp-decribe:hover {
	    outline: none;
	    border: none;
	    border: solid 1px #1C1B1F;
	}

	select option {
	    /* color: red; */
	    background-color: #FFF5F6 !important;
	    color: #C70F19 !important;
	}

	.form-group input:focus {
	    outline: none;
	    /* border-color: #ffffff; */
	}

	.form-control:focus, .form-select:focus{
	    border-color: #C70F19;
	    box-shadow: 0 0 0 0.25rem rgba(199, 15, 25,.25);
	}
	.form-select option{
	    padding: 5.5px 4px;
	}
	.form-select option:checked, .form-select option:hover, .form-select option:checked:focus{
	    background-color: #C70F19 !important;
	    color: #ffffff !important;
	}

	.type {
	    top: -10%;
	    margin-top: -20px;
	    background-color: #fff;
	}

	.btn-primary {
	    background-color: #C70F19 !important;
	    color: white !important;
	    border-color: #C70F19 !important;

	    --bs-btn-color: #fff !important;
	    --bs-btn-bg: #C70F19 !important;
	    --bs-btn-border-color: #C70F19 !important;
	    --bs-btn-hover-color: #fff !important;
	    --bs-btn-hover-bg: #C70F19 !important;
	    --bs-btn-hover-border-color: #C70F19 !important;
	    --bs-btn-focus-shadow-rgb: 49, 132, 253;
	    --bs-btn-active-color: #fff;
	    --bs-btn-active-bg: #d60f19 !important;
	    --bs-btn-active-border-color: #C70F19 !important;
	    --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
	    --bs-btn-disabled-color: #fff !important;
	    --bs-btn-disabled-bg: #C70F19 !important;
	    --bs-btn-disabled-border-color: #C70F19 !important;
	}

	.btn-primary:hover {
	    background-color: transparent !important;
	    color: #C70F19 !important;
	}

	.forget-link {
	    color: #181818;
	    text-decoration: none;
	}

	.forget-link:hover {
	    text-decoration: underline;
	    color: #181818;
	}



	/* ORGANIZATION APPLICATION */
	.org-card {
	    color: #181818;
	    text-decoration: none;
	}

	.org-card:hover {
	    color: #C70F19;
	}

	.org-demand {
	    color: #785900;
	    flex-wrap: wrap;
	}

	.org-demand small {
	    display: inline-block;
	}

	.org-arr svg {
	    font-size: 200px;
	}

	.org-card:hover .org-arr>svg>path {
	    fill: #C70F19;
	}

	.company-img {
	    object-fit: cover;
	    width: clamp(100px, 50px, 200px);
	    display: block;
	    border: 3px solid #C70F19;
	    box-shadow: -3px 3px 5px rgba(0, 0, 0, 0.199);
	}

	.btn-outline-primary {
	    border-color: #C70F19;
	    color: #C70F19;
	    --bs-btn-color: #C70F19;
	    --bs-btn-border-color: #C70F19;
	    --bs-btn-hover-color: #fff;
	    --bs-btn-hover-bg: #C70F19;
	    --bs-btn-hover-border-color: #C70F19;
	    --bs-btn-focus-shadow-rgb: 13, 110, 253;
	    --bs-btn-active-color: #fff;
	    --bs-btn-active-bg: #C70F19;
	    --bs-btn-active-border-color: #C70F19;
	    --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
	    --bs-btn-disabled-color: #C70F19;
	    --bs-btn-disabled-bg: transparent;
	    --bs-btn-disabled-border-color: #C70F19;
	    --bs-gradient: none;

	}

	.btn-outline-primary:hover {
	    background-color: #C70F19;
	    color: white;
	    border-color: #C70F19;
	}


	.btn-saved {
	    position: relative;
	    background-color: #FFEBEC;
	    color: #C70F19;
	}

	.btn-saved::after {
	    content: ' ';
	    width: 10px;
	    height: 10px;
	    border-radius: 50%;
	    background-color: #C70F19;
	    display: block;
	    position: absolute;
	    top: 10%;
	    right: 2%;
	}

	/* Modal Card */
	.mod-card {
	    top: 0;
	    left: 0;
	    height: 100vh !important;
	    background-color: #1818184d;
	    -webkit-backdrop-filter: blur(5px);
	    backdrop-filter: blur(5px);
	}

	.mod-card .card {
	    background: #FFF5F6;
	}

	@keyframes herobg {
	    0% {
	        opacity: 1;
	        background: linear-gradient(to left, #00000850, #C70F1950), url(../images/hero.png) no-repeat;
	        background-size: cover;
	    }

	    25% {
	        opacity: 1;
	        background: linear-gradient(to top, #00000830, #C70F1925), url(../images/hero.png) no-repeat;
	        background-size: cover;
	    }

	    50% {
	        opacity: 1;
	        background: linear-gradient(to right, #00000850, #C70F1930), url(../images/hero.png) no-repeat;
	        background-size: cover;
	    }

	    100% {
	        opacity: 1;
	        background: linear-gradient(to bottom, #00000850, #C70F1950), url(../images/hero.png) no-repeat;
	        background-size: cover;
	    }
	}


	/* REGISTRATION ENTRY */

	.company-logo {
	    width: 120px;
	    height: 120px;
	    margin: 0 auto;
	}

	.company-logo img {
	    display: block;
	    width: 100%;
	    border: solid 3px #C70F19;
	    transition: .2s;
	}

	.company-logo img:hover {
	    opacity: .6;
	    transition: .3s;
	}
</style>