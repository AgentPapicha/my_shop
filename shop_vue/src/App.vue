<template>
  <div id="wrapper">
    <nav class="navbar is-light menu">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Glee</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/about" class="navbar-item">About</router-link>
          <router-link to="/chairs" class="navbar-item">Chairs</router-link>
          <router-link to="/furnitures" class="navbar-item">Furnitures</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-top">
                <div class="footer-top__item footer-top__contact">
                    <a class="logo footer-top__logo" href="#">
                        <img class="logo__img " src="./assets/images/logo.png" alt="logo">
                    </a>
                    <a class="footer-top__adress" href="#">
                        ADDRESS: 4772 Wines Lane
                        Houston, TX 77032
                    </a>
                    <a class="footer-top__phone" href="tel:+8323475843">
                        Telephone: +832-347-5843
                    </a>
                    <a class="footer-top__email" href="mailto:contact@Glee.com">
                        Email: contact@Glee.com
                    </a>

                </div>
                <div class="footer-top__item footer-top__services">
                    <h6 class="footer-top__title">
                        Services
                    </h6>
                    <ul class="footer-top__list">
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                About us
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Return Policy
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Our Blog
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Contact Us
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Terms & Condition
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="footer-top__item footer-top__account">
                    <h6 class="footer-top__title">
                        Account
                    </h6>
                    <ul class="footer-top__list">
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Your Account
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Checkout
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Login
                            </a>
                        </li>
                        <li class="footer-top__item">
                            <a class="footer-top__link" href="#">
                                Register
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="footer-top__item footer-top__item-form">
                    <h6 class="footer-top__title">
                        newsletter
                    </h6>
                    <p class="footer-top__text">
                        Subscribe by our newsletter and get
                        update protidin.
                    </p>
                    <form class="footer-top__form" action="#">
                        <input class="footer-top__form-input" type="email" placeholder="Email address">
                        <button class="footer-top__form-btn" type="submit" required>
                            Subscribe
                        </button>
                    </form>
                </div>
            </div>
            <div class="footer-bot">
                <p class="footer-bot__copy">
                    ©2023 CopyRight Example. All rights reserved.
                </p>
                <menu class="footer-bot__menu">
                    <li class="footer-bot__menu-item">
                        <a class="footer-bot__menu-link" href="#">
                            Home
                        </a>
                    </li>
                    <li class="footer-bot__menu-item">
                        <a class="footer-bot__menu-link" href="#">
                            About
                        </a>
                    </li>
                    <li class="footer-bot__menu-item">
                        <a class="footer-bot__menu-link" href="#">
                            Blog
                        </a>
                    </li>
                    <li class="footer-bot__menu-item">
                        <a class="footer-bot__menu-link" href="#">
                            Contact
                        </a>
                    </li>
                </menu>
            </div>
        </div>
    </footer>
  </div>
</template>

<script>

import axios from "axios"

export default{
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
       }
     }
    },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}

</script>


<style lang="scss">
@import '../node_modules/bulma/';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

.button.is-primary {
    background-color: #a3bbc8;
    border-color: transparent;
    color: #fff;
}


.button.is-success {
    background-color: #a3bbc8;
    border-color: transparent;
    color: #fff;
}


.button.is-success:hover, .button.is-success.is-hovered {
    background-color: #414141;
    border-color: transparent;
    color: #fff;
}
</style>
