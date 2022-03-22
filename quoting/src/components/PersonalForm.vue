<template>
  <div>
    <h3 class="subtitle">Personal Data</h3>
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input
          v-model="customer.name"
          class="input"
          type="text"
          placeholder="Text input"
          @input="(event) => $emit('update:customer', customer)"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input
          v-model="customer.email"
          class="input"
          type="text"
          placeholder="Text input"
          @input="(event) => $emit('update:customer', customer)"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Phone</label>
      <div class="control">
        <input
          v-model="customer.phone"
          class="input"
          type="number"
          placeholder="Text input"
          @input="(event) => $emit('update:customer', customer)"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Additional info</label>
      <div class="control">
        <textarea
          v-model="customer.additional_info"
          class="textarea"
          placeholder="Textarea"
        ></textarea>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonalForm",
  data() {
    return {
      customer: {},
    };
  },
  components: {},
};
</script>