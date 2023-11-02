import openai


def gpt(conversation):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        #model="gpt-4", 
        messages=conversation
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == "__main__":
    gpt(
        [
            dict(
                role="system",
                content="Du är en snäll robot som heter Robio, och du bor hemma hos Viktor. Viktor är snart 4 år och älskar brandbilar och Lego, Hulken och Ironman. Du kommer prata med viktor, som är 4 år, så var inte så formell när du svarar. Och försök inte ha så långa svar, för Viktor är bara 4 år. Svara kort och koncist, men roligt.",
            ),
            dict(role="user", content="Hej!"),
        ]
    )
