<template>
	<div>
		<div class="submenu">
			<common-search 
				:join-count="joinCount" 
				:filterd-members-length="filterdMembers.length"
				@do-change="updateSelectDev" 
				@do-input="updateName" />
		</div>

		<div class="sticky_table_wrapper bg-white2">
			<table class="table table-sm sticky_table">
				<thead>
					<tr class="bg-cream">
							<th scope="col" style="width: 30%;border:0;">部署</th>
							<th scope="col" style="width: 35%;border:0;">名前</th>
							<th scope="col" style="width: 35%;border:0;"></th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="member in filterdMembers" :key=member.id v-bind:style="{background:colorSelect(member.condition)}">
						<td>[[ member.dev ]]</td>
						<td>[[ member.name ]]</td>
						<td v-if="member.condition==='未定'" style="text-align:center;">
							<button class="btn btn-warning condition-btn" v-on:click="doJoin(member.id)">参加</button>
						</td>
						<td v-else-if="member.condition==='参加'" style="text-align:center;">
							<button class="btn btn-light condition-btn" v-on:click="doCancel(member.id)">キャンセル</button>
						</td>
						<td v-else-if="member.condition==='不参加'" style="text-align:center;">
							<button class="btn btn-warning condition-btn" v-on:click="doJoin(member.id)">参加</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>

	</div>
</template>
<script>
module.exports = {
	delimiters: ['[[', ']]'],
	data:function(){
		return{
			name:'',
			selectDev:'',
			members:[],
		};
	},
	methods:{
		colorSelect:function(condition){
			if(condition === "未定"){
				return "#fefefe";
			}else if(condition === "参加"){
				return "#eee";
			}else if(condition === "不参加"){
				return "#fefefe";
			}
		},
		doJoin:function(memberId){
			this.members[parseInt(memberId)-1].condition = "参加";
			axios.post('http://127.0.0.1:5000/api/mod_member',{
				memberId:memberId,
				condition:1
			},
			{
				headers:{
					'Content-Type':'application/json',
				}
			}).then((res) => {
				console.log(res.data);
			});
		},
		doCancel:function(memberId){
			this.members[parseInt(memberId)-1].condition = "不参加";
			axios.post('http://127.0.0.1:5000/api/mod_member',{
				memberId:memberId,
				condition:0
			},{
				headers:{
					'Content-Type':'application/json',
				}
			}).then((res) => {
				console.log(res.data);
			});
		},
		updateSelectDev:function(value){
			this.selectDev = value;
		},
		updateName:function(value){
			this.name = value;
		}
	},
	computed:{
		filterdMembers:function(){
			let members = [];
			this.members.filter((value) => { return value.dev === this.selectDev || this.selectDev.length <= 0 })
			.forEach((member) => {
				if(member.name.indexOf(this.name) !== -1){
					members.push(member);
				}
			});
			return members;
		},
		joinCount:function(){
			return this.filterdMembers.filter((value) => { return value.condition === "参加" }).length;
		}
	},
	created: function () {
		var self = this;
		axios.get('http://127.0.0.1:5000/api/members').then(function (res) {
			self.members = res.data.result.slice(1);
		});
	}
}
</script>