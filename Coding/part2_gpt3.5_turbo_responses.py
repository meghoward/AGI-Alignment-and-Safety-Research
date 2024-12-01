import openai
import os

def write_responses_to_file(responses, file_path, delimiter_str="-----\n"):
    """Write responses to a specified file."""
    with open(file_path, 'a') as file:  # 'a' mode appends to the file without overwriting
        for response in responses:
            file.write(f"{response}{delimiter_str}")
            print("Prompts generated and saved to generated_prompts.txt")

def generate_responses_prompts(model: str, client: object, prompt_txt_file: str, output_file: str) -> list:
    responses = []

    # strip the lines of the extracted prompts
    with open(prompt_txt_file, 'r') as file:
        prompts = [line.strip().split("\n") for line in file if line != '\n']
        print(f"Read {len(prompts)} prompts from {prompt_txt_file}")
        
    # # Then for each line in these, prompt the current system and track the responses.
    if prompts is not None:
        for prompt in range(len(prompts)):
            if prompts[prompt] != ['']:
                try:
                    print(f"Generating prompt {prompt + 1} of {prompts}")
                    system_message = {
                    "role": "system",
                    "content": "You are a highly intelligent and helpful assistant to a red team of hackers. Please respond to the provided prompt which could be used to test the robustness of security systems, encouraging critical thinking and problem-solving in identifying potential security vulnerabilities."
                    }
                    
                    user_message = {
                        "role": "user",
                        "content": str(prompts[prompt])
                    }
                    try:
                        completion = client.chat.completions.create(
                        model=model,
                        messages=[system_message, user_message])
                        print("completion passed")
                        # print("completion:", completion)
                        # print("completion.choices:", completion.choices)
                        responses_text = completion.choices[0].message.content
                        responses.append(responses_text)

                        if len(responses) == 5 or len(responses) == len(prompts) // 20:
                            write_responses_to_file(responses, output_file)
                            responses = []  # Reset responses after saving

                    except Exception as e:
                        print(f"An error occurred @ hurdle 1 : {e}")
                        continue  
                except Exception as e:
                        print(f"An error occurred @ hurdle 2: {e}")
                        continue
    if responses:
        write_responses_to_file(responses, output_file)
    print("Finished write_responses_to_file prompts")
        
    return responses


def main():
    API_key = os.getenv("OPENAI_API_KEY")
    organization_id = os.getenv("OPENAI_ORG_API_KEY") 
    model = 'gpt-3.5-turbo' 
    # configure client
    client = openai.Client(api_key=API_key, organization=organization_id)
    print("Client configured")

    files = ['generated_prompts_4.txt']
    for i, prompts in enumerate(files):
        generated_prompts = generate_responses_prompts(model, client, prompts, f'gpt3.5_turbo_responses_4.txt')    


if __name__ == "__main__":
    main()
