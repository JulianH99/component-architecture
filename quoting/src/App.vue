<template>
  <div class="container">
    <h2 class="title">Hola mundo</h2>
    <PersonalForm />
    <SupplyForm />
    <ListSupplies/>
  </div>
</template>

<script>
import PersonalForm from './components/PersonalForm.vue'
import SupplyForm from './components/SupplyForm.vue'
import ListSupplies from './components/ListSupplies.vue'
export default {
  name: "App",
  components: {
    PersonalForm,
    SupplyForm,
    ListSupplies,
  },
};
</script>

<style>
</style>
