const routes = [
    {path:'/',component:httpVueLoader('./static/js/components/IndexPage.vue')},
    {path:'/result',component:httpVueLoader('./static/js/components/ResultPage.vue')},
];
const router = new VueRouter({
    mode:"history",
    routes
});
var app = new Vue({
    el:"#app",
    router:router,
})
