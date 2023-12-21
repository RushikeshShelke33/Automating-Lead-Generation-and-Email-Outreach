import gspread
import openai

# Set up your OpenAI API key
# This is necessary to authenticate your requests to the OpenAI API
# Replace 'your-api-key' with your actual OpenAI API key
api_key = 'your-api-key'
openai.api_key = api_key

# Function to generate email text using OpenAI API
# This function takes a company name and location as input, and returns a personalized email text

def get_email_text(name, location="Pune"):
    # The prompt for the OpenAI API is constructed using the company name and location
    # The API then generates a completion based on this prompt

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"take given company name '{name}' and its location '{location}' and create dynamic and personalized email text that we send to this company for sales inquiry. Incorporate lead-specific information e.g. name and business details into the email text",
        max_tokens=150
    )

    # The generated text is extracted from the response and returned by the function

    return response.choices[0].text.strip()

# Use gspread to read data from Google Sheet
# Replace 'your-creds.json' with your own JSON file that contains your Google API credentials

gc = gspread.service_account(filename='creds.json')
sh = gc.open('Your-Google-Sheet-Name').sheet1

# Get all values from the sheet
data = sh.get_all_values()

# Iterate over each row in data
for row in data:
    # Assuming first column is name and second is address
    name = row[0]
    address = "Pune"  # Address is taken As pune because the script works with Scraping so location should be taken from it
    
    # Generate email text for each row
    # Print out the generated email text for each company name and address

    email_text = get_email_text(name, address)
    print("Email Text For",name,"and Address: ",address)
    print(email_text)
