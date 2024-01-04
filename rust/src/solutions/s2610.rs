pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut groups: Vec<Vec<i32>> = vec![];

    'outer: for num in nums {
        for group in &mut groups {
            if !group.contains(&num) {
                group.push(num);
                continue 'outer;
            }
        }
        groups.push(vec![num]);
    }

    return groups;
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        let input = vec![1, 3, 4, 1, 2, 3, 1];
        // Sum up the lengths of each of the
        let x = super::find_matrix(input)
            .iter()
            .fold(0, |acc, x| acc + x.len());
        assert_eq!(x, 7);
    }

    #[test]
    fn test2() {
        let input = vec![1, 2, 3, 4];
        // Sum up the lengths of each of the
        let x = super::find_matrix(input)
            .iter()
            .fold(0, |acc, x| acc + x.len());
        assert_eq!(x, 4);
    }
}
