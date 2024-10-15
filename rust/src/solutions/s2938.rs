struct Solution {}

impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        let mut swaps: i64 = 0;
        let mut black_ball_count = 0;

        for c in s.chars() {
            if c == '0' {
                swaps += black_ball_count;
            }
            else {
                black_ball_count += 1;
            }
        }

        swaps
    }
}