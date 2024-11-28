#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

unordered_map<string, int> userEvents[1005];
unordered_map<string, vector<int>> eventGroups[105];

void init(){
    for (int i = 0; i < 1005; ++i) userEvents[i].clear();
    for (int i = 0; i < 105; ++i) eventGroups[i].clear();
}

void addEvent(int uid, char ename[], int groupid){
    ++uid;
    ++groupid;
    string event(ename);

    userEvents[uid].insert({ event, groupid });
    eventGroups[groupid][event].push_back(uid);
}

int deleteEvent(int uid, char ename[]){
    int result;
    ++uid;
    string event(ename);
    int groupId = userEvents[uid][event];

    auto participants = eventGroups[groupId][event];

    int i;
    for (i = 0; i < participants.size(); ++i) {
        if (participants[i] == uid) break;
    }
    if (i == 0) {  // if master
        result = participants.size();
        for (int j = 0; j < participants.size(); ++j) {
            userEvents[participants[j]].erase(event);
        }
        eventGroups[groupId][event].clear();
    }
    else {
        result = 1;
        userEvents[uid].erase(event);
        eventGroups[groupId][event].erase(eventGroups[groupId][event].begin() + i);
    }
    return result;
}

int changeEvent(int uid, char ename[], char cname[]){
    int result;
    ++uid;
    string event(ename);
    string newEvent(cname);
    int groupId = userEvents[uid][event];

    auto participants = eventGroups[groupId][event];

    int i = 0;
    for (i = 0; i < participants.size(); ++i) {
        if (participants[i] == uid) break;
    }
    if (i == 0) {
        result = participants.size();
        for (int j = 0; j < participants.size(); ++j) {
            userEvents[participants[j]].erase(event);
            userEvents[participants[j]].insert({ newEvent, groupId });
            eventGroups[groupId][newEvent].push_back(participants[j]);
        }
        eventGroups[groupId][event].clear();
    }
    else {
        result = 1;
        userEvents[uid].erase(event);
        userEvents[uid].insert({ newEvent, groupId });
        eventGroups[groupId][event].erase(eventGroups[groupId][event].begin() + i);
        eventGroups[groupId][newEvent].push_back(uid);
    }
    return result;
}

int getCount(int uid){
    ++uid;
    return userEvents[uid].size();
}
