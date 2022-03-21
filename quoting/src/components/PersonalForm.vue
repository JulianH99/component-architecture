<template>
  <div>
    <h3 class="subtitle">Personal Data</h3>
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input class="input" type="text" placeholder="Text input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input class="input" type="text" placeholder="Text input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Phone</label>
      <div class="control">
        <input class="input" type="number" placeholder="Text input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Additional info</label>
      <div class="control">
        <textarea class="textarea" placeholder="Textarea"></textarea>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonalForm",
  components: {},
};
</script>