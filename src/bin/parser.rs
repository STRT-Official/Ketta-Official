use std::io;
use ollama_rs::Ollama;
use ollama_rs::history::ChatHistory;
use ollama_rs::generation::chat::{request::ChatMessageRequest, ChatMessage};

const SYSTEM_INSTRUCTIONs : &str = "Your name is Ketta. You are an AI assistant running on a user's laptop. You can help them by answering questions and executing terminal commands.

If you need to execute a command to gather information or perform an action, you MUST wrap your command exactly in <run_command> and </run_command> tags.
For example:
<run_command>ls -la</run_command>

Rules:
1. ONLY write ONE command block at a time.
2. Wait for the system to return the output of your command before you proceed.
3. If you have the final answer, just output it as normal text without the command tags.";

async fn gen(prompt : String, history : &mut Vec<ChatMessage>) -> String{

    let ollama = Ollama::default();
    let model = "hadad/LFM2.5-1.2B:Q4_K_M".to_string();
    let res = ollama
    .send_chat_messages_with_history(
        history,
        ChatMessageRequest::new(
            model,
            vec![ChatMessage::user(prompt)],
        ),
    ).await;
    if let Ok(res) = res {
        return res.message.content;
    }
    "Failed to generate response from model".to_string()
}

#[tokio::main]
async fn main(){
    let mut history : Vec<ChatMessage> = vec![];
    let mut input = String::new();
    let mut result = String::new();
    let mut prompt = String::new();

    result = gen(SYSTEM_INSTRUCTIONs.to_string(), &mut history).await;
    
    while 1==1{
        io::stdin()
            .read_line(&mut input)
            .expect("Error");
        prompt = input.trim().to_string();
        result = gen(prompt, &mut history).await;
        println!("Ketta : {}", result);
    }

}
