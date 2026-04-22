class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> res;

    for (string s : strs){
        vector<int> count(26, 0);
        for (char ch : s){
            count[ch - 'a']++;
        }
        string key = to_string(count[0]);
        for (int i : count){
            key += ',' + to_string(i);
        }
        res[key].push_back(s);
    }
    
    vector<vector<string>> result;
    for (const auto& pair : res){
        result.push_back(pair.second);
    }

    return result;        
    }
};
