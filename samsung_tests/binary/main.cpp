# include <stdio.h>

char card[51][101]

int getDigit(int row, int col)
{
    if (card[row][col] != '0')
    return -1
    if (card[row][col+6] != '1')
    return -1

    if (card[row][col+1] == '0' & & card[row][col+2] == '0' & & card[row][col+3] == '1' & & card[row][col+4] == '1' & & card[row][col+5] == '0')
    return 0
    if (card[row][col+1] == '0' & & card[row][col+2] == '1' & & card[row][col+3] == '1' & & card[row][col+4] == '0' & & card[row][col+5] == '0')
    return 1
    if (card[row][col+1] == '0' & & card[row][col+2] == '1' & & card[row][col+3] == '0' & & card[row][col+4] == '0' & & card[row][col+5] == '1')
    return 2
    if (card[row][col+1] == '1' & & card[row][col+2] == '1' & & card[row][col+3] == '1' & & card[row][col+4] == '1' & & card[row][col+5] == '0')
    return 3
    if (card[row][col+1] == '1' & & card[row][col+2] == '0' & & card[row][col+3] == '0' & & card[row][col+4] == '0' & & card[row][col+5] == '1')
    return 4
    if (card[row][col+1] == '1' & & card[row][col+2] == '1' & & card[row][col+3] == '0' & & card[row][col+4] == '0' & & card[row][col+5] == '0')
    return 5
    if (card[row][col+1] == '1' & & card[row][col+2] == '0' & & card[row][col+3] == '1' & & card[row][col+4] == '1' & & card[row][col+5] == '1')
    return 6
    if (card[row][col+1] == '1' & & card[row][col+2] == '1' & & card[row][col+3] == '1' & & card[row][col+4] == '0' & & card[row][col+5] == '1')
    return 7
    if (card[row][col+1] == '1' & & card[row][col+2] == '1' & & card[row][col+3] == '0' & & card[row][col+4] == '1' & & card[row][col+5] == '1')
    return 8
    if (card[row][col+1] == '0' & & card[row][col+2] == '0' & & card[row][col+3] == '1' & & card[row][col+4] == '0' & & card[row][col+5] == '1')
    return 9

    return -1
}


int main(void)
{
    int cc
    int N, M


    scanf("%d", & cc)

    for (int c=1
         c <= cc
         c++)
    {
        scanf("%d%d\n", & N, & M)
        for (int i=1
             i <= N
             i++)
        scanf("%s", & card[i][1])

        int a, b
        bool bFlag = false
        for (a=1
             a <= N
             a++)
        {
            for (b=M
                 b >= 8
                 b--)
            {
                if (card[a][b] == '1')
                {
                    bFlag = true
                    break
                }
            }

            if (bFlag)
            break
        }

        b -= 6

        int d[9]
        for (int i=8
             i >= 1
             i--)
        {
            d[i] = getDigit(a, b)
            b -= 7
        }

        int sum
        if (((d[1] + d[3] + d[5] + d[7]) * 3 + d[2] + d[4] + d[6] + d[8]) % 10 == 0)
        sum = d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8]
        else
        sum = 0

        printf("#%d %d\n", c, sum)

    }
    return 0
}
