use std::{collections::HashSet, fmt::Binary, vec};

struct Solution;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut output: Vec<Vec<i32>> = vec![vec![]];
        
        fn backTrack(start: i32, cur_list: &mut Vec<i32>, output: &mut Vec<Vec<i32>>) {
            output.push(cur_list.clone());

            for j in start..cur_list.len() as i32 {
                cur_list.push(j);
                backTrack(j + 1, cur_list, output);
                cur_list.pop();
            }
        }

        backTrack(0, &mut vec![], &mut output);
        return output;
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_78() {
        let result = Solution::subsets(vec![1, 2, 3]);
        assert_eq!(result, vec![
            vec![],
            vec![1],
            vec![2],
            vec![1, 2],
            vec![3],
            vec![1, 3],
            vec![2, 3],
            vec![1, 2, 3]
        ]);
    }
}
