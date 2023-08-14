import axios from 'axios';

const state = {
  user: null,
  token:null
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
  token: state => state.token
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('register', form);
    let UserForm = new FormData();
    UserForm.append('username', form.user_name);
    UserForm.append('password', form.pass_word);
    await dispatch('logIn', UserForm);
  },
  async logIn({dispatch}, user) {
    let {data}  = await axios.post('login', user);
    await dispatch('viewMe', data);
  },
  async viewMe({commit}, data) {
    const {user, token } =  data 
    await commit('setUser', user);
    await commit('setToken', token);
    localStorage.setItem("token", token);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    let token = null;
    await commit('setToken', token);
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  logout(state, user){
    state.user = user;
  },
  setToken(state, token){
    state.token  = token;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
