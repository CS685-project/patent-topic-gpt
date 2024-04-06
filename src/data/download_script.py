import requests
import zipfile
import io

def download_zip_file(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the zip file using BytesIO
        with io.BytesIO(response.content) as zip_buffer:
            with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
                # Find the XML file in the zip archive
                xml_file = [file for file in zip_ref.namelist() if file.endswith('.xml')]
                if not xml_file:
                    print("No XML file found in the zip archive.")
                    return None
                # Extract the XML file content
                xml_content = zip_ref.read(xml_file[0])
                return xml_content
    else:
        print("Failed to download file. Status code:", response.status_code)
        return None

def main():
    # URL of the zip file you want to download
    zip_url = 'https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2022/ipg220705.zip'
    
    # Download the zip file and extract the XML content
    xml_content = download_zip_file(zip_url)
    
    if xml_content:
        # Print the XML content
        print("XML file content:\n", xml_content.decode('utf-8'))

if __name__ == "__main__":
    main()
