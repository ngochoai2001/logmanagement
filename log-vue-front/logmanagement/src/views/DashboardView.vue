<template>
  <div>
    <section>
      <h1>Add new log</h1>
      <hr />
      <br />

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="system_subscribe" class="form-label">Hệ thống:</label>
          <input type="text" name="system_subscribe" v-model="form.system_subscribe" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="department_name" class="form-label">Đơn vị khai thác:</label>
          <textarea name="department_name" v-model="form.department_name" class="form-control"></textarea>
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
      form: {
        title: "",
        content: "",
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
  },
});
</script>
