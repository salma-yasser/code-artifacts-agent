from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

load_dotenv()


class LLMResponse(BaseModel):
    text: str
    input_tokens: int
    output_tokens: int


def ask(prompt: str, temperature: float = 0.0) -> LLMResponse:
    model = init_chat_model("groq:openai/gpt-oss-20b", temperature=temperature)
    response = model.invoke(prompt)
    usage = response.usage_metadata
    return LLMResponse(
        text=response.content,
        input_tokens=usage["input_tokens"],
        output_tokens=usage["output_tokens"],
    )


if __name__ == "__main__":
    prompt = "Suggest one name for an AI research assistant. Reply with the name only."

    for temperature in [0.0, 1.0]:
        print(f"\n--- temperature = {temperature} ---")
        for run in range(1, 4):
            result = ask(prompt, temperature)
            print(f"Run {run}: {result.text}")
            print(f"   tokens -> input: {result.input_tokens}, output: {result.output_tokens}")