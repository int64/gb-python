user_seconds = int(input("Введите секунды >>> "))

hours = user_seconds // 3600
minutes = user_seconds % 3600 // 60
seconds = user_seconds % 3600 % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
