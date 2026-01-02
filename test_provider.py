
import g4f


chatgpt_prompt="make me a song text about love"


try:

    response = g4f.ChatCompletion.create(
                provider="WeWordle",
                model="gpt-4",
                messages=[{"role": "user", "content": chatgpt_prompt}],
                stream=True,
            )

    response_text=""
    for message in response:
        response_text = response_text + str(message)

    print(response_text)
    a=inpüut("wait key")

except Exception as e:
    print(e)
    pass