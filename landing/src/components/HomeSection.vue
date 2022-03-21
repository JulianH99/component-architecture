<template>
    <div id="home">
        <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
            <a href="#home" class="navbar-brand">
                <img src="" alt="Brand" />
            </a>
            <button
                type="button"
                class="navbar-toggler"
                data-toggle="collapse"
                data-target="#navbarResponsive"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collpase navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a href="#home" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="#contact"  class="nav-link">Contact</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div 
        class="hero home-hero"
        :style="{backgroundImage:`url(${banner.background_image})`}"
        >
            <div class="overlay"></div>
        </div>
        <div class="caption text-center">
            <h1>{{ banner.title }}</h1>
            <h3>{{ banner.description }}</h3>
            <a
                target="_blank"
                class="btn btn-outline-light btn-lg"
                id="show-modal" 
                @click="showModal = true"
            >
                Contactar soporte
            </a>
            
            <Teleport to="body" v-if="activeModal === '' ">
                <modal :show="showModal">
                    <template #header>
                        <h3>Contactar soporte</h3>
                    </template>
                </modal>
            </Teleport>
        </div>
    </div>
</template>

<script>
import Modal from '../components/Modal.vue'
export default {
    name: "home",
    data() {
        return {
            banner: null,
            title: null,
            activeModal: null,
            showModal: false
        }
    },
    mounted(){
         axios
         .get('http://127.0.0.1:5000/api/banner')
         .then(response => (this.banner = response.data))
         .catch(error => console.log(error)),
         axios
         .get('http://127.0.0.1:5000/api/title')
         .then(response => (this.title = response.data))
         .catch(error => console.log(error)),
         axios
         .get('http://127.0.0.1:5100/support/active')
         .then(response => (this.activeModal = response.data))
         .catch(error => console.log(error))
    },
    components: {
        Modal
    },
    methods: {
    }
};
</script>

<style scoped>
.navbar {
    text-transform: uppercase;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.1rem;
    background-color: rgba(0, 0, 0, 0.7) !important;
}
.navbar-brand img {
    height: 2rem;
}
.navbar-toggler {
    outline: none !important;
}
.navbar-nav li {
    padding-right: 0.5rem;
}
.navbar .navbar-nav .nav-link {
    color: white;
    padding-top: 0.8rem;
}
.navbar .navbar-nav .nav-link.active,
.navbar .navbar-nav .nav-link:hover {
    color: #1ebba3;
    cursor: pointer;
}
.hero {
    height: 100vh;
    width: 100%;
    position: relative;
}
.hero .overlay {
    position: absolute;
    top: 0;
    height: 100vh;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.7);
}
.home-hero {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
.caption {
    position: absolute;
    top: 35%;
    width: 100%;
    color: white;
    text-transform: uppercase;
}
.caption h1 {
    font-size: 3.8rem;
    font-weight: bold;
    letter-spacing: 0.3rem;
    text-shadow: 0.1rem 0.1rem 0.8rem black;
    padding-bottom: 1rem;
}
.caption h3 {
    font-size: 2rem;
    text-shadow: 0.1rem 0.1rem 0.8rem black;
    padding-bottom: 1rem;
}
</style>