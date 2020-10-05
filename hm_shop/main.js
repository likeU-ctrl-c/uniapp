import Vue from 'vue'
import App from './App'
import { myRequest } from './util/api.js'

Vue.prototype.$myRequest = myRequest
Vue.filter('formatDate',(data)=>{
			const newDate = new Date(data)
			const year = newDate.getFullYear()
			const monty = newDate.getMonth().toString().padStart(2,0)
			const day = newDate.getDay().toString().padStart(2,0)
			return year+'-'+monty+'-'+day
})
Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
