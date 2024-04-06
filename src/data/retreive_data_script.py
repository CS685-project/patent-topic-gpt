from download_script import download_zip_file


#loops through link dataset, for each link it downloads the xml contents
with open('links.txt', 'r') as file:
    for line in file:
        link = line.strip()  
        xml_contents = download_zip_file(link)
        #call your script here using the xml contents
        break