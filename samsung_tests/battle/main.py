# define MAX_N 20

int N
int map[MAX_N][MAX_N]

// Stores structure configurations and checks for placement validity.
void init(int size, int mMap[MAX_N][MAX_N]) {
    N = size
    for (int i=0
         i < N
         + +i)
    for (int j=0
         j < N
         + +j)
    map[i][j] = mMap[i][j]
}

// Helper to check if structure placement is valid.
bool isValidPlacement(int row, int col, int M, int structure[5], int rotation) {
    int dr[4][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}}
    int dc[4][5] = {{0, 1, 2, 3, 4}, {0, 0, 0, 0, 0}, {0, -1, -2, -3, -4}, {0, 0, 0, 0, 0}}

    int newHeight = map[row][col] + structure[0]
    // Target height.

    for (int i=0
         i < M
         + +i) {
        int nr = row + dr[rotation][i]
        int nc = col + dc[rotation][i]
        if (nr < 0 | | nc < 0 | | nr >= N | | nc >= N) return false
        // Boundary check.
        if (map[nr][nc] + structure[i] != newHeight) return false
        // Height uniformity check.
    }
    return true
}

int numberOfCandidate(int M, int mStructure[5]) {
    int count = 0
    for (int rot=0
         rot < 4
+ +rot) {// 0, 90, 180, 270 degrees.
          for (int i = 0
              i < N
              + +i) {
             for (int j=0
                   j < N
                   + +j) {
                  if (isValidPlacement(i, j, M, mStructure, rot))
                 count++
              }
             }
          }
    return count
}

// Flood simulation and counting dry land.
void floodMap(int mSeaLevel, int tempMap[MAX_N][MAX_N]) {
    bool visited[MAX_N][MAX_N] = {false}
    for (int i=0
         i < N
         + +i) {
        for (int j=0
             j < N
             + +j) {
            if (tempMap[i][j] < mSeaLevel) {
                tempMap[i][j] = -1
                // Mark flooded areas.
            }
        }
    }
}

// Calculate max dry land areas.
int maxArea(int M, int mStructure[5], int mSeaLevel) {
    int maxDryLand = -1

    for (int rot=0
         rot < 4
+ +rot) {// Try all rotations.
          for (int i = 0
              i < N
              + +i) {
             for (int j=0
                   j < N
                   + +j) {
                  if (isValidPlacement(i, j, M, mStructure, rot)) {
                     int tempMap[MAX_N][MAX_N]
                     for (int r=0
                          r < N
                          + +r)
                     for (int c=0
                          c < N
                          + +c)
                     tempMap[r][c] = map[r][c]

                     floodMap(mSeaLevel, tempMap)

                     // Count the largest connected dry area.
                     int dryCount = 0
                     for (int x=0
                          x < N
                          + +x) {
                         for (int y=0
                              y < N
                              + +y) {
                             if (tempMap[x][y] >= mSeaLevel) {
                                 dryCount++
                             }
                         }
                          }
                     if (dryCount > maxDryLand) {
                         maxDryLand = dryCount
                          }
                     }
              }
             }
          }
    return maxDryLand
}
