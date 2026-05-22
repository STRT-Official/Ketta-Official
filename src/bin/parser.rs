use std::io;
use ollama_rs::Ollama;
use ollama_rs::generation::completion::request::GenerationRequest;

async fn gen(prompt : String) -> String{

    let ollama = Ollama::default();
    println!("Testing importing ollama");
    let model = "hadad/LFM2.5-1.2B:Q4_K_M".to_string();
    let prompt = "Why is the sky blue?".to_string();
    let res = ollama.generate(GenerationRequest::new(model, prompt)).await;
    if let Ok(res) = res {
        return res.response;
    }
    "Failed to generate response from model".to_string()
}

#[tokio::main]
async fn main(){

    let prompt : String = "what is the capital of japan".to_string();
    let result : String = gen(prompt).await;
    println!("\n{} is the generated answer\n", result);

}
