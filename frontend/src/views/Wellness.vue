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
                <li class="nav-item nav-left"><a href="#Wellness" class="nav__link">Wellness</a></li>
                <li class="nav-item nav-center"><a href="/sexual-awareness" class="nav__link">Sexual Awareness</a></li>
                <li class="nav-item nav-right"><a href="/gender-violence" class="nav__link">Gender Violence</a></li>
            </ul>
            <hr>
        </section>

        <section class="section bd-container">
            <div class="container">
                <div class="left_block">
                    <p>Articles About</p>
                    <h2 class="section-title" style="text-align: left;">Wellness</h2>
                </div>
                <div class="separator"></div>
                <div class="right_block">
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.</p>
                </div>
            </div>
        </section>
        
        <!---- Popular Post ---->
        <section class="about section bd-container" id="about">
            <div class="about__container  bd-grid">
                <div class="about__data">
                    <span class="section-subtitle about__initial">Popular Post</span>
                    <h2 class="section-title about__initial">Lorem ipsum dolor <br> sit amet</h2>
                    <p class="about__description">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                    <a href="#" class="button">Explore history</a>
                </div>

                <img src="../assets/img/about.jpg" alt="" class="about__img">
            </div>
        </section>
        <!---- Popular Post End ---->

        <!-- Contents from the previouse version -->
        <div class="wellness-hub">
          <header>
            <h1>Women's Wellness Hub</h1>
            <p>Promoting physical and mental health</p>
          </header>

          <div class="intro">
            <h2>🌟Welcome to Our Health Hub!🌟</h2>
            <p>
              Life can get hectic, right? Whether you’re juggling classes, work, or family responsibilities, taking care of yourself often takes a backseat. But guess what? Your well-being matters, and it’s time to prioritize it!
            </p>
            <p><b>Beyond the Basics:</b></p>
            <p>
              Sure, we all know about physical health, but there’s a whole world of wellness waiting for you. From mental well-being to self-care rituals, we’ve got you covered. So, buckle up—this journey is about to get exciting!
              Explore, learn, and take charge of your health. No regrets—promise! 💪 
            </p>
          </div>

          <main>
            <section id="mental-health">
              <h2>Mental Health Check-Ins</h2>
              <p>Regularly assess your mental well-being:</p>
              <ul>
                <li>Check for signs of anxiety, depression, or stress.</li>
                <li>Seek professional help if needed.</li>
              </ul>
            </section>

            <section class="health-checks">
              <h2>Health Checks</h2>
              <ul>
                <li><a href="#" @click.prevent="showModal('fertility')">Fertility checks</a></li>
                <li><a href="#" @click.prevent="showModal('smear')">Pap smear tests</a></li>
                <li><a href="#" @click.prevent="showModal('cancer')">Breast cancer screening</a></li>
                <li><a href="#" @click.prevent="showModal('sti')">STI testing</a></li>
                <li><a href="#" @click.prevent="showModal('blood')">Blood pressure checks</a></li>
                <li><a href="#" @click.prevent="showModal('chole')">Cholesterol checks</a></li>
              </ul>
            </section>

            <section id="physical-health">
              <h2>Physical Health Tips</h2>
              <p>Take care of your body:</p>
              <ul>
                <li>Stay active: Engage in regular exercise (walking, yoga, etc.).</li>
                <li>Eat well-balanced meals with plenty of fruits and vegetables.</li>
                <li>Get enough restful sleep each night.</li>
                <li>Stay hydrated.</li>
              </ul>
            </section>

            <section id="water-intake">
              <h2>Water Intake</h2>
              <p>Proper hydration is essential for overall health. Here's what you need to know:</p>
              <ul>
                <li><strong>Recommended Daily Intake:</strong> Aim for about 8 cups (64 ounces) of water per day.</li>
                <li><strong>Adjust Based on Needs:</strong> Adjust your water intake based on activity level, climate, and individual requirements.</li>
                <li><strong>Hydration Tips:</strong>
                  <ul>
                    <li>Carry a reusable water bottle with you.</li>
                    <li>Set reminders to drink water throughout the day.</li>
                    <li>Incorporate hydrating foods like fruits and vegetables into your diet.</li>
                  </ul>
                </li>
              </ul>
            </section>

            <section id="self-care">
              <h2>Self-Care Routines</h2>
              <p>Prioritize self-care:</p>
              <ul>
                <li>Practice skincare rituals (cleansing, moisturizing).</li>
                <li>Set aside time for relaxation (meditation, deep breathing).</li>
                <li>Engage in hobbies you enjoy (reading, painting, gardening).</li>
              </ul>
            </section>
          </main>

          <div v-if="modalContent" class="popup" :id="modalContent.id">
              <div class="mt-150">
                  <div class="container">
                      <h1 style="text-align:center">{{ modalContent.title }}</h1>
                      <p><b>Definition:</b> {{ modalContent.definition }}</p>
                      <p v-if="modalContent.types"><b>Types of tests:</b></p>
                      <ul v-if="modalContent.types">
                      <li v-for="type in modalContent.types" :key="type">{{ type }}</li>
                      </ul>
                      <p><b>What to expect:</b> {{ modalContent.expect }}</p>
                      <p><b>Why it's important:</b> {{ modalContent.importance }}</p>
                  </div>
              </div>
            <button class="close" @click="closeModal">Close</button>
          </div>
        </div>
        <!-- Contents from the previouse version End -->

        <!---- Wellness ----->
        <section class="menu section bd-container" id="Wellness">
            <!-- Blog Posts goes here -->
        </section>
        <!--- Wellness End --->
    </main>
