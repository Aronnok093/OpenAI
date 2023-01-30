import openai
openai.api_key="Your API KEY"
while True:
    print("Enter Your Command.Ctrl-D or Ctrl-z to execute.");
    cmd = [];
    prompt="";
    while True:
        try:
            tmp=input()
        except:
            break;
        cmd.append(tmp)

    print("Thinking....")
    ln = len(cmd)
    
    for i in range(ln):
        prompt+=cmd[i]+" "
        
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
    result=response.choices[0].text
    print(result)
    print("Enter To continue")
    input();
