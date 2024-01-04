use std::collections::HashMap;

pub fn min_operations(nums: Vec<i32>) -> i32 {
    let mut counts: HashMap<i32, u32> = HashMap::new();
    for n in nums {
        if let Some(x) = counts.get_mut(&n) {
            *x += 1;
        } else {
            counts.insert(n, 1);
        }
    }

    let mut operations = 0;
    for i in counts.values_mut() {
        while *i >= 5 {
            *i -= 3;
            operations += 1;
        }

        if *i == 3 {
            *i -= 3;
            operations += 1;
        }

        while *i >= 2 {
            *i -= 2;
            operations += 1;
        }

        if *i != 0 {
            return -1;
        }
    }
    return operations;
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        let input = vec![2, 3, 3, 2, 2, 4, 2, 3, 4];
        assert_eq!(super::min_operations(input), 4);
    }

    #[test]
    fn test2() {
        let input = vec![2, 1, 2, 2, 3, 3];
        assert_eq!(super::min_operations(input), -1);
    }
}
