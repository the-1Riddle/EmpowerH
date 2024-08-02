<template>

    <main class="l-main">
        <!---------- HOME ---------->
        <section class="section bd-container">
            <div style="text-align: center;">
                <div class="home__data">
                    <h1 class="home__title">EmpowerHer Forum</h1>
                </div>
            </div>
            <br>
            <hr>
            <ul class="nav nav-underline justify-content-center">
                <li class="nav-item">
                    <a class="nav-link nav__link active" href="#">Categories</a>
                </li>
                <li>
                    <a class="nav-link nav__link" href="#">Latest</a>
                </li>
                <li>
                    <a class="nav-link nav__link" href="#">Top</a>
                </li>
                <li>
                    <a class="nav-link nav__link" href="#">My Posts</a>
                </li>
                <li>
                    <a class="nav-link nav__link" href="#">Bookmarks</a>
                </li>
                <nav class="navbar bg-body-tertiary">
                    <div class="container-fluid">
                        <form class="d-flex" role="search">
                            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                            <button class="btn btn-outline-success" type="submit">Search</button>
                        </form>
                    </div>
                </nav>
                <li class="nav-right">
                    <button type="button" class="btn btn-secondary"><i class="bi bi-plus"></i> New Topic</button>
                </li>
            </ul>
            <hr>
        </section>

        <!---- Wellness ----->
        <section class="menu section1 bd-container" id="Wellness">

            <div class="menu__container bd-grid">
                <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="..." class="img-fluid rounded-start" alt="...">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="..." class="img-fluid rounded-start" alt="...">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="..." class="img-fluid rounded-start" alt="...">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!--- Wellness End --->

        <!---- Discusions ---->
        <section class="menu section1 bd-container" id="Awareness">
            <h2 class="section-title" style="text-align: left;">Latest Discusions</h2>
            <hr>

            <div class="menu__container bd-grid">
                <!--- Discusions goes here --->
            </div>
            <br>
            <div class="content-subtitle">
                <a href="#"><span class="content-subtitle"> Read More »</span></a>
            </div>
        </section>
        <!---- Discusions End ---->

    </main>

</template>