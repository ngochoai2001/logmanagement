import axios from 'axios';
const state = {
  logs: null,
  log: null
};

const getters = {
  stateLogs: state => state.logs,
  stateLog: state => state.log,
};

const actions = {
  async createLog({dispatch}, log) {
    await axios.post('logs', log);
    await dispatch('getLogs');
  },
  async getLogs({commit}) {
    let {data} = await axios.get('logs/',
    {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem("token")}`
      }
    });
    commit('setLogs', data.data);
  },
  async viewLog({commit}, logId) {
    let {data} = await axios.get(`logs/${logId}`,
      {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem("token")}`
        }
      }
    );
    commit('setLog', data.data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateLog({}, log) {
    await axios.patch(`log/${log._id}`, log.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteLog({}, logId) {
    await axios.delete(`log/${logId}`);
  }
};

const mutations = {
  setLogs(state, logs){
    state.logs = logs;
  },
  setLog(state, log){
    state.log = log;
  },
};

export default {
  state,
  getters,
  actions,
  mutations  
};