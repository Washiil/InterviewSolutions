pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
    let mut cnt = 0;
    let mut min = left;
    let mut max = right;
    while min != max {
        min >>= 1;
        max >>= 1;
        cnt += 1;
    }
    return min << cnt;
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        assert_eq!(super::range_bitwise_and(5, 7), 4)
    }

    #[test]
    fn test2() {
        assert_eq!(super::range_bitwise_and(0, 0), 0)
    }

    #[test]
    fn test3() {
        assert_eq!(super::range_bitwise_and(1, 2147483647), 0)
    }
}
