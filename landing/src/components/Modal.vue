<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">Contactar soporte</slot>
          </div>

          <div class="modal-body">
            <slot name="body">
                <form>
                    <label>Asunto</label>
                    <input type="text" v-model="asunto">
                    <label>Email</label>
                    <input type="text" v-model="email">
                    <label>Mensaje</label>
                    <textarea class="form-control" rows="3" v-model="message"></textarea>
                </form>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button type="button" class="btn btn-primary" @click="saveMessage">Aceptar</button>
              <button type="button" class="btn btn-primary" @click="$emit('close')">Cerrar</button>
            </slot> 
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
import axios from "axios";

export default {
  props: {
    show: Boolean,
  },
  data() {
    return {
      email: null,
      asunto: null,
      message: null,
    }
  },
  methods: {
    saveMessage: function(){
      if (this.asunto && this.email && this.message) {
        axios
        .post("http://127.0.0.1:5100/save-message",
        {
          "business": this.asunto,
          "email": this.email,
          "message": this.message
        })
        .then(result => {
          console.log(result);
          this.$swal({ icon:'success', title: 'Mensaje enviado', target: document.getElementById('ventana')});
          })  
        .catch(error => console.log(error))
      } else {
        this.$swal({ icon:'error', title: 'Error: Campos vacios', target: document.getElementById('ventana')});
      }
    }
  }
};
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.753);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  text-align: center;
  color: #42b983;
}

.modal-body {
  margin: 10px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>