<template>

	<main class="l-main">

		<!---- Login ---->
		
		<section class="menu section bd-container">
			<form class="row g-3 needs-validation" @submit.prevent="submit" id="sign-up" novalidate>
			<h1 class="font-semibold text-4xl mb-4">Sign up</h1>
			<p class="text-base mb-4 leading-5">
			  Have an account?
			  <router-link :to="{ name: 'login' }" class="font-semibold text-primary">Login</router-link>
			</p>
			<div class="col-md-4">
			<label for="validationCustom01" class="form-label">First name</label>
			<input v-model="formData.first_name" type="text" class="form-control" id="validationCustom01 firstName" required>
			<div class="valid-feedback">
			Looks good!
			</div>
			</div>
			<div class="col-md-4">
			<label for="validationCustom02" class="form-label">Last name</label>
			<input v-model="formData.last_name" type="text" class="form-control" id="validationCustom02 lastName" required>
			<div class="valid-feedback">
			Looks good!
			</div>
			</div>
			<div class="col-md-4">
			<label for="validationCustomUsername" class="form-label">Username</label>
			<div class="input-group has-validation">
			<span class="input-group-text" id="inputGroupPrepend">@</span>
			<input v-model="formData.user_name" type="text" class="form-control" id="validationCustomUsername userName" aria-describedby="inputGroupPrepend" required>
			<div class="invalid-feedback">
			Please choose a username.
			</div>
			</div>
			</div>
			<div class="col-md-6">
			<label for="validationCustom03" class="form-label">Phone Number</label>
			<input v-model="formData.phone_number" type="tel" class="form-control" id="phoneNumber" required>
			<div class="invalid-feedback">
			Please provide a valid number.
			</div>
			</div>
			<div class="col-md-3">
			<label for="validationCustom04" class="form-label">Gender</label>
			<select v-model="formData.gender" class="form-select" id="validationCustom04 gender" required>
			<option selected disabled value="">Choose...</option>
			<option value="male">Male</option>
			<option value="female">Female</option>
			<option value="other">Other</option>
			</select>
			<div class="invalid-feedback">
			Please select a valid state.
			</div>
			</div>
			<div class="col-md-3">
			<label for="validationCustom05" class="form-label">Your Age</label>
			<input v-model="formData.age" type="number" class="form-control" id="validationCustom05 age" required>
			<div class="invalid-feedback">
			Your age does't seem correct.
			</div>
			</div>
			<div class="col-12">
			<div class="row mb-3">
			    <label for="phoneNumber" class="col-sm-2 col-form-label">Email</label>
			    <div class="col-sm-10">
					<input v-model="formData.user_email" type="email" class="form-control" id="validationCustom03 email" required>
					<div class="invalid-feedback">
					Please provide a valid email.
					</div>
			    </div>
			</div>
			<div class="row mb-3">
			    <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
			    <div class="col-sm-10">
					<input v-model="formData.user_password" type="password" class="form-control" id="inputPassword3 password" required>
					<div class="invalid-feedback">
					Please provide a strong password.
					</div>
			    </div>
			</div>
			<div class="row mb-3">
				<label for="inputPassword3" class="col-sm-2 col-form-label">Confirm Password</label>
			    <div class="col-sm-10">
					<input v-model="formData.repeatPassword" type="password" class="form-control" id="inputPassword3 repeatPassword" required>
					<div class="invalid-feedback">
					Password miss match!
					</div>
			    </div>
			</div>
			</div>
			<div class="col-12">
			<div class="form-check">
			<input class="form-check-input" type="checkbox" value="" id="invalidCheck" required>
			<label class="form-check-label" for="invalidCheck">
			Agree to <a href="/TermsAndConditions">Terms and Conditions</a>
			</label>
			<div class="invalid-feedback">
			You must agree before submitting.
			</div>
			</div>
			</div>
			<div class="col-12">
			<button class="w-full btn btn-primary" type="submit">Submit form</button>
			</div>
			</form>
		</section>
		<!---- Login End ---->
	</main>
	
</template>


<script>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api';

const passwordRules = [
  (v) => !!v || 'Password field is required',
  (v) => (v && v.length >= 8) || 'Password must be at least 8 characters long',
  (v) => (v && /[A-Za-z]/.test(v)) || 'Password must contain at least one letter',
  (v) => (v && /\d/.test(v)) || 'Password must contain at least one number',
  (v) => (v && /[!@#$%^&*(),.?":{}|<>]/.test(v)) || 'Password must contain at least one special character',
];

export default {
  setup() {
    const router = useRouter();

    const formData = reactive({
      user_name: '',
      first_name: '',
      last_name: '',
      age: '',
      phone_number: '',
      user_email: '',
      user_password: '',
      repeatPassword: '',
      gender: '',
    });

    const submit = async () => {
      try {
        if (formData.gender === '') {
          alert('Please select your gender.');
          return;
        }

        if (formData.user_password !== formData.repeatPassword) {
          alert('Passwords do not match.');
          return;
        }

        if (formData.gender.toLowerCase() === 'male') {
          alert('Signup not allowed: An error occured on form submission.');
          return;
        }

        console.log('Form Data:', formData);

        const response = await api.createUser({
          user_name: formData.user_name,
          first_name: formData.first_name,
          last_name: formData.last_name,
          age: formData.age,
          phone_number: formData.phone_number,
          user_email: formData.user_email,
          user_password: formData.user_password,
        });

        console.log('Response:', response);

        if (response.status === 200 && response.data) {
          alert('You\'ve successfully signed up');

          router.push({ name: 'login' });
        } else {
          throw new Error('Signup failed');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Signup failed. Please check your details and try again.');
      }
    };

    return {
      formData,
      passwordRules,
      submit,
    };
  },
};
</script>