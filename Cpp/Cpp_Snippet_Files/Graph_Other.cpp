vi toposort(vii graph){
	vi res;
	vi found(graph.size(),0);
	vi st;
	for(int i=0;i<len(graph);i++){
		st.pb(i);
	}
	while(!st.empty()){
		int node = st.back();
		st.pop_back();
		if(node<0){
			res.pb(~node);
		}
		else if(!found[node]){
			found[node] = 1;
			st.pb(~node);
			for (auto j:graph[node]){
				st.pb(j);
			}
		}
	}
	return res;
}
