<template>
	<view class="goods_list">
		<goods-list :goods = "goods" @goodsItemClick='goGoodsDetail'></goods-list>
		<view class="isOver" v-if="flag">-------我是有底线的------</view>
	</view>
</template>

<script>
	import goodsList from "../../template/goods-list/goods-list.vue"
	export default {
		data() {
			return {
				pageindex:1,
				goods:[],
				flag:false
			}
		},
		components:{
			"goods-list":goodsList,
		},
		methods: {
			//获取商品列表的数据
			async getGoodsList(callBack){
				const res = await this.$myRequest({
					url:'/gethotgoods/'+this.pageindex
				})
				this.goods =[...this.goods,...res.data.message]
				console.log("goods.vue->getgoodslist",res)
				callBack && callBack()
			},
			//导航到商品详情页面
			goGoodsDetail(id){
				uni.navigateTo({
					url:'/pages/goods-detail/goods-detail?id='+id
				})
			}
		},
		onLoad() {
			this.getGoodsList()
		},
		onReachBottom() {
			if(this.goods.length<this.pageindex * 5){
				this.flag = true
				return
			}
			console.log("触底了")
			this.pageindex +=1
			this.getGoodsList()
		},
		onPullDownRefresh() {
			this.pageindex =1
			this.goods = []
			this.flag = false
			setTimeout(() => {
				this.getGoodsList(()=>{
					uni.stopPullDownRefresh()
				})
			}, 1000);
			
		},
			
	}
</script>

<style lang="scss">
	.goods_list{
		background:#eee;
	}
	.isOver{
		width: 100%;
		height: 10px;
		line-height: 50px;
		text-align: center;
		font-size: 28rpx;
	}

</style>
