struct Solution;

impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut fives = 0;
        let mut tens = 0;

        for b in bills {
            match b {
                5 => fives += 1,
                10 => {
                    if fives <= 0 {
                        return false;
                    }
                    tens += 1;
                    fives -= 1;
                },
                20 => {
                    if tens > 0 && fives > 0{
                        tens -= 1;
                        fives -= 1;
                    }
                    else if fives >= 3 {
                        fives -= 3;
                    }
                    else {
                        return false
                    }
                },
                _ => {}
            }
        }

        return true;
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_860() {
        let input = vec![5,5,5,10,20];

        assert_eq!(Solution::lemonade_change(input), true);
    }
}
