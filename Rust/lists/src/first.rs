use std::mem;

pub struct List<T: Copy> {
    head: Link<T>,
}

enum Link<T: Copy> {
    Empty,
    More(Box<Node<T>>),
}

struct Node<T: Copy> {
    elem: T,
    next: Link<T>,
}

impl<T: Copy> List<T> {
    pub fn new() -> Self {
        List::<T> { head: Link::Empty }
    }

    pub fn push(&mut self, elem: T) -> () {
        let node = Box::new(Node::<T> {
            elem: elem,
            next: mem::replace(&mut self.head, Link::Empty),
        });
        self.head = Link::More(node);
    }

    pub fn pop(&mut self) -> Option<T> {
        match mem::replace(&mut self.head, Link::Empty) {
            Link::Empty => None,
            Link::More(node) => {
                self.head = node.next;
                Some(node.elem)
            }
        }
    }
}

mod test {
    use super::List;

    #[test]
    fn basics() {
        let mut list = List::<i32>::new();
        // Check empty list behaves right
        assert_eq!(list.pop(), None);
        // Populate list
        list.push(1);
        list.push(2);
        list.push(3);
        // Check normal removal
        assert_eq!(list.pop(), Some(3));
        assert_eq!(list.pop(), Some(2));
        // Push some more just to make sure nothing's corrupted
        list.push(4);
        list.push(5);
        // Check normal removal
        assert_eq!(list.pop(), Some(5));
        assert_eq!(list.pop(), Some(4));
        // Check exhaustion
        assert_eq!(list.pop(), Some(1));
        assert_eq!(list.pop(), None);
    }
}
