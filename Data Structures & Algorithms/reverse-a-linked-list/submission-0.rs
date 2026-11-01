// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        //print_list(&head);

        let mut prev: Option<Box<ListNode>> = None;
        let mut current = head;

        while let Some(mut node) = current {
            current = node.next.take();
            node.next = prev;
            prev = Some(node)
        }

        prev
    }


}

    fn print_list(head: &Option<Box<ListNode>>) {
        let mut current = head.as_deref();
        while let Some(node) = current {
            print!("{} -> ", node.val);
            current = node.next.as_deref();
        }
        println!("None");
    }
