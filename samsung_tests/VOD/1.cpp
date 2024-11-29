#define MAX_N               20000
#define MAX_M               128
#define MAX_BLOCKCOUNT      1250
#define MAX_DATALENGTH      5120000
#define FRAMESIZE           256
 
struct huffman {
    int symbol, codeword, codewordLength;
};
 
const int TRIE_SIZE = 21 * MAX_M + 5;
 
int numFrame, numBlock;
int currFrame, currBlock;
int trie[TRIE_SIZE][2], trie_size, sym[TRIE_SIZE];
 
unsigned char* encoded[MAX_BLOCKCOUNT];
unsigned char decoded[MAX_BLOCKCOUNT * 4096];
bool vis[MAX_BLOCKCOUNT];
 
void Init(int N, int* size, unsigned char* data, int M, struct huffman* code)
{
    numFrame = N;
    numBlock = N >> 4;
     
    auto p = data;
    for (int i = 0; i < numBlock; i++) {
        encoded[i] = p;
        vis[i] = 0;
        p += size[i];
    }
 
    for (int i = 0; i <= trie_size; i++) {
        trie[i][0] = trie[i][1] = sym[i] = 0;
    }
 
    trie_size = 0;
    for (int i = 0; i < M; i++) {
        int curr = 0;
        for (int j = code[i].codewordLength - 1; j >= 0; j--) {
            int x = (code[i].codeword >> j) & 1;
            if (!trie[curr][x])
                trie[curr][x] = ++trie_size;
            curr = trie[curr][x];
        }
        sym[curr] = code[i].symbol;
    }
}
 
void Goto(int frame) {
    currFrame = frame;
}
 
int Tick(unsigned char* screen) {
    currBlock = currFrame >> 4;
 
    if (vis[currBlock] == false) {
        vis[currBlock] = true;
        auto encodedBlock = encoded[currBlock];
        for (int i = 0, curr = 0; i < 4096; ) {
            for (int j = 7; j >= 0; j--) {
                int x = ((*encodedBlock) >> j) & 1;
                curr = trie[curr][x];
                if (sym[curr]) {
                    decoded[currBlock * 4096 + i++] = sym[curr];
                    curr = 0;
                    if (i == 4096)
                        break;
                }
            }
            encodedBlock++;
        }
        for (int i = 256; i < 4096; i++) {
            decoded[currBlock * 4096 + i] += decoded[currBlock * 4096 + i - 256] - 128;
        }
    }
    for (int i = 0; i < 256; i++) {
        screen[i] = decoded[currFrame * 256 + i];
    }
 
    return (currFrame == numFrame - 1) ? currFrame : currFrame++;
}