</template>


<script>
export default {
  data() {
    return {
      modalContent: null,
    };
  },
  methods: {
    showModal(type) {
      const modalData = {
        fertility: {
          id: "fertility",
          title: "Fertility Checks",
          definition: "Fertility checks encompass various medical evaluations to assess an individual's reproductive health and ability to conceive.",
          types: ["Ovulation testing (for women)", "Hormone level testing (for both men and women)"],
          expect: "Expect a comprehensive evaluation by a healthcare provider, including a pelvic exam, blood tests to assess hormone levels, and ovulation monitoring for women.",
          importance: "Identifying potential fertility issues early can provide crucial guidance and treatment options, increasing the chances of successful conception.",
        },
        smear: {
          id: "smear",
          title: "Pap Smear Tests",
          definition: "Pap smear tests are screening procedures used to detect precancerous or cancerous processes in the cervix.",
          expect: "During the test, a healthcare provider collects cells from the cervix to examine under a microscope for any abnormalities.",
          importance: "Early detection through Pap smears significantly increases the chances of successful treatment of cervical cancer, highlighting their role in preventive healthcare.",
        },
        cancer: {
          id: "cancer",
          title: "Breast Cancer Screening",
          definition: "Breast cancer screening involves tests and exams to detect breast cancer at an early, more treatable stage.",
          types: ["Mammogram (X-ray imaging)", "Clinical breast exam (physical exam by a healthcare provider)"],
          expect: "Expect a mammogram, which involves X-ray imaging of the breasts, or a clinical breast exam where a healthcare provider physically examines the breasts for abnormalities.",
          importance: "Early detection of breast cancer through regular screenings can significantly improve survival rates and treatment outcomes.",
        },
        sti: {
          id: "sti",
          title: "STI Checks",
          definition: "STI checks involve various tests to diagnose sexually transmitted infections early.",
          types: ["Blood tests", "Urine tests", "Swab tests (for genital, oral, or rectal infections)"],
          expect: "A healthcare provider will collect blood, urine, or swab samples from the affected area to test for STIs.",
          importance: "Early detection and treatment of STIs are crucial for preventing long-term health issues and reducing the spread of infections to others.",
        },
        blood: {
          id: "blood",
          title: "Blood Pressure Checks",
          definition: "Blood pressure checks are routine tests to measure the force of blood against the walls of the arteries.",
          expect: "A healthcare provider will use a blood pressure cuff to measure your blood pressure, typically at the upper arm.",
          importance: "Regular blood pressure checks are vital for identifying hypertension early, reducing the risk of heart disease, stroke, and other related health issues.",
        },
        chole: {
          id: "chole",
          title: "Cholesterol Checks",
          definition: "Cholesterol checks are tests that measure the levels of cholesterol and other fats in your blood.",
          expect: "A healthcare provider will draw a blood sample to analyze cholesterol levels, including LDL (bad cholesterol), HDL (good cholesterol), and triglycerides.",
          importance: "Monitoring cholesterol levels is essential for identifying and managing the risk of cardiovascular diseases, including heart attacks and strokes.",
        },
      };
      this.modalContent = modalData[type];
    },
    closeModal() {
      this.modalContent = null;
    },
  },
};
</script>

<style scoped>
.wellness-hub {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  padding: 20px;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

.intro {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.intro h2 {
  color: #007bff;
}

.main {
  margin-bottom: 20px;
}

section {
  margin-bottom: 20px;
}

.health-checks ul {
  list-style: none;
  padding: 0;
}

.health-checks li {
  margin: 5px 0;
}

.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 20px;
  border: 2px solid #007bff;
  border-radius: 8px;
  z-index: 1000;
}

.popup h1 {
  margin-top: 0;
}

.close {
  background: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.close:hover {
  background: #0056b3;
}
</style>