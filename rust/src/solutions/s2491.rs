struct Solution;

impl Solution {
    pub fn divide_players(skill: Vec<i32>) -> i64 {
        let mut skill = skill.clone();

        skill.sort();
        let n = skill.len();

        let mut left = 0;
        let mut right = n - 1;

        let base_sum = skill[0] + skill[1];

        let mut pairs: Vec<(i32, i32)> = Vec::new();
        while left < right {
            if skill[left] + skill[right] != base_sum {
                return -1;
            }
            pairs.push((skill[left], skill[right]));
            left += 1;
            right -= 1;
        }

        let mut chemistry: i64 = 0;
        for (p1, p2) in pairs {
            chemistry += (p1 * p2) as i64;
        }
        chemistry
    }
}