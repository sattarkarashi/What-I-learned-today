use std::sync::mpsc;
use std::thread;
use std::time::Duration;



fn main() {
    // Let's explore sending and recieving messages using channels between threads.
    let (tx, rx) = mpsc::channel();
    thread::spawn(move || {
        let val = String::from("Hello from the spawned thread!");
        tx.send(val).unwrap();
        // The send method will block until the message is received.
        // If we don't receive the message, the spawned thread will block until the main thread receives it.
    });

    // The main thread will wait for the message to be sent.
    let received = rx.recv().unwrap();
    println!("Received: {}", received);


    // Let's recive multiple messages.
    let (tx, rx) = mpsc::channel();
    let tx1 = tx.clone();
    thread::spawn(move || {
        let vals = vec![
            String::from("Hello from the spawned thread1!"),
            String::from("How are you?"),
            String::from("Goodbye!"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });
    thread::spawn(move || {
        let vals = vec![
            String::from("Hello from the spawned thread2!"),
            String::from("How are you?"),
            String::from("Goodbye!"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Received: {}", received);
    }


}
