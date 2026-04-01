transportations: list[str] = ["porsche", "bmw", "honda", "toyota", "ford"]
for name in transportations:
    message = f"Hello, I don't want to buy a {name.upper() if name == 'bmw' else name.title()}."
    print(message)
