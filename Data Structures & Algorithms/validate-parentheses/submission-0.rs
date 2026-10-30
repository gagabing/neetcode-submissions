impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for p in s.chars() {
            match p {
                '(' | '[' | '{' => {stack.push(p)},
                _ => {
                    let expected = match p {
                        ')' => '(',
                        ']' => '[',
                        '}' => '{',
                        _ => unreachable!(),
                    };
                    if stack.pop() != Some(expected) {
                        return false;
                    }
                }
            }
        }
        stack.is_empty()
    }
}
