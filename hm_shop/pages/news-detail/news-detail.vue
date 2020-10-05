<template>
	<view class="news_detail">
		<view class="title">{{detail.title}}</view>
		<view class="info">
			<text>发表时间：{{detail.add_time | formatDate}}</text>
			<text>浏览：{{detail.click}}</text>
		</view>
		<view class="content">
		<rich-text :nodes="detail.content"></rich-text></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id:0,
				detail:{}
			}
		},
		methods: {
			async getNewsDetail(){
			const res = await	this.$myRequest({
					url:'/getdetail/'+this.id
				})
			console.log(res)
			this.detail = res.data.message[0]
			}
		},
		onLoad(options) {
			console.log(options)
			this.id = options.id
			this.getNewsDetail()
		}
	}
</script>

<style lang="scss">
	.news_detail{
		font-size: 30rpx;
		padding: 0 20rpx;
		.title{
			width: 710rpx;
			text-align: center;
			display: block;
			margin: 20rpx 0;
		}
		.info{
			display: flex;
			justify-content: space-between;
		}
	}

</style>
