<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	@font-face {font-family: "iconfont";
	  src: url('~@/static/font/iconfont.eot?t=1601375295065'); /* IE9 */
	  src: url('~@/static/font/iconfont.eot?t=1601375295065#iefix') format('embedded-opentype'), /* IE6-IE8 */
	  url('data:application/x-font-woff2;charset=utf-8;base64,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') format('woff2'),
	  url('~@/static/font/iconfont.woff?t=1601375295065') format('woff'),
	  url('~@/static/font/iconfont.ttf?t=1601375295065') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
	  url('~@/static/font/iconfont.svg?t=1601375295065#iconfont') format('svg'); /* iOS 4.1- */
	}
	
	.iconfont {
	  font-family: "iconfont" !important;
	  font-size: 16px;
	  font-style: normal;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	}
	
	.icon-shipin:before {
	  content: "\e6c1";
	}
	
	.icon-Auchanmarket:before {
	  content: "\e61a";
	}
	
	.icon-shequn:before {
	  content: "\e609";
	}
	
	.icon-lianxiwomen:before {
	  content: "\e612";
	}
	

</style>
