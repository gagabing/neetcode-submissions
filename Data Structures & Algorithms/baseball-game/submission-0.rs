impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut vn: Vec<i32> = Vec::new();

        for op in &operations {
            match op.as_str() {
                "C" => {vn.pop();}
                "D" => {
                    let last = *vn.last().unwrap();
                        vn.push(last * 2);
                }
                "+" => {
                    let len = vn.len();
                    vn.push(vn[len-1] + vn[len-2]);
                }
                _ => vn.push(op.parse().unwrap()),
            }
        }
        vn.into_iter().sum()
    }
}
