class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums){
            count[num]++;
        }
        
        vector<vector<int>> arr;
        for (const auto& p : count){
            arr.push_back({p.second, p.first});
        }
        
        sort(arr.rbegin(), arr.rend());
        vector<int> res;
        for (const auto& v : arr){
            res.push_back(v[1]);
            if (res.size() == k) {
                return res;
            }
        }



        
    }
};
