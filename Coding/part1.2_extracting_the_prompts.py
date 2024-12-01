import re 

def main():
    with open('generated_prompts.txt', 'r') as base_file:
        with open('extracted_prompts.txt', 'w') as file:
            for line in base_file:
                split_line = re.split('content=|, role=', line)

                if len(split_line) > 1:
                    prompt = split_line[1].strip("'").strip('"')
                    # print(prompt)
                else:
                    print("Line does not contain a prompt in expected format:", line)
                file.write(f"{prompt}\n")
    print("Finished writing extracted prompts to file 'extracted_prompts.txt'")

if __name__ == "__main__":
    main()
