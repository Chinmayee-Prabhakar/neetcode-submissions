class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int sub = target - nums[i];
            if (seen.find(sub) != seen.end()){
                return {seen[sub], i};
            }
            seen[nums[i]] = i;
        }

        return {};
        
    }
};
