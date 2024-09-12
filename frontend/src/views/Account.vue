<template>
	<div class="container section">
		<div class="row">
			<div class="col-md-3">
				<div class="leftbar">
					<div class="user-details">
						<img src="../assets/logo.svg" class="img-fluid rounded-circle" alt="Profile Image">
						<h4>{{ firstName }} {{ lastName }}</h4>
						<p>{{ userEmail }}</p>
					</div>
					<div class="common-features">
						<ul>
							<li><a href="#editProfile">My Posts</a></li>
							<li><a href="#manageAccount">Manage </a></li>
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-9" id="editProfile">
				<div class="main-section">
					<h2>Edit Profile</h2>
					<p>Keep your personal details private
						. Information you add here is visible to anyone who can view your profile.
					</p>
					<div class="edit-profile">
						<form>
							<div class="row g-3">
								<div class="col">
									<label for="firstName" class="form-label">First Name</label>
									<input type="text" class="form-control" aria-label="First name">
								</div>
								<div class="col">
									<label for="lastName" class="form-label">Last Name</label>
									<input type="text" class="form-control" aria-label="Last name">
								</div>
							</div>
							<div class="mb-3">
							<label for="exampleFormControlTextarea1" class="form-label">About</label>
							<textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
							</div>
							<div class="mb-3">
								<label for="specificSizeSelect">Pronouns</label>
								<select class="form-select" id="specificSizeSelect">
								<option selected>Choose...</option>
								<option value="ey/em">ey/em</option>
								<option value="he/him">he/him</option>
								<option value="ne/nem">ne/nem</option>
								<option value="she/her">she/her</option>
								<option value="they/them">they/them</option>
								<option value="ve/ver">ve/ver</option>
								<option value="xe/xem">xe/xem</option>
								<option value="xie/xem">xie/xem</option>
								<option value="ze/zir">ze/zir</option>
								</select>
								<p>
									Choose up to 2 sets of pronouns to appear on your 
									profile so others know how to refer to you
									. You can edit or remove these any time.
								</p>
							</div>
							<div class="input-group flex-nowrap">
								<span class="input-group-text" id="addon-wrapping">@</span>
								<input type="text" class="form-control" placeholder="Username" 
								aria-label="Username" aria-describedby="addon-wrapping">
							</div>
							<button type="button" class="btn btn-success">
								Save
							</button>
						</form>
					</div>
				</div>
			</div>

			<div class="col-md-9" id="manageAccount">
				<div class="main-section">
					<h2>
						Manage your account
					</h2>
					<p>
						Make changes to your personal information or account type.
					</p>
					<div class="edit-profile">
						<form>
							<div class="row mb-3">
								<label for="inputPassword3" class="col-sm-2 col-form-label">Current Password</label>
								<div class="col-sm-10">
								<input type="password" class="form-control" id="inputPassword3">
								</div>
							</div>
							<div class="row g-3">
								<div class="col">
									<input type="password" placeholder="New Password" class="form-control" id="newPassword">
								</div>
								<div class="col">
									<button type="button" class="btn btn-success" @click="changePassword">
										Change
									</button>
								</div>
							</div>
						</form>
						<h4>
							Profile visibility
						</h4>
						<div class="row mb-3">
							<p>
								Manage how your profile can be viewed on and off of Pinterest.
							</p>
							<div class="form-check form-switch">
							<input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
							<label class="form-check-label" for="flexSwitchCheckDefault"><strong>Private profile</strong></label>
							<p>When your profile is private only the 
								people you approve can see your profile and all your comments 
								and posts would appear as Anonymous.</p>
							</div>
						</div>
						<h4>
							Account deletion
						</h4>
						<div class="row mb-3">
							<p>
								You can delete your account at any time. 
								When you delete your account, your profile, photos, 
								videos, comments, likes, and followers will be permanently removed.
							</p>
							<div class="col-sm-10">
								<button type="button" class="btn btn-danger">
									Delete Account
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>

		</div>
	</div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '../api';

export default {
	setup() {
		const userEmail = ref('');
		const firstName = ref('');
		const lastName = ref('');
		const userImage = ref('');
		const currentPassword = ref('');
		const newPassword = ref('');
		const confirmNewPassword = ref('');

		const fetchUserDetails = async () => {
			try {
				const response = await api.getUserDetails();
				userEmail.value = response.data.user_email;
				firstName.value = response.data.first_name;
				lastName.value = response.data.last_name;
				userImage.value = response.data.user_image;
			} catch (error) {
				console.error("Failed to fetch user details:", error);
			}
		};

		const updatePassword = async (email, currentPassword, newPassword) => {
			try {
				const passwordData = {
					old_password: currentPassword,
					new_password: newPassword
				};
				await api.updatePassword(email, passwordData);
				alert('Password updated successfully');
			} catch (error) {
				console.error("Failed to update password:", error);
				alert('Failed to update password');
			}
		};

		const changePassword = () => {
			if (newPassword.value !== confirmNewPassword.value) {
				alert('New password and confirm password do not match');
				return;
			}

			updatePassword(userEmail.value, currentPassword.value, newPassword.value);
		};

		/**const handleImageUpload = (event) => {
			const file = event.target.files[0];
		};

		const uploadImage = async () => {
			// this is not implemented in the API yet
		};**/

		onMounted(() => {
			fetchUserDetails();
		});

		return {
			userEmail,
			firstName,
			lastName,
			userImage,
			currentPassword,
			newPassword,
			confirmNewPassword,
			changePassword
			/**
			 * handleImageUpload,
			 * uploadImage
			*/
		};
	},
}
</script>