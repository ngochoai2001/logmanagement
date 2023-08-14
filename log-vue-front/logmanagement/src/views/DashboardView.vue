<template>
  <div>
    <section>
      <h1>Add new log</h1>
      <hr />
      <br />

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea name="content" v-model="form.content" class="form-control"></textarea>
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
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <ul>
                <li>{{log._id}}</li>
                <li><strong>System Describe</strong> {{ log.system_subscribe }}</li>
                <li><strong>Department name</strong> {{ log.department_name }}</li>
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
