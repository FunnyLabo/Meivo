Vue.component('common-search', {
	template: `
	<div>
		<div class="d-flex select-content pb-1 mt-3 pl-3">
			<select class="flex-fill form-select" style="border:1px solid #ccc;" aria-label="部署選択" @change="doChange">
				<option value="" disabled selected style="display:none;">部署を選択</option>
				<option v-for="value in devList">[[ value ]]</option>
			</select>
			<div class="flex-fill"></div>
			<div class="flex-fill form-group mb-0 ml-auto mr-3" >
				<input type="text" class="form-control" placeholder="名前検索" @input="doInput">
			</div>
		</div>
		<p style="text-align:right;margin:0 17px 0 0;color:#333;font-size:.75rem;">※参加割合：[[ joinCount ]]/[[ filterdMembersLength ]]</p>
	</div>
	`,
	delimiters: ['[[', ']]'],
	props: ['joinCount','filterdMembersLength'],
	data:function(){
		return{
			devList:[],
		};
    },
	methods:{
		doChange(e){
			this.$emit('do-change', e.target.value)
		},
		doInput(e){
			this.$emit('do-input', e.target.value)
		}
	},
	created: function () {
		var self = this;
		axios.get('http://127.0.0.1:5000/api/departments').then(function (res) {
			console.log(res.data.result)
			self.devList = res.data.result;
		});
	},
});