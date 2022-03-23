<template>
  <div v-if="active" class="container">
    <h2 class="title">Hola mundo</h2>
    <PersonalForm @update:customer="customer=$event" />
    <SupplyForm @add:supply="addSupply($event)" />
    <ListSupplies :supplies="quote.supplies" :total="quote.total" />
  </div>
  <section class="hero is-danger" v-else>
    <div class="hero-body">
      <p class="title">Error: The service not found</p>
      <p class="subtitle">Please contact with your IT center</p>
    </div>
  </section>
</template>

<script>
import PersonalForm from "./components/PersonalForm.vue";
import SupplyForm from "./components/SupplyForm.vue";
import ListSupplies from "./components/ListSupplies.vue";
import axios from "axios"

const host = 'http://localhost:5200/api/'

export default {
  name: "App",
  components: {
    PersonalForm,
    SupplyForm,
    ListSupplies,
  },
  data() {
    return {
      quote: {
        supplies: [],
        total: 0,
      },
      customer: {},
      active: true
    };
  },
  mounted() {
    axios.get(host + 'alive')
    .then(() => {
      this.active = true
    })
    .catch(() => {
      this.active = false
    })
  },
  methods:{
    addSupply(e){
      this.quote.total += e.price_suggested * e.qty
      this.quote.supplies.push(e)
    }
  }
};
</script>

<style>
</style>
