<template>
  <div v-if="active" class="container">
    <h2 class="title">Hola mundo</h2>
    <PersonalForm @update:customer="customer=$event" />
    <SupplyForm @add:supply="addSupply($event)" />
    <ListSupplies :supplies="quote.supplies" :total="quote.total" />
  </div>
  <div v-else>
    <p>Page not found</p>
  </div>
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
