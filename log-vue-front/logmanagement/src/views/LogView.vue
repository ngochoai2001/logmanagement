<template>
    <div v-if="log">
      <p><strong>Hệ thống</strong> {{ log.system_subscribe }}</p>
      <p><strong>Đơn vị khai thác</strong> {{ log.department_name }}</p>
      <p><strong>Đầu mối khai thác</strong> {{ log.personal_name }}</p>
      <p><strong>Log name</strong> {{ log.name }}</p>
      <p><strong>Open request time</strong> {{ log.open_date }}</p>
      <p><strong>Respond time (ms)</strong> {{ log.respond_time }}</p>
      <p><strong>IP request</strong> {{ log.remote_addr }}</p>
      <p><strong>Return request time</strong> {{ log.return_date }}</p>
      <p><strong>Port request</strong> {{ log.remote_port }}</p>
      <p><strong>Path info</strong> {{ log.path_info }}</p>
      <p><strong>Content length</strong> {{ log.content_length }}</p>
      <p><strong>Server port</strong> {{ log.remote_port }}</p>
      <p><strong>Content type</strong> {{ log.content_type }}</p>
      <p><strong>Server name</strong> {{ log.server_name }}</p>
      <p><strong>Server protocol</strong> {{ log.server_protocol }}</p>
      <p><strong>Access token</strong> {{ log.access_token }}</p>
      <p><strong>Function name</strong> {{ log.function_name	 }}</p>
      <p><strong>Http user agent</strong> {{ log.http_user_agent	 }}</p>
      <p><strong>Query string</strong> {{ log.query_string }}</p>
      <p><strong>Note</strong> {{ log.msg }}</p>
  
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