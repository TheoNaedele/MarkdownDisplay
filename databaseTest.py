import sqlite3
import os

# Function to create the database and tables
def create_tables():
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    # Create the Documents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Documents (
            ID INTEGER PRIMARY KEY,
            FileType TEXT,
            FileData BLOB,
            FileName TEXT
        )
    """)

    # Create the Testcase table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Testcase (
            ID INTEGER PRIMARY KEY,
            Name TEXT
        )
    """)

    # Create the Testsuite table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Testsuite (
            ID INTEGER PRIMARY KEY,
            Name TEXT
        )
    """)

    # Create the many-to-many relationship table (Document_Testcase)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Document_Testcase (
            DocumentID INTEGER,
            TestcaseID INTEGER,
            FOREIGN KEY (DocumentID) REFERENCES Documents(ID),
            FOREIGN KEY (TestcaseID) REFERENCES Testcase(ID),
            PRIMARY KEY (DocumentID, TestcaseID)
        )
    """)

    # Create the many-to-many relationship table (Document_Testsuite)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Document_Testsuite (
            DocumentID INTEGER,
            TestsuiteID INTEGER,
            FOREIGN KEY (DocumentID) REFERENCES Documents(ID),
            FOREIGN KEY (TestsuiteID) REFERENCES Testsuite(ID),
            PRIMARY KEY (DocumentID, TestsuiteID)
        )
    """)

    conn.commit()
    conn.close()

# Function to insert a file into the Documents table
def insert_document(file_path):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    # Read the file as binary data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Get the file type based on the file extension
    file_type = file_path.split(".")[-1]
    file_name = file_path.split("/")[-1]

    # Insert the file into the Documents table
    cursor.execute("INSERT INTO Documents (FileType, FileData, FileName) VALUES (?, ?, ?)", (file_type, sqlite3.Binary(file_data), file_name))

    conn.commit()
    conn.close()

# Function to retrieve a file from the Documents table and write it to a specified path
def retrieve_document(document_id, output_path):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    # Retrieve the file data and type from the Documents table
    cursor.execute("SELECT FileType, FileData, FileName FROM Documents WHERE ID = ?", (document_id,))
    row = cursor.fetchone()

    if row:
        #print(row)
        file_type, file_data, file_name = row

        # Construct the output file path with the appropriate file extension
        file_extension = file_type if file_type.startswith('.') else '.' + file_type
        output_file_path = os.path.join(output_path, f"{file_name}{file_extension}")

        # Write the file data to the specified output path
        with open(output_file_path, "wb") as file:
            file.write(file_data)

        print(f"File written to: {output_file_path}")
    else:
        print("Document not found.")

    conn.close()

# Create the tables (if they don't exist)
create_tables()

# Insert a file into the Documents table
file_path_word = "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/03.05.2022 Aufgabenbeschreibung BThesis Theo Nädele.docx"  # Replace with the actual path to your file
file_path_pdf = "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/Procedural Building Generator v1.2.pdf"
file_path_zip = "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/DRV_Chipset_AMD_AM5_SZ-TSD_W11_64_V407132243_20220901R.zip"
file_path_image = "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/test.jpg"
file_paths = [file_path_zip,file_path_word,file_path_image,file_path_pdf]
for file_path in file_paths:
    insert_document(file_path)
for i in range(len(file_paths)):
    retrieve_document(i+1, "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/OutputTest")
#retrieve_document(1, "C:/Users/TheoN/Desktop/Work/TestChatGPT/WordInDatabaseTest/OutputTest")