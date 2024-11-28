#include <vector>
#include <unordered_map>
#include <cstring>
#include <algorithm>  // For std::remove_if

struct Event {
    char ename[16]; // Maximum length 15 + '\0'
    int uid;
    bool isMaster;
};

std::unordered_map<int, std::vector<Event>> groupEvents; // Group ID -> Events
std::unordered_map<int, std::vector<Event>> userEvents;  // User ID -> Events

void init() {
    groupEvents.clear();
    userEvents.clear();
}

// Utility function to find the group ID of an event by a user
int findGroupId(int uid, const char ename[]) {
    for (const auto& [groupId, events] : groupEvents) {
        for (const auto& event : events) {
            if (event.uid == uid && strcmp(event.ename, ename) == 0) {
                return groupId;
            }
        }
    }
    return -1; // Not found
}

void addEvent(int uid, char ename[], int groupid) {
    Event newEvent;
    strcpy(newEvent.ename, ename);
    newEvent.uid = uid;
    newEvent.isMaster = true;

    // Check if the event already exists in the group
    for (const auto& event : groupEvents[groupid]) {
        if (strcmp(event.ename, ename) == 0) {
            newEvent.isMaster = false;  // Set to normal if the name exists
            break;
        }
    }

    // Add to group and user structures
    groupEvents[groupid].push_back(newEvent);
    userEvents[uid].push_back(newEvent);
}

int deleteEvent(int uid, char ename[]) {
    int deleteCount = 0;
    int groupid = findGroupId(uid, ename);

    if (groupid == -1) return 0; // Event not found

    auto& events = groupEvents[groupid];
    bool isMaster = false;

    // Find the event and check its state
    for (auto it = events.begin(); it != events.end(); ++it) {
        if (it->uid == uid && strcmp(it->ename, ename) == 0) {
            isMaster = it->isMaster;
            break;
        }
    }

    // Remove events with matching names (if master, remove all)
    events.erase(std::remove_if(events.begin(), events.end(), [&](const Event &e) {
        if (strcmp(e.ename, ename) == 0 && (isMaster || e.uid == uid)) {
            deleteCount++;
            return true;
        }
        return false;
    }), events.end());

    // Also remove from the user's event list
    auto& userEvts = userEvents[uid];
    userEvts.erase(std::remove_if(userEvts.begin(), userEvts.end(), [&](const Event &e) {
        return strcmp(e.ename, ename) == 0;
    }), userEvts.end());

    return deleteCount;
}

int changeEvent(int uid, char ename[], char cname[]) {
    int changeCount = 0;
    int groupid = findGroupId(uid, ename);

    if (groupid == -1) return 0; // Event not found

    auto& events = groupEvents[groupid];
    bool isMaster = false;

    // Identify if the event to change is master
    for (const auto& event : events) {
        if (event.uid == uid && strcmp(event.ename, ename) == 0) {
            isMaster = event.isMaster;
            break;
        }
    }

    // Modify all matching events if master
    for (auto& event : events) {
        if (strcmp(event.ename, ename) == 0 && (isMaster || event.uid == uid)) {
            strcpy(event.ename, cname);
            changeCount++;
            if (!isMaster) event.isMaster = true; // Promote to master
        }
    }

    // Update user's event list
    auto& userEvts = userEvents[uid];
    for (auto& event : userEvts) {
        if (strcmp(event.ename, ename) == 0) {
            strcpy(event.ename, cname);
            break;
        }
    }

    return changeCount;
}

int getCount(int uid) {
    return userEvents[uid].size();  // Number of events for the user
}
