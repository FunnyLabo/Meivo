Vue.component('common-header', {
	template: `
	<div>
		<div class="app-title">
			<router-link  to="/">
				<h1 class="ml-1" style="display:inline-block;">meivo<span class="ml-2" style="font-size:.8rem;">-参加チェック用-</span></h1>
			</router-link>
			<!--<router-link style="display:inline-block;color:#54433a;font-size:.8rem;" class="ml-2" to="/">参加者一覧</router-link>-->
			<router-link style="display:inline-block;color:#54433a;font-size:.8rem;" class="ml-2" to="/result">※集計結果へ</router-link>
		</div>
	</div>
	`,
	delimiters: ['[[', ']]'],
	props: ['joinCount','filterdMembersLength'],

});