<template>
  <div>
    <h3 class="subtitle">Supply info</h3>
    <div class="field is-grouped">
      <p class="control has-icons-left">
        <span class="select">
          <select v-model="supply">
            <option selected :value="0">Choose Supply</option>
            <option v-for="supply in supplies" :key="supply.sku" :value="supply">
              {{ supply.name }}
            </option>
          </select>
        </span>
        <span class="icon is-small is-left">
          <i class="fas fa-globe"></i>
        </span>
      </p>
      <p class="control is-expanded">
        <input class="input" type="number" placeholder="Quantity" v-model="qty" />
      </p>
      <p class="control">
        <a class="button is-success" @click="addSupply"> Add </a>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const host = 'http://localhost:5000/api/'

export default {
  name: "SupplyForm",
  components: {},
  data(){
    return {
      supplies: [],
      supply: 0,
      qty: 0,
    }
  },
  mounted (){
    axios.get(host + 'supply')
    .then((res) => {
      this.supplies = res.data
    })
    .catch((e) => {
      console.log(e)
    })
  },
  methods:{
    addSupply(){
      this.supply.qty = this.qty;
      return this.$emit('add:supply', this.supply)
    }
  }
};
</script>