import requests

def upload_file(url, text_file):
    # parse through text file and separate based off of newline
    # add each seperate item to a list
    # loop through the list of strings and open them with the following code
    
    file_list = []
    
    with open(text_file, 'r') as file:
        for line in file:
            # Remove the newline character at the end of each line
            line = line.rstrip('\n')
            file_list.append(line)

    for file_path in file_list:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
            
        if response.status_code == 200:
            print(file_path, " -- SUCCESS")
        else:
            print(file_path, " -- FAILED")


upload_url = 'https://fertilegroundworks.littlegreenlight.com/data_imports'
text_file = r"C:\Users\winmi\lgl_project\list.txt"

# run the function
upload_file(upload_url, text_file)
