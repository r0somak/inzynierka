import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Register from '../views/Register.vue';
import HomeLoged from '../views/HomeLoged.vue';
import EditProfile from '../views/EditProfile.vue';
import NewVisit from '../views/NewVisit.vue';
import VisitList from '../views/VisitList.vue';
import VisitDetails from '../views/VisitDetails.vue';
import VisitDiagnosis from '../views/VisitDiagnosis.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/homeloged',
    name: 'homeloged',
    component: HomeLoged,
  },
  {
    path: '/editprofile',
    name: 'editprofile',
    component: EditProfile,
  },
  {
    path: '/visit',
    name: 'newvisit',
    component: NewVisit,
  },
  {
    path: '/visitlist',
    name: 'visitlist',
    component: VisitList,
  },
  {
    path: '/visitdetails/:id',
    name: 'visitdetails',
    component: VisitDetails,
  },
  {
    path: '/visitdiagnosis/:id',
    name: 'visitdiagnosis',
    component: VisitDiagnosis,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
