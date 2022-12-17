
pub fn process(input: &str) -> u32 {
    input
    .split("\r\n\r\n")
    .map(|e| e.lines().filter_map(|v| v.parse::<u32>().ok()).sum::<u32>())
    .max()
    .unwrap_or(0)
}

pub fn process_part2(input: &str) -> u32 {
    let mut calories: Vec<u32> = input
    .split("\r\n\r\n")
    .map(|e| e.lines().filter_map(|v| v.parse::<u32>().ok()).sum::<u32>())
    .collect();

    calories.sort();

    calories.iter().rev().take(3).sum()
}

#[cfg(test)]
mod test
{
    use std::fs;

    use super::*;
    #[test]
    fn it_works()
    {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process(&input)), 24000);
    }

    #[test]
    fn part2_works()
    {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process_part2(&input)), 45000);
    }
}