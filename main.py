from app.query_interface import ask_question

if __name__ == "__main__":
    while True:
        q = input("Ask your DB: ")
        if q.lower() in ["exit", "quit"]:
            break
        answer = ask_question(q)
        print("\nAgent Answer:\n", answer)
