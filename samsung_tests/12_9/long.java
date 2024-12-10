import java.util.Scanner;
import java.util.Arrays;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {

        Scanner scanner = new Scanner(System.in);
        int testCaseCount;
        testCaseCount = scanner.nextInt();

        for (int currentTestCase = 1; currentTestCase <= testCaseCount; currentTestCase++)
        {
            int stringLength = scanner.nextInt();
            String inputString = scanner.next();

            int[] suffixArray = calculateSuffixArray(inputString);
            int[] lcpArray = calculateLCP(inputString, suffixArray);

            int maxLCP = 0;
            for (int i = 0; i < stringLength; i++) {
                maxLCP = Math.max(maxLCP, lcpArray[i]);
            }

            System.out.println("#" + currentTestCase + " " + maxLCP);
        }
    }

    public static int[] calculateSuffixArray(String inputString) {
        int length = inputString.length();
        Suffix[] suffixes = new Suffix[length];

        for (int i = 0; i < length; i++) {
            int rank = inputString.charAt(i) - 'a';
            suffixes[i] = new Suffix(i, rank);
        }

        for (int i = 0; i < length - 1; i++) {
            suffixes[i].nextRank = suffixes[i + 1].rank;
        }
        suffixes[length - 1].nextRank = -1;

        Arrays.sort(suffixes);

        int[] temporaryArray = new int[length];

        for (int lengthMultiplier = 4; lengthMultiplier < 2 * length; lengthMultiplier <<= 1) {
            int rank = 0;
            int previousRank = suffixes[0].rank;
            suffixes[0].rank = rank;
            temporaryArray[suffixes[0].index] = 0;

            for (int i = 1; i < length; i++) {
                if (suffixes[i].rank == previousRank && suffixes[i].nextRank == suffixes[i - 1].nextRank) {
                    previousRank = suffixes[i].rank;
                    suffixes[i].rank = rank;
                } else {
                    previousRank = suffixes[i].rank;
                    suffixes[i].rank = ++rank;
                }
                temporaryArray[suffixes[i].index] = i;
            }

            for (int i = 0; i < length; i++) {
                int nextIndex = suffixes[i].index + (lengthMultiplier / 2);
                if (nextIndex >= length) {
                    suffixes[i].nextRank = -1;
                    continue;
                }
                suffixes[i].nextRank = suffixes[temporaryArray[nextIndex]].rank;
            }
            Arrays.sort(suffixes);
        }

        int[] resultSuffixArray = new int[length];
        for (int i = 0; i < length; i++) {
            resultSuffixArray[i] = suffixes[i].index;
        }
        return resultSuffixArray;
    }

    private static int[] calculateLCP(String inputString, int[] suffixArray) {
        int length = suffixArray.length;
        int[] lcpArray = new int[length];
        int[] inverseSuffixArray = new int[length];

        for (int i = 0; i < length; i++) {
            inverseSuffixArray[suffixArray[i]] = i;
        }

        int k = 0;
        for (int i = 0; i < length; i++) {
            if (inverseSuffixArray[i] == length - 1) {
                k = 0;
                continue;
            }

            int j = suffixArray[inverseSuffixArray[i] + 1];

            while (i + k < length && j + k < length) {
                if (inputString.charAt(i + k) != inputString.charAt(j + k)) {
                    break;
                }
                k++;
            }

            lcpArray[inverseSuffixArray[i]] = k;

            if (k > 0) {
                k--;
            }
        }
        return lcpArray;
    }
}

class Suffix implements Comparable<Suffix> {
    int index;
    int rank, nextRank;

    public Suffix(int index, int rank) {
        this.index = index;
        this.rank = rank;
    }

    public int compareTo(Suffix target) {
        if (this.rank != target.rank) {
            return Integer.compare(this.rank, target.rank);
        }
        return Integer.compare(this.nextRank, target.nextRank);
    }
}
