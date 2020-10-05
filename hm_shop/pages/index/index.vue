<template>
	<view >
		<view class="home">
			<swiper class="swiper" indicator-dots="true" indicator-color="white" indicator-active-color="red" autoplay="true" :interval = "timeout">
				<swiper-item  v-for="item in  swipers" :key="item.id">
					<image class="image" :src="item.picurl"></image>
				</swiper-item>
			</swiper>
			<!-- 导航区域 -->
			<view class ="nav">
				<view class="nav_item" v-for="(item,index) in navs" :key="index" @click="navItemClick(item.path)">
					<view :class="item.icon"></view>
					<text >{{item.title}}</text>
				</view>
			</view>
			<!-- 推荐商品 -->
			<view class="hot_goods">
				<view class="tit">推荐商品</view>
				<goods-list :goods="goods" @goodsItemClick="goGoodsDetail"></goods-list>
			</view>
			
		</view>
	</view>
</template>

<script>
	import goodsList from '../../template/goods-list/goods-list.vue'
	export default {
		data() {
			return {
				swipers:[],
				timeout:'',
				navs:[
					{
						icon:'iconfont icon-Auchanmarket',
						title:'黑马超市',
						path:"/pages/goods/goods"
					},
					{
						icon:'iconfont icon-lianxiwomen',
						title:'联系我们',
						path:"/pages/contact/contact"
					},
					{
						icon:'iconfont icon-shequn',
						title:'社区图片',
						path:"/pages/pics/pics"
					},
					{
						icon:'iconfont icon-shipin',
						title:'学习视频',
						path:"/pages/video/video"
					},
				],
				goods:[]
			}
		},
		onLoad() {
			this.getSwipers()
			this.getHotGoods()
		},
		components:{
			"goods-list":goodsList
		},
		methods: {
			//获取轮播图的数据
			async getSwipers(){
				// console.log("获取轮播图的数据");
				// uni.request({
				// 	url:"http://127.0.0.1:8808/getlunbo",
				// 	method:'GET',
				// 	success:(res)=>{
				// 		console.log('调用成功',res)
				// 		// if (res.data.status !==0){
				// 		// 	return uni.showToast({
				// 		// 		title: '网络连接失败'
				// 		// 	});
				// 		// }
				// 		this.swipers = res.data.message
				// 	},
				// 	fail: (res) => {
				// 		console.log("调用接口失败：",res)
						
				// 	}
				// })
				const res = await this.$myRequest({
					url:'/getlunbo'
				})
				this.swipers = res.data.swiper
				this.timeout = res.data.timeout
			},
			// 获取热门商品列表数据
			async getHotGoods(){
				const res = await this.$myRequest({
					url:'/gethotgoods/1'
				})
				this.goods = res.data.message
				console.log(this.goods)
			},
			//导航点击的处理函数
			navItemClick(url){
				console.log(url)
				uni.navigateTo({
					url:url
				})
				console.log("跳转")
			},
			//导航到商品详情页面
			goGoodsDetail(id){
				uni.navigateTo({
					url:'/pages/goods-detail/goods-detail?id='+id
				})
			}
			
		}
	}
</script>

<style lang="scss">
 	.home  {
	}
	.swiper{
		width:750rpx;
		height:380rpx;
	}
	.image{
		height: 100%;
		width: 100%;
	}
	.nav{
		display: flex;
		.nav_item{
			width: 25%;
			text-align: center;
			view {
				width:120rpx;
				height: 120rpx;
				background:$shop-color ;
				border-radius: 60rpx;
				margin: 10rpx auto;
				line-height: 120rpx;
				color: #fff;
				font-size: 80rpx;
			}
			.icon-Auchanmarket{
				font-size: 100rpx;
			}
			.icon-shequn{
				font-size: 100rpx;
			}
			.icon-shipin{
				font-size: 60rpx;
			}
			text{
				font-size: 30rpx;
			}
		}
	}
	.hot_goods{
		background: #eee;
		overflow: hidden;
		margin-top: 10rpx;
		.tit{
			height: 50px;
			line-height: 50px;
			color: $shop-color;
			text-align: center;
			letter-spacing: 20rpx;
			background: #fff;
			margin: 7rpx 0;
		}

	}
	
	/* .text{
		font-size: 30rpx;
	}
	
	.nav_item view{
		width:120rpx;
	} */
</style>
