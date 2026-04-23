class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";

        for (const string& s : strs){
            res = res + to_string(s.size()) + '#' + s;
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.size()){
            int j = i;
            while (s[j] != '#'){
                j++;
            }
            int length_of_string = stoi(s.substr(i, j-i));

            i = j + 1;
            string res = s.substr(i, length_of_string);
            result.push_back(res);
            i = i + length_of_string;
            

        }

        return result;
    }
};
