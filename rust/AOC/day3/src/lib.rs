#![allow(unused)]

use std::{collections::HashSet, ops::Deref};

fn find_common_char(c1: &str, c2: &str) -> char {
    let map = c1.chars().fold(HashSet::new(), |mut f, c| {
        f.insert(c);
        f
    });

    c2.chars().skip_while(|c| !map.contains(c)).next().unwrap()

    // for c in c2.chars() {
    //     if let Some(x) = map.get(&c) {
    //         return *x;
    //     }
    // }
}

fn find_common_char_in_array(arr: &[&str]) -> char {
    let freq = |c1: &str| {
        c1.chars().fold(HashSet::new(), |mut f, c| {
            f.insert(c);
            f
        })
    };

    let sets: Vec<HashSet<char>> = arr.iter().map(|line| freq(line)).collect();

    let mut sets = sets.into_iter();
    let mut result = sets.next().unwrap();
    for set in sets.skip(1) {
        result = result.intersection(&set).map(|c| *c).collect();
    }
    result.into_iter().last().unwrap()
}

fn priority(c: char) -> u32 {
    (match c {
        'a'..='z' => (c as u8) - b'a' + 1,
        'A'..='Z' => (c as u8) - b'A' + 27,
        _ => todo!(),
    }) as u32
}

pub fn process(input: &str) -> u32 {
    input
        .lines()
        .map(|line| line.split_at(line.len() / 2))
        .map(|(c1, c2)| find_common_char(c1, c2))
        .map(priority)
        .sum()
}

pub fn process_part2(input: &str) -> u32 {
    let lines: Vec<&str> = input.lines().collect();

    lines
        .chunks(3)
        .map(find_common_char_in_array)
        .map(priority)
        .sum()
}

#[cfg(test)]
mod test {
    use std::fs;

    use super::*;
    #[test]
    fn it_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process(&input)), 157);
    }

    #[test]
    fn part2_works() {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process_part2(&input)), 70);
    }
}
