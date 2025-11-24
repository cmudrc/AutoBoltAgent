import torch
import transformers
import llama_cpp
import requests
import fastener_toolkit as ft
import prompts
import sp

llm = llama_cpp.Llama.from_pretrained(
    repo_id="bartowski/WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B-GGUF",
    filename="WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B-IQ4_XS.gguf",
    n_ctx=16000,
    n_gpu_layers = -1,
    seed = -1,
    use_mlock = False
)

def llm_engine(messages, stop_sequences = ["Task"]) -> str:
    response = llm.create_chat_completion(
        messages = messages,
        stop = stop_sequences,
        max_tokens = 10000,
    )

    if "choices" in response and len(response["choices"]) > 0:
        if "message" in response["choices"][0] and "content" in response["choices"][0]["message"]:
            answer = response["choices"][0]["message"]["content"]
        else:
            # Handle the case where "message" or "content" is missing
            answer = "Error: Incomplete response structure."
    else:
        # Handle the case where the "choices" list is empty or missing
        answer = "Error: No valid response received."

    return answer

    


def main():

    
    structured_prompts = prompts.generate_structured_prompts()

    for i, (prompt, load, preload, clamped_length, fos) in enumerate(structured_prompts, start=1):

        agent = transformers.ReactCodeAgent(
            tools=[FastenatingCalculator()],
            llm_engine = llm_engine,
            add_base_tools=False,
            verbose=2,
            max_iterations = 50,
            system_prompt = sp.system_pr
        )

        response = agent.run(prompt)  # Assuming `agent.run()` executes the prompt
        print(response)

    print("30 problems solved. Results saved to results.csv")
    
if __name__ == "__main__":
    main()