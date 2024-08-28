def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += f"{i}{j}"
    return result
if __name__ == "__main__":
    for num in range(3, 21):
        password = generate_password(num)
        print(f"{num} - {password}")

