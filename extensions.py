"""
File Extensions

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""
# def extensions():
#     possible_extensions = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
#     file_types = ["image", "image", "image", "image", "application", "text", "file"]
#     extension = input("Please type out the extension of your file...")[-4:].lower().replace(".", "")
#     try:
#         index = possible_extensions.index(extension)
#         print(f"{file_types[index]}/{extension}")
#     except ValueError:
#         print(f'"{extension}" is not valid. Please type out a valid extension')

# extensions()

def get_media_type(file_name):
    file_extension = file_name.lower().split('.')[-1]

    # Dictionary mapping file extensions to media types
    media_types = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Output the media type based on the file extension
    if file_extension in media_types:
        return media_types[file_extension]
    else:
        return 'application/octet-stream'

def main():
    # Prompt the user for the file name
    file_name = input("Enter the file name: ")

    # Get and print the media type
    media_type = get_media_type(file_name)
    print("Media type:", media_type)

if __name__ == "__main__":
    main()