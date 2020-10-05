<template>
	<view class="pics">
		<scroll-view class="left" scroll-y>
			<view 
			@click="leftClickHandle(index,item.id)"
			:class="active===index?'active':''" 
			v-for="(item,index) in cates" 
			:key="item.id">
			{{item.title}}</view>
		</scroll-view>
		<scroll-view class="right" scroll-y>
			<view class="item" v-for="item in secondData" :key="item.id">
				<image @click="previewImg(item.picurl)" :src="item.picurl"></image>
				<text>{{item.text}}</text>
			</view>
			<view v-if="secondData.length===0">暂无数据</view>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				cates:[],
				active:0,
				secondData:[]
			}
		},
		methods: {
			 async getPicsCate(){
				 const res = await this.$myRequest({
					url:'/getimgcategory/'
				})
				this.cates = res.data.message
				this.leftClickHandle(0,this.cates[0].id)
				// console.log(res)
			},
			async leftClickHandle(index,id){
				this.active=index
				//获取右侧的数据
				const res = await this.$myRequest({
					url:'/getimg/'+id
				})
				this.secondData = res.data.message
				console.log(res)
			},
			//预览照片
			previewImg(current){
				const urls = this.secondData.map(item=>{
					return item.picurl
				})
				uni.previewImage({
					current,
					urls,
					
				})
			}
			
		},
		onLoad() {
			this.getPicsCate()
		}
	}
</script>

<style lang="scss">
	page{
		height: 100%;
	}
	.pics{
		height: 100%;
		display: flex;
		.left{
			width: 200rpx;
			height: 100%;
			border-right:1px solid #eee ;
		}
		view{
			height: 60px;
			line-height: 60px;
			color: #333;
			text-align: center;
			font-size: 30rpx;
			border-top: 1px solid #eee;
		}
		.active{
			background: $shop-color;
			color: #fff;
		}
		.right{
			height: 100%;
			width: 528rpx;
			margin: 0 auto;
			.item{
				image{
					width: 520rpx;
					height: 520rpx;
					border-radius: 5px;
				}
				text{
					font-size: 30rpx;
					line-height: 60rpx;
				}
			}
		}
	}

</style>
