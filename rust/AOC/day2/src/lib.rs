#![allow(unused)]
fn read_input(input: &str) -> Vec<(char,char)> {
    input
    .lines()
    .map(|line| 
        line.split_once(' ')
        .map(|(p1,p2)| (p1.chars().next().unwrap(),p2.chars().next().unwrap() )).unwrap() )
    .collect()

}

pub fn process(input: &str) -> u32 {
    let input = read_input(input);
    let mut score = 0;
    for (x,y) in input {

        let y = match y {
            'X' => 'A',
            'Y' => 'B',
            'Z' => 'C',
            _ => unimplemented!()
        };
        score += match y {
            'A' => 1,
            'B' => 2,
            'C' => 3,
            _ => unimplemented!()
        };
        score += match (y,x) {
            (x,y) if x == y => 3,
            ('A','C')  => 6,
            ('B','A')  => 6,
            ('C','B')  => 6,
            _ => 0
        }
    }
    score
}

pub fn process_part2(input: &str) -> u32 {
    let input = read_input(input);
    let mut score = 0;
    for (x,y) in input {


        score += match y {
            'X' => 0,
            'Y' => 3,
            'Z' => 6,
            _ => unimplemented!()
        };

        score += match (x,y) {
            ('A','X') => 3,
            ('A','Y') => 1,
            ('A','Z') => 2,

            ('B','X') => 1,
            ('B','Y') => 2,
            ('B','Z') => 3,

            ('C','X') => 2,
            ('C','Y') => 3,
            ('C','Z') => 1,
            _ => unimplemented!()
        };
    }
    score
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
        assert_eq!(dbg!(process(&input)), 15);
    }

    #[test]
    fn part2_works()
    {
        let input = fs::read_to_string("test.txt").unwrap();
        assert_eq!(dbg!(process_part2(&input)), 12);
    }
}