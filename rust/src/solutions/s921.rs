use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut open_brackets = 0;
        let mut swaps = 0;

        for c in s.chars() {
            if c == '(' {
                open_brackets += 1;
            }
            else {
                if open_brackets > 0 {
                    open_brackets -= 1;
                }
                else {
                    swaps += 1;
                }
            }
        }
        swaps + open_brackets
    }
}


mod tests {
    use super::*;


}
