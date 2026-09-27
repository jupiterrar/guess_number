class UI:

    def show_message(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)