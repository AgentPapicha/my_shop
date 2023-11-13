
<template>
  <head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Glee</title>
  <link rel="stylesheet" href="../assets/css/style.min.css">
</head>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Glee
            </p>
            <p class="subtitle">
                The best furniture store online
            </p>
        </div>
    </section>
<main class="main">
  <section class="top-slider">

<div class="top-slider__wrapper">
    <div class="top-slider__item">
        <div class="top-slider__content">
            <h2 class="top-slider__title">
                SMART AND
                TRENDY
            </h2>
            <p class="top-slider__text">
                Dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
            </p>
            <a class="top-slider__link" href="#">
                Shop Now <span>→</span>
            </a>
        </div>
        <img class="top-slider__img" src="../assets/images/slider/photo.png" alt="slide img">
    </div>
    <!-- <div class="top-slider__item">
        <div class="top-slider__content">
            <h2 class="top-slider__title">
                SMART AND
                TRENDY
            </h2>
            <p class="top-slider__text">
                Dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
            </p>
            <a class="top-slider__link" href="#">
                Shop Now <span>→</span>
            </a>
        </div>
        <img class="top-slider__img" src="images/slider/photo.png" alt="slide img">
    </div>
    <div class="top-slider__item">
        <div class="top-slider__content">
            <h2 class="top-slider__title">
                SMART AND
                TRENDY
            </h2>
            <p class="top-slider__text">
                Dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
            </p>
            <a class="top-slider__link" href="#">
                Shop Now <span>→</span>
            </a>
        </div>
        <img class="top-slider__img" src="images/slider/photo.png" alt="slide img">
    </div> -->
</div>

</section>
</main>
    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />


    </div>
  </div>
</template>

<style lang="scss">
.top-slider {
    margin: 0 75px;
    background-color: #fcd7b6;

    &__content {
        padding-top: 225px;
        padding-left: 300px;
    }

    &__item {
        display: flex !important;
        justify-content: space-between;
    }

    &__title {
        max-width: 420px;
        // @extend %rubik-500;
        font-size: 72px;
        line-height: 70px;
        color: #243f4d;
        margin-bottom: 45px;
    }

    &__text {
        // @extend %rubik-400;
        color: #436372;
        max-width: 330px;
        margin-bottom: 45px;

    }

    &__link {
        background-color: #a3bbc8;
        padding: 25px 20px 25px 25px;
        // @extend %rubik-500;
        color: white;
        cursor: pointer;

        span {
            padding-left: 60px;
            font-size: 20px;
        }
    }

    &__img {
        padding: 100px 180px 0 0;
    }

}
</style>

<script>

import axios from 'axios'

import ProductBox from '@/components/Productbox.vue'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Glee'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>