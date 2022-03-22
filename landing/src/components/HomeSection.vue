<template>
    <div id="home">
        <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
            <a href="#home" class="navbar-brand">
                <img src="@/assets/images/Logo.png" alt="Brand" />
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
        v-if="banner && error === false"
        class="hero home-hero"
        :style="{backgroundImage:`url(${banner.background_image})`}"
        >
            <div class="overlay"></div>
        </div>
        <div 
        v-if="banner && error === false"
        class="caption text-center"
        >
            <h1 v-if="banner">{{ banner.title }}</h1>
            <h3 v-if="banner">{{ banner.description }}</h3>
            <a
                target="_blank"
                class="btn btn-outline-light btn-lg"
                id="show-modal" 
                @click="showModal = true"
                v-if="activeModal === '' "
            >
                Contactar soporte
            </a>
            <br>

            <Teleport to="body" v-if="activeModal === '' ">
                <modal :show="showModal" @close="showModal = false" id="ventana">
                    <template #header>
                        <h3>Contactar soporte</h3>
                    </template>
                </modal>
            </Teleport>
        </div>
        <div v-else>
            <br>
            <br>
            <br>
            <br>
            <div class="alert alert-warning" role="alert">
                <b>ERROR:</b> CARGANDO DATOS, LOS DATOS QUE NO SE HAN CARGADO SON
                <div v-if="banner===null"> - Banner ->  'http://127.0.0.1:5000/api/banner'</div>
                <div v-if="title===null"> - Titulo -> 'http://127.0.0.1:5000/api/title'</div>
            </div>
        </div>
        <footer id="fotter">
                <div class="row">
                    <div class="col-md-1"></div>
                    <div class="col-md-5 text-center">
                        <br>
                        <img src="../assets/images/logo.png" />
                        <br>         
                    </div>
                    <div class="col-md-4 text-center">
                        <br>
                        <p> DISEÑO ARQUITECTURAL DE SOFTWARE Y PATRONES </p>
                        <strong>Presentado por: </strong>
                        <br>
                        <br>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">Juan Camilo Sánchez - 20171020131</li>
                            <li class="list-group-item">Julián Barrios - 20171020123</li>
                            <li class="list-group-item">Sebastian Chacon Benitez - 20171020148</li>
                        </ul>  
                        <br>
                    </div>
                    <div class="col-md-3"></div>
                </div>
                
        </footer>
    </div>
</template>

<script>
import Modal from '../components/Modal.vue';
import axios from "axios";

export default {
    name: "home",
    data() {
        return {
            banner: null,
            title: null,
            activeModal: null,
            showModal: false,
            error: false,
        }
    },
    mounted(){
         axios
         .get('http://127.0.0.1:5000/api/banner')
         .then(response => (this.banner = response.data))
         .catch(error => {
             console.log(error);
             this.error = true;
         }),
         axios
         .get('http://127.0.0.1:5000/api/title')
         .then(response => (this.title = response.data))
         .catch(error => {
             console.log(error);
             this.error = true;
         }),
         axios
         .get('http://127.0.0.1:5100/support/active')
         .then(response => (this.activeModal = response.data))
         .catch(error => {
             console.log(error);
         })   
    },
    components: {
        Modal
    }
};
</script>

<style scoped>

.navbar {
    text-transform: uppercase;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.1rem;
    background-color:   rgba(42, 87, 13, 0.459) !important;
}
ul{
    color: black;
}
.navbar-brand img {
    height: 3rem;
}

#fotter{
    color: white;
    text-transform: uppercase;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.1rem;
    background-color:   rgb(55, 97, 47) !important;
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