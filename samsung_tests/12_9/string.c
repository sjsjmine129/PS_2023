import java.util.Scanner;
import java.math.BigDecimal;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        // Read number of test cases
        int T = sc.nextInt();

        // Process each test case
        for (int test_case = 1; test_case <= T; test_case++) {
            // Read the value of N for this test case
            int N = sc.nextInt();
            
            // Initialize dp array
            BigDecimal[] dp = new BigDecimal[N + 1];

            // Base cases
            if (N < 2) {
                System.out.println("#" + test_case + " 1");
            } else {
                dp[1] = new BigDecimal(1);
                dp[2] = new BigDecimal(3);

                // Fill dp array using recurrence relation
                for (int i = 3; i <= N; i++) {
                    dp[i] = dp[i - 1].add(dp[i - 2].multiply(new BigDecimal(2)));
                }

                // Print the result for the current test case
                System.out.println("#" + test_case + " " + dp[N]);
            }
        }
    }
}
