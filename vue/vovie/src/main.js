
import { createApp } from 'vue'
import App from './App.vue'
import FoodItem from './components/FoodItem.vue'
import DrinkItem from './components/DrinkItem.vue'

const app = createApp(App)
app.component('food-item', FoodItem)
app.component('drink-item', DrinkItem) 
app.mount('#app')
