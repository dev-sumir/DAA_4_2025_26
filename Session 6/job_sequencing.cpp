class Solution {
  public:
    
    int find(int x,vector<int> &parent){
        if(parent[x]==x)
            return x;
        return parent[x]=find(parent[x],parent);
    }
    
    vector<int> jobSequencing(vector<int> &deadline, vector<int> &profit) {
        int size=profit.size();
        
        vector<pair<int,int>> jobs;
        for(int i=0;i<size;i++){
            jobs.push_back({profit[i],deadline[i]});
        }
        
        sort(jobs.begin(),jobs.end(),greater<>());
        
        int max=0;
        for(int i=0;i<size;i++){
            if(max<jobs[i].second){
                max=jobs[i].second;
            }
        }
        
        vector<int> parent(max+1);
        for(int i=0;i<=max;i++){
            parent[i]=i;
        }
        
        int total=0;
        int count=0;
        
        for(int i=0;i<size;i++){
            int available=find(jobs[i].second,parent);
            if(available>0){
                parent[available]=find(available-1,parent);
                total+=jobs[i].first;
                count++;
            }
        }
        
        return {count, total};
    }
};
