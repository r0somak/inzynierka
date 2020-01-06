import Vue from 'vue';

import {
  ValidationObserver, ValidationProvider, extend, localize,
} from 'vee-validate';
import en from 'vee-validate/dist/locale/en.json';
import * as rules from 'vee-validate/dist/rules';
import axios from 'axios';
import VueAxios from 'vue-axios';
import BootstrapVue from 'bootstrap-vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'vue-navigation-bar/dist/vue-navigation-bar.css';

// eslint-disable-next-line import/order
import VueNavigationBar from 'vue-navigation-bar';

Vue.component('vue-navigation-bar', VueNavigationBar);

Vue.use(BootstrapVue);

Vue.use(VueAxios, axios);

// install rules and localization
Object.keys(rules).forEach((rule) => {
  extend(rule, rules[rule]);
});

localize('en', en);

// Install components globally
Vue.component('ValidationObserver', ValidationObserver);
Vue.component('ValidationProvider', ValidationProvider);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
