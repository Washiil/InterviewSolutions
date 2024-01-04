pub fn number_of_beams(bank: Vec<String>) -> i32 {
    bank.iter()
        .map(|row| row.chars().filter(|&c| c == '1').count())
        .filter(|&row| row != 0)
        .collect::<Vec<_>>()
        .windows(2)
        .fold(0, |acc, window| acc + window[0] * window[1]) as i32
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        let input = vec![
            "011001".to_string(),
            "000000".to_string(),
            "010100".to_string(),
            "001000".to_string(),
        ];
        assert_eq!(super::number_of_beams(input), 8);
    }

    #[test]
    fn test2() {
        let input = vec!["000".to_string(), "111".to_string(), "000".to_string()];
        assert_eq!(super::number_of_beams(input), 0);
    }
}
