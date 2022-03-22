<template>
    <table class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Total Price</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th colspan="3">Total Supplies</th>
                <th>{{ total }}</th>
            </tr>
        </tfoot>
        <tbody>
            <tr v-for="supply in supplies" :key="supply.id">
                <td>{{supply.name}}</td>
                <td>{{supply.qty}}</td>
                <td>{{supply.price_suggested}}</td>
                <td>{{supply.qty * supply.price_suggested}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
  name: "ListSupplies",
  components: {},
  props: ['supplies', 'total'],
};
</script>