<template>

	<main class="l-main">

		<!---- Login ---->
		
		<section class="menu section bd-container" id="Gender">
			<form @submit.prevent="submit" id="sign-up">
			  <h1 class="font-semibold text-4xl mb-4">Sign up</h1>
			  <p class="text-base mb-4 leading-5">
			    Have an account?
			    <router-link :to="{ name: 'login' }" class="font-semibold text-primary">Login</router-link>
			  </p>
			  <div class="form-row">
			    <div class="form-group col-md-6">
			      <label for="firstName">First Name</label>
			      <input v-model="formData.first_name" type="text" class="form-control" id="firstName" required>
			    </div>
			    <div class="form-group col-md-6">
			      <label for="lastName">Last Name</label>
			      <input v-model="formData.last_name" type="text" class="form-control" id="lastName" required>
			    </div>
			  </div>
			  <div class="form-row">
			    <div class="form-group col-md-6">
			      <label for="userName">Username</label>
			      <div class="input-group">
			        <div class="input-group-prepend">
			          <span class="input-group-text" id="validationTooltipUsernamePrepend">@</span>
			        </div>
			        <input v-model="formData.user_name" type="text" class="form-control" id="userName" placeholder="Username" required>
			      </div>
			    </div>
			    <div class="form-group col-md-4">
			      <label for="age">Your Age</label>
			      <input v-model="formData.age" type="number" class="form-control" id="age" required>
			    </div>
			    <div class="form-group col-md-2">
			      <label for="gender">Gender</label>
			      <select v-model="formData.gender" id="gender" class="form-control" required>
			        <option value="" disabled>Gender</option>
			        <option value="male">Male</option>
			        <option value="female">Female</option>
			        <option value="other">Other</option>
			      </select>
			    </div>
			  </div>
			  <div class="form-row">
			    <div class="form-group col-md-6">
			      <label for="phoneNumber">Phone Number</label>
			      <input v-model="formData.phone_number" type="tel" class="form-control" id="phoneNumber" placeholder="Phone number" required>
			    </div>
			    <div class="form-group col-md-6">
			      <label for="email">Email</label>
			      <input v-model="formData.user_email" type="email" class="form-control" id="email" placeholder="Email" required>
			    </div>
			  </div>
			  <div class="form-group">
			    <label for="validationTooltip03" class="form-label">Password</label>
			    <input v-model="formData.user_password" type="password" class="form-control" id="password" placeholder="Password" required>
			    <ul class="password-rules">
			      <li v-for="(rule, index) in passwordRules" :key="index">
			        <span :class="{ 'text-success': rule(formData.user_password) === true, 'text-danger': rule(formData.user_password) !== true }">
			          {{ rule(formData.user_password) !== true ? rule(formData.user_password) : '✔' }}
			        </span>
			      </li>
			    </ul>
			  </div>
			  <div class="form-group">
			    <label for="repeatPassword">Confirm Password</label>
			    <input v-model="formData.repeatPassword" type="password" class="form-control" id="repeatPassword" placeholder="Password" required>
			  </div>
			  <button type="submit" id="signup-btn" class="w-full btn btn-primary">Sign Up</button>
			</form>
		</section>
		<!---- Login End ---->
	</main>

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