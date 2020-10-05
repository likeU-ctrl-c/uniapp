<template>
	<view class="goods_detail">
			<swiper indicator-dots>
				<swiper-item v-for="(item,index) in swipers" :key = "index" >
					<image :src="item"></image>
				</swiper-item>
			</swiper>
			<view class="box1">
				<view class="price">
					<text>{{info.sell_price}}</text>
					<text>{{info.make_price}}</text>
				</view>
				<view class="goods_name">{{info.title}}</view>
			</view>
			<view class="line"></view>
			<view class="box2">
				<view>货号：{{info.huohao}}</view>
				<view>库存：{{info.kucun}}</view>
			</view>
			<view class="line"></view>
			<view class="box3">
				<view class="tit">详情介绍</view>
				<view class="content">
					<rich-text>
						{{info.zhaiyao}}
					</rich-text>
				
				</view>
			</view>
			<view class="goods_nav">
				<uni-goods-nav :fill="true"  :options="options" :buttonGroup="buttonGroup"  @click="onClick" @buttonClick="buttonClick" />
				
			</view>
				</view>
</template>

<script>
	import uniGoodsNav from '@/components/uni-goods-nav/uni-goods-nav.vue'
	export default {
		data() {
			return {
				id:0,
				swipers:[],
				info:{},
				options: [{
				            icon: 'headphones',
				            text: '客服'
				        }, {
				            icon: 'shop',
				            text: '店铺',
				            info: 2,
				            infoBackgroundColor:'#007aff',
				            infoColor:"red"
				        }, {
				            icon: 'cart',
				            text: '购物车',
				            info: 2
				        }],
				        buttonGroup: [{
				          text: '加入购物车',
				          backgroundColor: '#ff0000',
				          color: '#fff'
				        },
				        {
				          text: '立即购买',
				          backgroundColor: '#ffa200',
				          color: '#fff'
				        }
				        ]
			}
		},
		methods: {
			async getSwipers(){
				const res = await this.$myRequest({
					url:'/getSwiper/'+this.id
				})
				console.log(res)
				this.swipers = res.data.message[this.id].picurl
				console.log(this.swipers)
			},
			async getDetailInfo(){
			const res = await this.$myRequest({
					url:'/getgoodsInfo/'+this.id
				})
				console.log(res)
				this.info =  res.data
			},
			onClick (e) {
					uni.showToast({
					  title: `点击${e.content.text}`,
					  icon: 'none'
					})
			},
			buttonClick (e) {
				console.log(e)
				if (e.index ==1){
					this.options[2].info--
				}else{
					this.options[2].info++
				}
					
			}
		},
		onLoad(options) {
			console.log(options)
			this.id = options.id
			this.getSwipers()
			this.getDetailInfo()
		},
		components: {uniGoodsNav}
	}
</script>

<style lang="scss">
	.line{
		height: 10rpx;
		width: 750rpx;
		background-color: #eee;
	}
	.goods_detail{
		swiper{
			height: 700rpx;
			image{
				width: 100%;
				height: 100%;
			}
		}
		.box1{
			padding: 10px;
			.price{
				font-size: 35rpx;
				color: $shop-color;
				line-height: 80rpx;
				text:nth-child(2){
					color: #ccc;
					font-size: 28rpx;
					text-decoration: line-through;
					margin-left: 20rpx;
				}
			}
			.goods_name{
				font-size: 32rpx;
				line-height: 60rpx;
			}
		}
		.box2{
				padding: 0 10px;
				font-size: 32rpx;
				line-height: 70rpx;
		}
		.goods_nav{
			position: fixed;
			bottom: 0;
			width: 100%;
		}
		.box3{
			padding-bottom: 50rpx;
			.tit{
				font-size: 32rpx;
				padding-left: 10px;
				border-bottom: 1px solid #eee;
				line-height: 70rpx;
			}
			.content{
				padding: 10px;
				font-size: 28rpx;
				color: #333;
				line-height: 50rpx;
			}
		}
	}
</style>
