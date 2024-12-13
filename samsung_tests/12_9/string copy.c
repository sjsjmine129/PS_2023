import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;

public class Solution {

    static int N;
    static BigDecimal[] dp;

    public static void test(int testNo) {
        dp = new BigDecimal[N + 1];

        // Base cases
        if (N < 2) {
            System.out.println("#" + testNo + " 1");
        } else {
            dp[1] = new BigDecimal(1);
            dp[2] = new BigDecimal(3);

            for (int i = 3; i <= N; i++) {
                dp[i] = dp[i - 1].add(dp[i - 2].multiply(new BigDecimal(2)));
            }

            System.out.println("#" + testNo + " " + dp[N]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            test(tc);
        }
    }
}
