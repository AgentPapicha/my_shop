<template>
    <div class="page-article">
        <h1 class="title has-text-centered">{{ article.title }}</h1>
            <figure class="image mb-6">
                <img v-bind:src="article.get_image">
            </figure>
        <h4 class="has-text-left">{{ article.created_at }}</h4>
        <p>{{ article.article_text }}</p>
        </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'Article',
    data() {
        return{
            article: {}
        }
    },
    mounted() {
        this.getArticle()
    },
    methods: {
        async getArticle() {
            this.$store.commit('setIsLoading', true)

            const article_slug = this.$route.params.article_slug

        await axios
                .get(`/api/v1/articles/${article_slug}`)
                .then(response => {
                    this.article = response.data

                    document.title = this.article.title + ' | Glee'
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false) 
        },
  
    }
}
</script>