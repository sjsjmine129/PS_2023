#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

unordered_map<string, int> userEvents[2000];
unordered_map<string, vector<int>> eventGroups[200];

void init(){
    for (int i = 0; i < 2000; ++i){
        userEvents[i].clear();
    }
    for (int i = 0; i < 105; ++i){
        eventGroups[i].clear();
    }
}

void addEvent(int uid, char ename[], int groupid){
    string event(ename);

    userEvents[uid+1].insert({ event, groupid+1 });
    eventGroups[groupid+1][event].push_back(uid+1);
}

int deleteEvent(int uid, char ename[]){
    string event(ename);
    int groupId = userEvents[uid+1][event];

    auto participants = eventGroups[groupId][event];

    int i = 0;
    for (i = 0; i < participants.size(); ++i) {
        if (participants[i] == uid+1) break;
    }
    if (i == 0) {
        for (int j = 0; j < participants.size(); ++j) {
            userEvents[participants[j]].erase(event);
        }
        eventGroups[groupId][event].clear();
        return participants.size();
    }
    else {
        userEvents[uid+1].erase(event);
        eventGroups[groupId][event].erase(eventGroups[groupId][event].begin() + i);
        return 1;
    }
}

int changeEvent(int uid, char ename[], char cname[]){
    string event(ename);
    string newEvent(cname);
    int groupId = userEvents[uid+1][event];

    auto participants = eventGroups[groupId][event];

    int i = 0;
    for (i = 0; i < participants.size(); ++i) {
        if (participants[i] == uid+1) break;
    }
    if (i == 0) {
        for (int j = 0; j < participants.size(); ++j) {
            userEvents[participants[j]].erase(event);
            userEvents[participants[j]].insert({ newEvent, groupId });
            eventGroups[groupId][newEvent].push_back(participants[j]);
        }
        eventGroups[groupId][event].clear();
        return participants.size();
    }
    else {
        userEvents[uid+1].erase(event);
        userEvents[uid+1].insert({ newEvent, groupId });
        eventGroups[groupId][event].erase(eventGroups[groupId][event].begin() + i);
        eventGroups[groupId][newEvent].push_back(uid+1);
        return 1;
    }
}

int getCount(int uid){
    return userEvents[uid+1].size();
}
