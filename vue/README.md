# vue readme file

# init project
```bash
npm init vue@latest
cd vovie
npm install
npm run dev
```

# first single file component [SFC] web page
- main.js
```javascript
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
app.mount('#app')
```
- App.vue
```javascript
<template>
    <h1>{{ displayMessage }}</h1>
</template>
<script>
    // export default makes it possible for main.js to catch
    // the data with the import App from './App.vue'
    // so that could be mounted on the <div id="app"></div>
    // inside index.html
    export default {
        data() {
            return {
                displayMessage: 'This is some text displaying on vue'
            };
        }
    };
</script>
<style></style>
```

# vue components
- main.js
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import ComponentName from './components/ComponentName.vue'

const app = createApp(App)
app.component('component-name', ComponentName)
app.mount('#app')
```
- App.vue
```javascript
<template>
  <h1>Food</h1>
  <food-item/>
  <food-item/>
  <food-item/>
</template>

<script></script>

<style></style>
```
- ComponentName.vue
```javascript
<template>
  <div>
    <h2>{{ name }}</h2>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: 'Apples',
      message: 'I like apples'
    }
  }
};
</script>

<style></style>
```

# vue props
- main.js
```javascript

```
- App.vue
```javascript

```
- .vue
```javascript

```

# vue v-for components
- main.js
```javascript

```
- App.vue
```javascript

```
- .vue
```javascript

```

# 
- main.js
```javascript

```
- App.vue
```javascript

```
- .vue
```javascript

```

