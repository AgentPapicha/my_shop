<template>
    <div class="page-product">

        <div class="catalog-card2">
            <div class="catalog-card2__imgbox">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">
                </figure>
            </div>
            <div class="catalog-card2__description">
                <h4 class="catalog-card2__title">
                    {{ product.name }}
                </h4>
                <div class="catalog-card2__star " data-rateyo-rating="4"></div>
                <p class="catalog-card2__price">
                    ${{ product.price }}
                </p>
                <p class="catalog-card2__text">
                    {{ product.description }}
                </p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns is multiline">

            <div class="column is-9">
                <h2 class="title">Reviews:</h2>
                <div v-for="review in reviews" :key="review.id" class="review-wrapper">
                    <p class="title">Review</p>
                    <p>User_name: {{ review.user }}</p>
                    <p>Stars: {{ review.stars }}</p>
                    <p class="review-wrapper__text">Review text:{{ review.content }}</p>
                    <p>Date: {{ review.date_added }}</p>
                </div>

                <div>
                    <form @submit.prevent="submitReview">
                        <label for="content">Отзыв:</label>
                        <textarea v-model="review.content" id="content" required></textarea>

                        <label for="stars">Оценка:</label>
                        <input v-model.number="review.stars" type="number" id="stars" required max="5" />

                        <button type="submit">Отправить отзыв</button>
                    </form>
                </div>
            </div>
        </div>

    </div>
</template>

<style lang="scss">

.catalog-card2 {
    display: flex;
    justify-content: space-evenly;

    &__description{
        max-width: 700px;
    }
}

.review-wrapper {
    margin-bottom: 20px;
    border-bottom: 1px solid #a3bbc8;

    &__text {
        font-size: 16px;
        line-height: 30px;
        color: #2292a5;
    }

}

</style>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            review: {},
            reviews: {},
            'quantity': 1,
            user_id: null,
            user_info: {},
            userreviewid: [],
            review_userid_List: [],
        }
    },
    mounted() {
        this.getProduct(),
            this.getProductReviews(),
            this.getUserInfo()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | Glee'
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async getUserInfo() {

            await axios
                .get('api/v1/users/me/', {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                    }
                })
                .then(response => {
                    this.user_info = response.data
                    this.user_id = response.data.id
                })
                .catch(error => {
                    console.log(error)
                })
        },


        async getProductReviews() {
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}/reviews`)
                .then(response => {
                    this.reviews = response.data
                    this.review_userid_List = this.reviews.map(review => review.user)
                })
                .catch(error => {
                    console.log(error)
                })
        },


        async submitReview() {
            if (this.review_userid_List.includes(this.user_id)) // Checking whether the user has left a review for this product
                toast({
                    message: 'You already have a review for this product!',
                    type: 'is-warning',
                    position: 'center',
                    duration: 3000,
                });
            else
                try {
                    const category_slug = this.$route.params.category_slug
                    const product_slug = this.$route.params.product_slug

                    const reviewData = {
                        user: this.user_id,
                        content: this.review.content,
                        stars: this.review.stars,
                    }


                    const response = await axios.post(`/api/v1/products/${category_slug}/${product_slug}/reviews/`, reviewData)
                    console.log('Server response:', response.data)


                    this.review = {}
                    this.getProductReviews()


                    toast({
                        message: 'Review sent successfully',
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000,
                    });
                } catch (error) {
                    console.error('Error sending review:', error.response.data);

                    toast({
                        message: 'Error sending review',
                        type: 'is-danger',
                        position: 'bottom-right',
                        duration: 3000,
                    });
                }
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })


        }
    }
}
</script>