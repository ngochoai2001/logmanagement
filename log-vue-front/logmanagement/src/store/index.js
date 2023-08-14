import { createStore } from "vuex";

import log from './modules/log';
import user from './modules/user';

export default createStore({
  modules: {
    log,
    user,
  }
});