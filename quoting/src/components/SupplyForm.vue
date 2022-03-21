<template>
  <div>
    <h3 class="subtitle">Supply info</h3>
    <div class="field is-grouped">
      <p class="control has-icons-left">
        <span class="select">
          <select>
            <option selected>
              Country one twu the daosdau ad adasd ad sad a
            </option>
            <option>Select dropdown</option>
            <option>With options</option>
          </select>
        </span>
        <span class="icon is-small is-left">
          <i class="fas fa-globe"></i>
        </span>
      </p>
      <p class="control is-expanded">
        <input class="input" type="number" placeholder="Quantity" />
      </p>
      <p class="control">
        <a class="button is-success"> Add </a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SupplyForm",
  components: {},
};
</script>