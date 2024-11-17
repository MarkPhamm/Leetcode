class Solution:
    def interpret(self, command: str) -> str:
        while True:
            if "()" in command:
                command = command.replace("()", "o")
            if "(al)" in command:
                command = command.replace("(al)", "al")
            else:
                break
        return command

        