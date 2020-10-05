<template>
	<view class="contact">
		<image class="img" src ="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601455382338&di=e71bdfd739bcb6517a5d54358ab9f632&imgtype=0&src=http%3A%2F%2Fsc.admin5.com%2Fuploads%2F150908%2F764-150ZQ455332O.jpg"></image>
		<view class="info">
			<view @click="phone">联系电话：176-0326-7574(点击拨打)</view>
			<view>联系地址：天为被-地为床-四海为家</view>
		</view>
		<map class="map" :longitude="longitude" :scale="scale" :latitude="latitude" :markers="markers"></map>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				longitude:121.23704,
				latitude:31.060041,
				scale:13,
				markers:[{
					longitude:121.23704,
					latitude:31.060041,
					iconPath:'../../static/log.png',
					width:30,
					height:30
				}]
			}
		},
		methods: {
			phone(){
				uni.makePhoneCall({
					phoneNumber:'17603267574'
				})
			}
		}
	}
</script>

<style lang="scss">
	.contact{
		.img{
			width: 750rpx;
			height: 320rpx;
		}
		.info{
			padding: 10rpx 20rpx;
			font-size: 30rpx;
			view{
				line-height: 80rpx;
				border-bottom: 1px solid #eee ;
			}
		}
		.map{
			width: 750rpx;
			height: 750rpx;
		}
	}

</style>
