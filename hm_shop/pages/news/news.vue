<template>
	<news-item @itemClick="goDetail" :list = "newsList"></news-item>
</template>

<script>
	import newitem from "../../template/new-item/news-item.vue"
	export default {
		data() {
			return {
				newsList:[]
			}
		},
		methods: {
			async getNews(){
				const res = await	this.$myRequest({
					url:'/getnews/'
				})
				this.newsList = res.data.message
				console.log(res)
			},
			goDetail(id){
				console.log(id)
				uni.navigateTo({
					url:'/pages/news-detail/news-detail?id='+id
				})
			}
		},
		
		components:{
			"news-item":newitem
		},
		onLoad() {
			this.getNews()
		}
	}
</script>

<style lang="scss">
	.news{
		
	}
</style>
