import Vue from 'vue'
import NavBar from './components/NavBar.vue'

Vue.config.productionTip = false


Vue.component('custom-navbar', NavBar);

new Vue({el: "#apphandle"})