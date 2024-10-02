use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut unqiue_elements = arr.clone();
        unqiue_elements.sort();
        unqiue_elements.dedup();

        let ranks: HashMap<i32, i32> = unqiue_elements
            .iter()
            .enumerate()
            .map(|(index, val)| (*val, (index + 1) as i32))
            .collect();

        arr
            .iter()
            .map(|x| *ranks.get(&x).unwrap())
            .collect::<Vec<i32>>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_1331() {
        let input = vec![40,10,20,30];
        assert_eq!(Solution::array_rank_transform(input), vec![4,1,2,3])
    }
}