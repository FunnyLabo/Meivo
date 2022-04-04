<template>
	<div>
		<div>
			<div class="submenu">
				<div style="text-align:right;" class="mr-4">
					<a class="btn btn-success m-1 mt-2 mb-2" style="color:#fefefe;font-size:.9rem;" @click="doExcelOutPut">Excel出力</a>
					<a class="btn btn-light m-1  mt-2 mb-2" style="font-size:.9rem;" @click="doCsvOutPut">CSV出力</a>
				</div>
			</div>
		</div>

		<div class="sticky_total_table_wrapper">
			<table class="table table-sm sticky_table">
				<thead>
					<tr class="bg-cream">
						<th colspan="2" style="width: 50%;border-bottom:0px;text-align:center;border:0;font-size:11pt;">参加者</th>
						<th colspan="2" style="width: 50%;border-bottom:0px;text-align:center;border:0;font-size:11pt;">不参加者</th>
					</tr>
					<tr class="bg-cream2">
						<th  scope="col" style="width: 25%;border:0;font-size:11pt;">部署</th>
						<th  scope="col" style="width: 25%;border:0;font-size:11pt;">名前</th>
						<th  scope="col" style="width: 25%;border:0;font-size:11pt;">部署</th>
						<th  scope="col" style="width: 25%;border:0;font-size:11pt;">名前</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="(member,key) in editMembers" :key="key">
						<!-- 参加者一覧 -->
						<td scope="col" style="border-right:1px solid #ddd;font-size:11pt;">{{ member[0].dev }}</td>
						<td scope="col" style="font-size:11pt;">{{ member[0].name }}</td>
						<!-- 不参加者一覧 -->
						<td scope="col" style="border-right:1px solid #ddd;background:#eee;font-size:11pt;">{{ member[1].dev }}</td>
						<td scope="col" style="background:#eee;font-size:11pt;">{{ member[1].name }}</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
	
</template>
<script>
module.exports = {
	data: function() {
		return {
			members:[],
		};
	},
	methods:{
		doExcelOutPut:function(){
			axios.get('http://127.0.0.1:5000/api/excel_output',{
				dataType: "binary",
        		responseType: "blob"
			})
			.then(function (res) {
				let xlsx_file = res.data;
				let blob = new Blob([xlsx_file], {
					type:"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
				});
				let link = document.createElement("a");
				link.download = 'output.xlsx';
				link.href = window.URL.createObjectURL(blob);
				link.click();
				console.log("成功");
				console.log(res);
			});
		},
		doCsvOutPut:function(){
			axios.get('http://127.0.0.1:5000/api/csv_output',{
        		responseType: "blob"
			})
			.then(function (res) {
				let mineType = res.headers["content-type"];
				let csv_file = res.data
				const blob = new Blob([csv_file], {
					type:mineType
				});
				let link = document.createElement("a");
				link.download = 'output.csv';
				link.href = window.URL.createObjectURL(blob);
				link.click();
			});
		},
	},
	computed:{
		joinMembers:function(){
			return this.members.filter((value) => { return value.condition === "参加"})
		},
		notJoinMembers:function(){
			return this.members.filter((value) => { return value.condition === "不参加" || value.condition === "未定"})
		},
		editMembers:function(){
			let members = [];
			let maxCount = Math.max(this.joinMembers.length,this.notJoinMembers.length);
			for (let i =0;i<maxCount;i++){
				let member_set = [];
				member_set.push(i < this.joinMembers.length ? {'dev':this.joinMembers[i].dev,'name':this.joinMembers[i].name}:{'dev':'','name':''});
				member_set.push(i < this.notJoinMembers.length ? {'dev':this.notJoinMembers[i].dev,'name':this.notJoinMembers[i].name}:{'dev':'','name':''});
				members.push(member_set);
			}
			return members;
		},
	},
	created: function () {
		var self = this;
		axios.get('http://127.0.0.1:5000/api/members').then(function (res) {
			self.members = res.data.result.slice(1);
		});
	}
};
</script>