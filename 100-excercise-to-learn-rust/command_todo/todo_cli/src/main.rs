use  chrono::{Local, DateTime};
use std::fs;
use std::io;
use serde::{Serialize, Deserialize};

fn main() {
    
    #[derive(Debug, Clone,Serialize, Deserialize)]
    enum TaskState {
        Pending,
        Completed,
        Overdue
    }


    #[derive(Debug,Clone,Serialize, Deserialize)]
    pub struct Task {
        pub task_name:String,
        pub state:TaskState,
        pub created_at:DateTime<Local>,
        pub due_date:u32,
    }


    impl Task {
        pub fn new(task_name: String, due_interval:u32) -> Self {
            Task {
                task_name,
                state: TaskState::Pending,
                created_at: Local::now(),
                due_date: due_interval,
            }
        }
        pub fn mark_complete(&mut self) {
            self.state = TaskState::Completed;
        }
    }
    
    fn save_tasks(tasks:&Vec<Task>) -> Result<(), io::Error> {
        //Serialize task
        let serialized_task = serde_json::to_string_pretty(tasks)?;
        fs::write("task.json", serialized_task)?;

        Ok(())
    }
    
    fn load_tasks(file_name:String) -> Result<Vec<Task>, io::Error> {
        let file_content = fs::read_to_string(file_name)?;
        let tasks: Vec<Task> = serde_json::from_str(&file_content)?;

        Ok((tasks))
    }

    let task  = Task::new(String::from("Sato is on the way"),5);
//    println!("the task is {:?}",task);
    
    let tasks:Vec<Task> = vec![task];

    match save_tasks(&tasks){
        Ok(())=> println!("Saved task {:?} succesfully", tasks),
        Err(e) => println!("Got an eroor: {:?}", e)
    };

    match load_tasks(String::from("task.json")){
       Tasks => {
           println!("Got the task: {:?}", Tasks)
            },
        Err(e) => println!("Hit error: {:?}", e)
    };
}
