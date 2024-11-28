#include <unordered_map>
#include <string>
#include <vector>
 
using namespace std;
 
unordered_map<string, int> prs[1005];
unordered_map<string, vector<int>> group[105];
 
void init()
{
    for (int i = 0; i < 1005; ++i) prs[i].clear();
    for (int i = 0; i < 105; ++i) group[i].clear();
}
 
void addEvent(int uid, char ename[], int groupid)
{
    ++uid;
    ++groupid;
    string vl(ename);
 
    prs[uid].insert({ vl, groupid });
    group[groupid][vl].push_back(uid);
}
 
int deleteEvent(int uid, char ename[])
{
    int ans;
    ++uid;
    string vl(ename);
    int groupid = prs[uid][vl];
 
    auto res = group[groupid][vl];
     
    int i;
    for (i = 0; i < res.size(); ++i) {
        if (res[i] == uid) break;
    }
    if (i == 0) {       //master면
        ans = res.size();
        for (int j = 0; j < res.size(); ++j) {
            prs[res[j]].erase(vl);
        }
        group[groupid][vl].clear();
 
    }
    else {
        ans = 1;
        prs[uid].erase(vl);
        group[groupid][vl].erase(group[groupid][vl].begin() + i);
    }
    return ans;
}
 
int changeEvent(int uid, char ename[], char cname[])
{
    int ans;
    ++uid;
    string vl(ename);
    string ch_vl(cname);
    int groupid = prs[uid][vl];
 
    auto res = group[groupid][vl];
 
    int i = 0;
    for (i = 0; i < res.size(); ++i) {
        if (res[i] == uid) break;
    }
    if (i == 0) {
        ans = res.size();
        for (int j = 0; j < res.size(); ++j) {
            prs[res[j]].erase(vl);
            prs[res[j]].insert({ ch_vl, groupid });
            group[groupid][ch_vl].push_back(res[j]);
        }
        group[groupid][vl].clear();
    }
    else {
        ans = 1;
        prs[uid].erase(vl);
        prs[uid].insert({ ch_vl, groupid });
        group[groupid][vl].erase(group[groupid][vl].begin() + i);
        group[groupid][ch_vl].push_back(uid);
    }
    return ans;
}
 
int getCount(int uid)
{
    ++uid;
    return prs[uid].size();
}