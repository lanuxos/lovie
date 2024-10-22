<template>
  <h1>Hello Vue</h1>
  <h2>{{ message }}</h2>
  <food-item food-name="Soup1234567" food-desc="with water" v-bind:is-favorite="true"/>
  <food-item food-name="rice1234567" v-bind:is-favorite="false"/>
  <div>
    <drink-item v-for="d in drinks" v-bind:drink-name="d"></drink-item>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "first msg from vue",
      drinks: ['Pepsi', 'Cocacola', 'Red Bull'],
    };
  }
};
</script>

<style>
#app>div {
  border: dashed black 1px;
  display: inline-block;
  margin: 10px;
  padding: 10px;
  background-color: lightgreen;
}

body {
  cursor: url('./components/icons/paw.svg'), auto;
}

#app>div:hover {
  cursor: url('./components/icons/pawGradient.svg'), auto;
}
</style>
