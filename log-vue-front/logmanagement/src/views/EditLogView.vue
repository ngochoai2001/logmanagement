<template>
    <section>
      <h1>Edit log</h1>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditLog',
    props: ['logId'],
    data() {
      return {
        form: {
          title: '',
          content: '',
        },
      };
    },
    created: function() {
      this.GetLog();
    },
    computed: {
      ...mapGetters({ log: 'stateLog' }),
    },
    methods: {
      ...mapActions(['updateLog', 'viewLog']),
      async submit() {
      try {
        let log = {
          logId: this.logId,
          form: this.form,
        };
        await this.updateLog(log);
        this.$router.push({name: 'Log', params:{logId: this.log._id}});
      } catch (error) {
        console.log(error);
      }
      },
      async GetLog() {
        try {
          await this.viewLog(this.logId);
          this.form.title = this.log.title;
          this.form.content = this.log.content;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>