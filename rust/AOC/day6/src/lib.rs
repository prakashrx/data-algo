#![allow(unused)]

use std::{
    collections::{HashMap, HashSet},
    ops::Add,
};

fn find_marker(input: &str, c: usize) -> u32 {
    let mut freq: HashMap<&u8, i32> = HashMap::new();
    let chars = input.as_bytes();
    for i in 0..c {
        let x = freq.entry(&chars[i]).or_insert(0);
        *x += 1;
    }

    for i in c..chars.len() {
        if let Some(x) = freq.get_mut(&chars[i - c]) {
            *x -= 1;

            if *x == 0 {
                freq.remove(&chars[i - c]);
            }
        }
        let x = freq.entry(&chars[i]).or_insert(0);
        *x += 1;

        if freq.len() == c && freq.values().all(|v| *v == 1) {
            return ((i + 1) as u32);
        }
    }

    0
}

pub fn process(input: &str) -> u32 {
    find_marker(&input, 4)
}

pub fn process_part2(input: &str) -> u32 {
    find_marker(&input, 14)
}

#[cfg(test)]
mod test {
    use std::fs;

    use super::*;
    #[test]
    fn example1_works() {
        let input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
        assert_eq!(dbg!(process(&input)), 7);
    }

    #[test]
    fn example2_works() {
        let input = "bvwbjplbgvbhsrlpgdmjqwftvncz";
        assert_eq!(dbg!(process(&input)), 5);
    }

    #[test]
    fn example3_works() {
        let input = "nppdvjthqldpwncqszvftbrmjlhg";
        assert_eq!(dbg!(process(&input)), 6);
    }

    #[test]
    fn example4_works() {
        let input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
        assert_eq!(dbg!(process(&input)), 10);
    }

    #[test]
    fn example5_works() {
        let input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";
        assert_eq!(dbg!(process(&input)), 11);
    }

    #[test]
    fn part2_example1_works() {
        let input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
        assert_eq!(dbg!(process_part2(&input)), 19);
    }

    #[test]
    fn part2_example2_works() {
        let input = "bvwbjplbgvbhsrlpgdmjqwftvncz";
        assert_eq!(dbg!(process_part2(&input)), 23);
    }

    #[test]
    fn part2_example3_works() {
        let input = "nppdvjthqldpwncqszvftbrmjlhg";
        assert_eq!(dbg!(process_part2(&input)), 23);
    }

    #[test]
    fn part2_example4_works() {
        let input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
        assert_eq!(dbg!(process_part2(&input)), 29);
    }

    #[test]
    fn part2_example5_works() {
        let input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";
        assert_eq!(dbg!(process_part2(&input)), 26);
    }
}
