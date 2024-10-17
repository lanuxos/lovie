<template>
    <div v-on:click="countClicks">
        <h2>{{ name }}</h2>
        <p>{{ message }}</p>
        <p>clicked count: {{ clicks }}</p>
        <h2>{{ foodName }}</h2>
        <h3>{{ foodDesc }}</h3>
        <button v-on:click="toggleFavorite">Favorite</button>
        <img src="../assets/pawPink.png" alt="Pink Paw" v-show="foodIsFavorite" height="50px" width="50px">
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: 'Apples',
            message: 'I like apples',
            clicks: 0,
            foodIsFavorite: this.isFavorite,
        }
    },
    // props: [
    //     'foodName',
    //     'foodDesc',
    //     'isFavorite',
    // ],
    props: {
        foodName: {
            type: String,
            required: true,
            validator: function (value) {
                if (10 < value.length && value.length < 20) {
                    return true;
                } else {
                    return false;
                }
            }
        },
        foodDesc: {type:String, required: false, default: 'this is food desc default value'},
        isFavorite: Boolean,
    },
    methods: {
        countClicks() {
            this.clicks++;
        },
        toggleFavorite() {
            this.foodIsFavorite = !this.foodIsFavorite;
        }
    }
};
</script>

<style></style>