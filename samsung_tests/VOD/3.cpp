#define MAX_N 20000
#define MAX_M 128
#define MAX_BLOCKCOUNT 1250
#define MAX_DATALENGTH 5120000
#define FRAMESIZE 256

struct huffman {
    int symbol, codeword, codewordLength;
};

// Global variables
unsigned char* encodedData[MAX_BLOCKCOUNT];
bool blockVisited[MAX_BLOCKCOUNT];
int totalFrames, totalBlocks, currentFrame, currentBlockIndex;
int trie[21 * MAX_M + 5][2], trieNodeCount, symbolMap[21 * MAX_M + 5];
unsigned char decodedData[MAX_BLOCKCOUNT * 4096];

// Helper function to reset the trie structure
void resetTrie() {
    for (int i = 0; i <= trieNodeCount; i++) {
        trie[i][0] = trie[i][1] = 0;
        symbolMap[i] = 0;
    }
    trieNodeCount = 0;
}

// Helper function to build the Huffman trie
void buildTrie(int M, struct huffman* code) {
    for (int i = 0; i < M; i++) {
        int currentNode = 0;
        for (int bitIndex = code[i].codewordLength - 1; bitIndex >= 0; bitIndex--) {
            int bit = (code[i].codeword >> bitIndex) & 1;
            if (!trie[currentNode][bit])
                trie[currentNode][bit] = ++trieNodeCount;
            currentNode = trie[currentNode][bit];
        }
        symbolMap[currentNode] = code[i].symbol;
    }
}

// Initialize function
void Init(int N, int* size, unsigned char* data, int M, struct huffman* code) {
    totalFrames = N;
    totalBlocks = N >> 4;

    unsigned char* dataPointer = data;
    for (int i = 0; i < totalBlocks; i++) {
        encodedData[i] = dataPointer;
        blockVisited[i] = false;
        dataPointer += size[i];
    }

    resetTrie();
    buildTrie(M, code);
}

// Decode a block if it hasn't been decoded yet
void decodeCurrentBlock() {
    if (blockVisited[currentBlockIndex]) return;
    
    blockVisited[currentBlockIndex] = true;
    unsigned char* encodedBlock = encodedData[currentBlockIndex];
    
    for (int i = 0, currentNode = 0; i < 4096;) {
        for (int bitPos = 7; bitPos >= 0; bitPos--) {
            int bit = ((*encodedBlock) >> bitPos) & 1;
            currentNode = trie[currentNode][bit];
            if (symbolMap[currentNode]) {
                decodedData[currentBlockIndex * 4096 + i++] = symbolMap[currentNode];
                currentNode = 0;
                if (i == 4096) break;
            }
        }
        encodedBlock++;
    }

    // Apply delta decoding for data after the first 256 bytes
    for (int i = 256; i < 4096; i++) {
        decodedData[currentBlockIndex * 4096 + i] += decodedData[currentBlockIndex * 4096 + i - 256] - 128;
    }
}

// Move to a specific frame
void Goto(int frame) {
    currentFrame = frame;
}

// Update the screen and move to the next frame
int Tick(unsigned char* screen) {
    currentBlockIndex = currentFrame >> 4;
    decodeCurrentBlock();

    // Copy decoded data to the screen buffer
    for (int i = 0; i < FRAMESIZE; i++) {
        screen[i] = decodedData[currentFrame * FRAMESIZE + i];
    }

    return (currentFrame == totalFrames - 1) ? currentFrame : currentFrame++;
}
