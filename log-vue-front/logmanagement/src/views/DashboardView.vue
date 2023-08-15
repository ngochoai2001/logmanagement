<template>
  <div>
    <section>
      <h1 style="fa-plus" @click="creating">Add new log</h1>
      <hr />
      <br />

      <form @submit.prevent="submit" v-show="isCreating == true">
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

    <br /><br />

    <section>
      <h1>Logs</h1>
      <hr />
      <br />

      <div v-if="logs && logs.length">
        <div v-for="log in logs" :key="log._id" class="logs">
          <div class="card" style="width: 18rem; float:left">
            <div class="card-body">
              <ul>
                <li><strong>Hệ thống</strong> {{ log.system_subscribe }}</li>
                <li><strong>Đơn vị khai thác</strong> {{ log.department_name }}</li>
                <li><strong>Đầu mối khai thác</strong> {{ log.personal_name }}</li>
                <li><strong>Log name</strong> {{ log.name }}</li>
                <li><strong>Open request time</strong> {{ log.open_date }}</li>
                <li><strong>Reponse time (ms)</strong> {{ log.respond_time }}</li>
                <li><strong>IP request</strong> {{ log.remote_addr }}</li>
                <li>
                  <router-link :to="{ name: 'Log', params: { logId: log._id } }"
                    >View</router-link
                  >
                </li>
              </ul>
            </div>
          </div>
          <br />
        </div>
      </div>


      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";

export default defineComponent({
  name: "DashboardView",
  data() {
    return {
      isCreating: false,
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
  created: function () {
    return this.$store.dispatch("getLogs");
  },
  computed: {
    ...mapGetters({ logs: "stateLogs" }),
  },
  methods: {
    ...mapActions(["createLog"]),
    async submit() {
      await this.createLog(this.form);
    },
    creating(){
      this.isCreating = !this.isCreating
    },
  },
});
</script>
