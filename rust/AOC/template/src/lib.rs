#![allow(unused)]

pub fn process(input: &str) -> u32 {
    unimplemented!()
}

pub fn process_part2(input: &str) -> u32 {
    unimplemented!()
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
        assert_eq!(dbg!(process(&input)), 0);
    }

    #[test]
    fn part2_works()
    {
        //let input = fs::read_to_string("test.txt").unwrap();
        //assert_eq!(dbg!(process_part2(&input)), 0);
    }
}