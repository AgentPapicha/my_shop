<template>
    <div class="page-product">
        <div class="columns is multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">

                </figure>

                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>

                <div v-for="review in reviews" :key="review.id" class="review-wrapper">
                    <p style="font-size:20px">Review</p>
                    <p>User_name: {{ review.user}}</p>
                    <p>Stars: {{ review.stars}}</p>
                    <p style="color: blue;">Review text:{{ review.content }}</p>
                </div>
                <div>
                <form @submit.prevent="submitReview">
                <label for="content">Отзыв:</label>
                <textarea v-model="review.content" id="content" required></textarea>

                <label for="stars">Оценка:</label>
                <input v-model.number="review.stars" type="number" id="stars" required/>

                <button type="submit">Отправить отзыв</button>
                </form>
            </div>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ product.price }}</p>

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

    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return{
            product: {},
            review: {},
            reviews: [],
            'quantity': 1
        }
    },
    mounted() {
        this.getProduct(),
        this.getProductReviews()
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

        async getProductReviews() {
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

        await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}/reviews`)
                .then(response => {
                    this.reviews = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async submitReview() {
            try {
                const category_slug = this.$route.params.category_slug;
                const product_slug = this.$route.params.product_slug;

                const reviewData = {
                id: 1,
                user: 4,
                date_added: "2023-11-26T17:07:18.121227Z", 
                content: this.review.content,
                stars: this.review.stars,
                };

                const response = await axios.post(`/api/v1/products/${category_slug}/${product_slug}/reviews/`, reviewData);
                console.log('Ответ от сервера:', response.data);


                this.review = {}; // Очистка формы после отправки отзыва
                this.getProductReviews(); // Обновление списка отзывов

                // Выведите уведомление о успешной отправке
                toast({
                    message: 'Отзыв успешно отправлен',
                    type: 'is-success',
                    position: 'bottom-right',
                    duration: 3000,
                });
            } catch (error) {
                console.error('Ошибка при отправке отзыва:', error.response.data);
                // Обработка ошибки, например, вывод сообщения пользователю
                toast({
                    message: 'Ошибка при отправке отзыва',
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