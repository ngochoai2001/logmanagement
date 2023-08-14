<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="user_name" class="form-label">Username:</label>
        <input type="text" name="user_name" v-model="user.user_name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="full_name" class="form-label">Full Name:</label>
        <input type="text" name="full_name" v-model="user.full_name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="pass_word" class="form-label">Password:</label>
        <input type="pass_word" name="pass_word" v-model="user.pass_word" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'RegistersForm',
  data() {
    return {
      user: {
        user_name: '',
        full_name: '',
        pass_word: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
        this.$router.push('/dashboard');
      } catch (error) {
        console.log(error)
        throw 'Username already exists. Please try again.';
      }
    },
  },
});
</script>
