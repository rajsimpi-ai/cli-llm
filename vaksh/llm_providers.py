def simple_calculator(prompt: str) -> str:
    """
    Very simple evaluator: takes math expressions from the prompt.
    Example: vak "2+2" -> '2+2 = 4'
    """
    try:
        expression = prompt.strip().replace("\"", "")
        result = eval(expression)  # ⚠️ only for demo!
        return f"{expression} = {result}"
    except Exception as e:
        return f"{prompt} = Error({e})"