use std::mem;

pub struct List<T>
where
    T: Copy,
{
    head: Link<T>,
}

enum Link<T>
where
    T: Copy,
{
    Empty,
    More(Box<Node<T>>),
}

struct Node<T>
where
    T: Copy,
{
    elem: T,
    next: Link<T>,
}

impl<T> List<T>
where
    T: Copy,
{
    pub fn new() -> Self {
        List::<T> {
            head: Link::<T>::Empty,
        }
    }

    pub fn push(&mut self, elem: T) -> () {
        let node = Box::new(Node::<T> {
            elem: elem,
            next: mem::replace(&mut self.head, Link::<T>::Empty),
        });
        self.head = Link::<T>::More(node);
    }

    pub fn pop(&mut self) -> Option<T> {
        match mem::replace(&mut self.head, Link::<T>::Empty) {
            Link::<T>::Empty => None,
            Link::<T>::More(node) => {
                self.head = node.next;
                Some(node.elem)
            }
        }
    }
}

impl<T> Drop for List<T>
where
    T: Copy,
{
    fn drop(&mut self) {
        let mut cur = mem::replace(&mut self.head, Link::<T>::Empty);
        while let Link::<T>::More(mut node) = cur {
            cur = mem::replace(&mut node.next, Link::<T>::Empty);
        }
    }
}

mod test {
    #[test]
    fn basics() {
        let mut list = super::List::<i32>::new();

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
