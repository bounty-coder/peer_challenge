// Given a set of n jobs where each jobi has a deadline and profit associated with it.
// Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with a job if and only if the job is completed by its deadline.
// Find the number of jobs done and the maximum profit.

// Input: Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
// Output: 2 60
// Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).

struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
};

bool jobPriority(Job a,Job b){
    return a.profit>b.profit;
}
vector<int> JobScheduling(Job arr[], int n) 
{ 
    sort(arr,arr+n,jobPriority); //sorting the arr in desc order by profit(so that we can take the bigger profit first)
    bool done[n]={0};  // initializing as 0, later will be filled with 1(if profit element found for that number
    int cnt=0,profit=0; 
    for(int i=0;i<n;i++){
        for(int j=arr[i].dead-1;j>=0;j--){  //need to complete the task at deadline or before it(so, start from deadline to 1) : -1 here yk that
            if(done[j]==0){  //if slot already not used
                done[j]=1;
                cnt++;
                profit+=arr[i].profit;
                break;
            }
        }
    }
    vector<int> result;
    result.push_back(cnt);
    result.push_back(profit);
    return result;
}
