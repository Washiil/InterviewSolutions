struct Solution;

impl Solution {
    fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut people = vec![0; (n + 1) as usize];
        for pair in trust {
            let truster = pair[0];
            let target = pair[1];
            people[truster as usize] -= 1;
            people[target as usize] += 1;
        }

        for i in 1..n + 1 {
            if people[i as usize] == n - 1 {
                return i;
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = vec![vec![1, 2]];
        assert_eq!(Solution::find_judge(2, input), 2);
    }

    #[test]
    fn test2() {
        let input = vec![vec![1, 3], vec![2, 3]];
        assert_eq!(Solution::find_judge(3, input), 3);
    }

    #[test]
    fn test3() {
        let input = vec![vec![1, 3], vec![2, 3], vec![3, 1]];
        assert_eq!(Solution::find_judge(3, input), -1);
    }
}
