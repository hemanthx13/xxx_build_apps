from dotenv import load_dotenv
import os

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_test = os.getenv("GEMINI_API_TEST")

print(todoist_api_key)
print(gemini_api_key)
print(gemini_api_test)

# if gemini_api_test is true i.e. it has some data, it prints empty string;
# otherwise, it prints "Add key to gemini_api_test"
print("" if gemini_api_test else "Add key to gemini_api_test")

# if gemini_api_test is true i.e. it has data, it prints "Key Provided";
# otherwise, it prints "Add key to gemini_api_test"
print("Key Provided" if gemini_api_test else "Add key to gemini_api_test")

# Old way
'''
if gemini_api_test:
    print("Key Provided")
else:
    print("Add key to gemini_api_test")
'''