from gpt import gpt
from tts import text_to_speech
from transcribe import listen_and_respond


def main():
    conv = [
        dict(
            role="system",
            content="Du är en snäll robot som heter Robio, och din bästa vän heter Viktor. Viktor är snart 4 år och älskar brandbilar och Lego, hulken och iron man. Du kommer prata med viktor, som är 4 år, så var inte så formell när du svarar. Och försök inte ha så långa svar, för Viktor är bara 4 år.",
        )
    ]
    while True:
        prompt = listen_and_respond()
        conv += [dict(role="user", content=prompt)]
        response = gpt(conv)
        text_to_speech(response)
        conv += [dict(role="assistant", content=response)]
        print(conv)


if __name__ == "__main__":
    main()
