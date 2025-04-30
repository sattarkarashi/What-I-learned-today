use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..=10 {
            println!("Spawned thread: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
        
    });
    
    
    for i in 1..=5 {
        println!("Main thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    };

    // In the above code, the spawned thread will not finish executing before the main thread exits. 
    // To fix it we can use thread::join() to wait for the spawned thread to finish before exiting the main thread.


    let handle = thread::spawn(|| {
        for i in 1..=10 {
            println!("Spawned thread: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
        
    });

    for i in 1..=5 {
        println!("Main thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    };
    // Wait for the spawned thread to finish
    handle.join().unwrap();

    // Point: based on where we put the handle, we can control if the main thread waits for the spawned thread to finish or not and about its concrrent state.
    
}
