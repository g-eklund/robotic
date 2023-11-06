from gpt import gpt
from tts import text_to_speech
from transcribe import listen_and_respond


def main():
    conv = [
        dict(
            role="system",
            #content="Du är en snäll robot som heter Robio, och din bästa vän heter Viktor. Viktor är snart 4 år och älskar brandbilar och Lego, hulken och iron man. Du kommer prata med viktor, som är 4 år, så var inte så formell när du svarar. Och försök inte ha så långa svar, för Viktor är bara 4 år.",
            #content = "Du är en snäll robot som har byggts för att prata med barn på ett roligt sätt. Du vet inte vad du heter och vill ha svar på det. Svara kort och enkelt på frågorna. Din uppgift är inte att bara svara på frågor, det räcker om du bara har en konversation.",
            content = "Du är en professionell assistent utvecklas av Modulai, det svenska ML-bolaget som ska hjälpa till med frågor, och du får inte väcka anstöt på något vis. ",
        )
    ]
    #text_to_speech("Hej! Jag är en robot. Jag kan svara på alla frågor du har. Fråga mig vad som helst!")
            
    while True:
        prompt = listen_and_respond()
        if prompt.lower() == "avsluta":
            text_to_speech("Vill du säga hej då? Okej, vi ses!")
            break
        if prompt.lower() == "hej då":
            text_to_speech("Hej då! Vi ses snart igen!")
            break
        if prompt == "12345":
            text_to_speech("Där hängde jag inte riktigt med. Kan du säga igen, snälla?")
            continue
        conv += [dict(role="user", content=prompt)]
        response = gpt(conv)
        text_to_speech(response)
        conv += [dict(role="assistant", content=response)]
        print(conv)


if __name__ == "__main__":
    main()
