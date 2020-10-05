<template>
	<view>
		<view class="news_item" @click="navigator(item.id)" v-for="(item,index) in list" :key="index">
			<image :src="item.imgurl"></image>
			<view class="right">
				<view class="tit">{{item.title}}</view>
				<view class="info">
					<text>发表时间：{{item.addtime | formatDate}}</text>
					<text>浏览：{{item.click}}</text>
				</view>
			</view>
		</view>
	</view>
	
</template>

<script>
	export default{
		props:['list'],
		filters:{
			formatDate(data){
				console.log(data)
				const newDate = new Date(data)
				const year = newDate.getFullYear()
				const monty = newDate.getMonth().toString().padStart(2,0)
				const day = newDate.getDay().toString().padStart(2,0)
				return year+'-'+monty+'-'+day
			}
		},
		methods:{
			navigator(id){
				this.$emit('itemClick',id)
			}
		}
	}
	
</script>

<style lang="scss">
	.news_item{
		display: flex;
		padding: 10rpx 20rpx;
		border-bottom: 1px solid $shop-color;
		image{
			min-width: 200rpx;
			max-width: 200rpx;
			height: 150rpx;
		}
		.right{
			margin-left:15rpx ;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			.tit{
				font-size: 30rpx;
				
			}
			.info{
				font-size: 24rpx;
				text:nth-child(2){
					margin-left: 30rpx;
				}
			}
		}
		
	}
</style>
