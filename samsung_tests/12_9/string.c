import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;

//2xN 직사각형을 2x1, 2x2 타일로 채우는 문제
//dp[i] 를 2xi 의 방법의 수라고 할 때, 세로 2는 고정이기 때문에 
//dp[1] 은 1개, dp[2] 는 3개의 방법이 존재한다. 
//이 때, dp[i] = dp[i-1] + dp[i-2]*2 의 점화식을 만들 수 있다. 
//dp[3] 을 생각해보면 dp[2] 는 이 고정이라고 할 때 dp[1] 은 양쪽으로 배치할 수 있기 때문에 x2 가 된다. 

public class Solution {

	static int N;
	static BigDecimal[] dp;

	public static void test(int testNo) {

		dp = new BigDecimal[N + 1];

		// dp[1] = 1
		// dp[2] = 3
		// dp[i] = dp[i-1] + dp[i-2]*2

		if (N < 2) {
			System.out.println("#" + testNo + " 1");
		} else {
			dp[1] = new BigDecimal(1);
			dp[2] = new BigDecimal(3);

			for (int i = 3; i <= N; i++) {
				BigDecimal tmp = dp[i - 1].add(dp[i - 2].multiply(new BigDecimal(2)));
				dp[i] = tmp;
			}

			System.out.println("#" + testNo + " " + dp[N]);
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			test(tc);
		}
	}
}