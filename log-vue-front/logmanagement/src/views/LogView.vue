<template>
    <div v-if="log">
      <p><strong>System Subcribe</strong> {{ log.system_subscribe }}</p>
      <p><strong>Content:</strong> {{ log.department_name }}</p>
      <!-- <p><strong>Author:</strong> {{ log.author.username }}</p> -->
  
      <div>
        <p><router-link :to="{name: 'EditLog', params:{logId: log._id}}" class="btn btn-primary">Edit</router-link></p>
        <p><button @click="removeLog()" class="btn btn-secondary">Delete</button></p>
      </div>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'LogView',
    props: ['logId'],
    async created() {
      try {
        await this.viewLog(this.logId);
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    },
    computed: {
      ...mapGetters({ log: 'stateLog', user: 'stateUser'}),
    },
    methods: {
      ...mapActions(['viewLog', 'deleteLog']),
      async removeLog() {
        try {
          await this.deleteLog(this.logId);
          this.$router.push('/dashboard');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>