<template>
    <section>
      <h1>Edit log</h1>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        
        <div class="mb-3">
          <label for="system_subscribe" class="form-label">Hệ thống</label>
          <input type="text" name="system_subscribe" v-model="form.system_subscribe" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="department_name" class="form-label">Đơn vị khai thác</label>
          <textarea name="department_name" v-model="form.department_name" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="personal_name" class="form-label">Đầu mối khai thác</label>
          <textarea name="personal_name" v-model="form.personal_name" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="open_date" class="form-label">Open request time</label>
          <input type="datetime-local"  name="open_date" v-model="form.open_date" class="form-control">
        </div>
        <div class="mb-3">
          <label for="name" class="form-label">Log name</label>
          <input name="name" v-model="form.name" class="form-control">
        </div>

        <div class="mb-3">
          <label for="respond_time" class="form-label">Respond time (ms)</label>
          <input type="text" name="respond_time" v-model.number="form.respond_time" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="remote_addr" class="form-label">IP request</label>
          <textarea name="remote_addr" v-model="form.remote_addr" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="return_date" class="form-label">Return request time</label>
          <input type="datetime-local" name="return_date" v-model="form.return_date" class="form-control">
        </div>
        <div class="mb-3">
          <label for="remote_port" class="form-label">Port request</label>
          <input type="number" min="0" name="remote_port" v-model.number="form.remote_port" class="form-control">
        </div>
        <div class="mb-3">
          <label for="path_info" class="form-label">Path info</label>
          <input name="path_info" v-model="form.path_info" class="form-control">
        </div>
        <div class="mb-3">
          <label for="content_length" class="form-label">Content length</label>
          <input type="number" min="0" name="content_length" v-model.number="form.content_length" class="form-control">
        </div>
        <div class="mb-3">
          <label for="remote_port" class="form-label">Server port</label>
          <input type="number" min="0" name="remote_port" v-model.number="form.server_port" class="form-control">
        </div>
        <div class="mb-3">
          <label for="p_request_method" class="form-label">Request method</label>
          <input type="number" min="0" name="p_request_method" v-model="form.p_request_method" class="form-control">
        </div>
        <div class="mb-3">
          <label for="content_type" class="form-label">Content type</label>
          <input  name="content_type" v-model="form.content_type" class="form-control">
        </div>
        <div class="mb-3">
          <label for="server_name" class="form-label">Server name</label>
          <input name="server_name" v-model="form.server_name" class="form-control">
        </div>
        
        <div class="mb-3">
          <label for="server_protocol" class="form-label">Server protocol</label>
          <input name="server_protocol" v-model="form.server_protocol" class="form-control">
        </div>
        <div class="mb-3">
          <label for="access_token" class="form-label">Access token</label>
          <input  name="access_token" v-model="form.access_token" class="form-control">
        </div>
        <div class="mb-3">
          <label for="function_name" class="form-label">Function name</label>
          <input name="function_name" v-model="form.function_name" class="form-control">
        </div>
        <div class="mb-3">
          <label for="http_user_agent" class="form-label">Http user agent</label>
          <input name="http_user_agent" v-model="form.http_user_agent" class="form-control">
        </div>
        <div class="mb-3">
          <label for="query_string" class="form-label">Query string</label>
          <input name="query_string" v-model="form.query_string" class="form-control">
        </div>
        <div class="mb-3">
          <label for="msg" class="form-label">Note</label>
          <input name="msg" v-model="form.note" class="form-control">
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
          system_subscribe: "",
          department_name : "",
          personal_name:"",
          name : "",
          open_date  : "",
          respond_time : 0,
          remote_addr  : "",
          return_date  : "",
          remote_port   : 0,
          path_info : "",
          content_length  : 0,
          server_port:0,
          p_request_method:"",
          content_type   : "",
          server_name   : "",
          server_protocol  : "",
          access_token   : "",
          function_name	   : "",
          http_user_agent	    : "",
          query_string 	   : "",
          msg 	    : "",
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
          this.form.system_subscribe = this.log.system_subscribe;
          this.form.department_name = this.log.department_name;
          this.form.personal_name = this.log.personal_name;
          this.form.name = this.log.name;
          this.form.open_date = this.log.open_date;
          this.form.respond_time = this.log.respond_time;
          this.form.remote_addr = this.log.remote_addr;
          this.form.return_date = this.log.return_date;
          this.form.remote_port = this.log.remote_port;
          this.form.path_info = this.log.path_info;
          this.form.content_length = this.log.content_length;
          this.form.server_port = this.log.server_port;
          this.form.p_request_method = this.log.p_request_method;
          this.form.content_type = this.log.content_type;
          this.form.server_name = this.log.server_name;
          this.form.server_protocol = this.log.server_protocol;
          this.form.access_token = this.log.access_token;
          this.form.function_name = this.log.function_name;
          this.form.http_user_agent = this.log.http_user_agent;
          this.form.query_string = this.log.query_string;
          this.form.msg = this.log.msg;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>