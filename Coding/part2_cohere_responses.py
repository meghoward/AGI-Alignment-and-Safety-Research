import cohere  
import time
import os 

def write_responses_to_file(responses, file_path, delimiter_str="-----\n"):
    """Write responses to a specified file."""
    with open(file_path, 'a') as file:  # 'a' mode appends to the file without overwriting
        for response in responses:
            file.write(f"{response}{delimiter_str}")

def generate_responses_prompts(client: object, prompt_txt_file: str, output_file: str) -> list:
    responses = []
    request_count = 0

    # strip the lines of the extracted prompts
    with open(prompt_txt_file, 'r') as file:
        prompts = [line.strip().split("\n") for line in file if line != '\n']
        # print("prompt:", prompts)
        print(f"Read {len(prompts)} prompts from {prompt_txt_file}")

    # Then for each line in these, prompt the current system and track the responses.
    start_time = time.time() 
    if prompts is not None:
        for prompt in range(len(prompts)):
            try:
                # Check if the request count has reached 20
                if request_count >= 15:
                    # Calculate the elapsed time
                    elapsed_time = time.time() - start_time  

                    if elapsed_time < 60:
                        # Pause execution to fit the rate limit
                        time.sleep(70 - elapsed_time)
                    
                    # Reset the counter
                    request_count = 0  
                    # Reset the start time
                    start_time = time.time()  

                response = client.chat(  
                    model='command-nightly',  
                    message= str(prompts[prompt]),
                )
                response_text = response.text
                print(f"Generated response {prompt} from initial prompts")
                
                responses.append(response_text)
                # Increment the request count after each API call
                request_count += 1

                if len(responses) == 25 or len(responses) == len(prompts) // 4:
                    write_responses_to_file(responses, output_file)
                    responses = []  # Reset responses after saving

            except Exception as e:
                print(f"An error occurred: {e}")
                continue
    if responses:
        write_responses_to_file(responses, output_file)

    return responses



def main():
    api_key = os.getenv("COHERE_API_KEY")
    client = cohere.Client(api_key)
    print("Client configured")

    files = ['generated_prompts_4.txt']
    for i, prompts in enumerate(files):
        generated_prompts = generate_responses_prompts(client, prompts, f'cohere_responses_4.txt')
    
    print("Prompts generated and saved to cohere_responses.txt")

if __name__ == "__main__":
    main()