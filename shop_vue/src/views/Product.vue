<template>
    <div class="page-product">
        <div class="columns is multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">

                </figure>
                
                <h1 class="title">{{ product.name }}</h1>
                <p>{{ user_review_id }}</p>
                <p>{{ user_id }}</p>
                <p>{{ user_info }}</p>
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
            'quantity': 1,
            user_id: null,
            user_info: {},
            user_review_id: [],
        }
    },
    mounted() {
        this.getProduct(),
        this.getProductReviews(),
        // this.fetchUserId()
        // this.fetchUser(),
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

        // async fetchUserId() {
        //     try {
        //         const response = await this.$axios.get('/api/v1/users/'); // замените на ваш URL
        //         this.id = response.data
        //         // Дальше можете использовать this.userId по вашему усмотрению
        //     } catch (error) {
        //         console.error('Ошибка при получении id пользователя:', error);
        //     }
        //     },

        // fetchUser() {
        //     axios.defaults.headers.common["Authorization"] = ""
        //  axios.get("/api/v1/users/", {
        //         headers: {
        //             Authorization: `Token ${localStorage.getItem('token')}`
        //         }
        //         })
        //         .then(response => {
        //             this.user = response.data;
        //         })
        //         .catch(error => {
        //             console.error(error);
        //         });
        //     },
        // getUserInfo() {
        //     axios.defaults.headers.common["Authorization"] = ""

        //     localStorage.getItem("token")
        //     localStorage.getItem("username")
        //     const userid = localStorage.getItem("userid")


        // },

        async getProductReviews() {
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

        await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}/reviews`)
                .then(response => {
                    this.reviews = response.data
                    this.user_review_id = response.data.user
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async submitReview() {
            try {
                const category_slug = this.$route.params.category_slug
                const product_slug = this.$route.params.product_slug

                const reviewData = {
                user: this.user_id,
                content: this.review.content,
                stars: this.review.stars,
                }

                const response = await axios.post(`/api/v1/products/${category_slug}/${product_slug}/reviews/`, reviewData)
                console.log('Ответ от сервера:', response.data)


                this.review = {}
                this.getProductReviews()

                // Выведите уведомление о успешной отправке
                toast({
                    message: 'Отзыв успешно отправлен',
                    type: 'is-success',
                    position: 'bottom-right',
                    duration: 3000,
                });
            } catch (error) {
                console.error('Ошибка при отправке отзыва:', error.response.data);
            
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