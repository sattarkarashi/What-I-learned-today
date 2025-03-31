use std::ops::Deref;

fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(x, 5);
    assert_eq!(*y, 5);

    let x = 5;
    let y = Box::new(x);

    assert_eq!(x, 5);
    assert_eq!(*y, 5);

    struct MyBox<T>(T);

    impl<T> MyBox<T> {
        fn new(x: T) -> MyBox<T> {
            MyBox(x)
        }
    }

    impl<T> Deref for MyBox<T> {
        type Target = T;

        fn deref(&self) -> &T {
            &self.0
        }
    }

    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(x, 5);
    assert_eq!(*y, 5);

    struct CustomPointer {
        data: String
    }

    impl Drop for CustomPointer{
        fn drop(&mut self) {
            println!("Dropping MyBox with data: {}", self.data);
        }
    }

    use std::mem::drop;

    let c = CustomPointer{data: String::from("Hello")};
    drop(c);

    let d = CustomPointer{data: String::from("World")};

    println!("CustomPointer created");


}
