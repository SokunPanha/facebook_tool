from flet import *
from flet_route import Params, Basket
from component import ProfileDataTable_ChBox
import os
import shutil
from module.browser import WebDriverManager
def Post_Active(page:Page, params: Params, basket: Basket):
    current_directory = os.getcwd()
    def uploadFile(e: FilePickerResultEvent):
        print("Current Working Directory:", current_directory)

        for file in e.files:
            print(file.path)
            # Construct the full destination file path using os.path.join
            destination_path = os.path.join(current_directory, "image", file.name)

            # Print the corrected destination file path
            print("Destination Path:", destination_path)

            # Check if the file exists
            if os.path.exists(file.path):
                # File exists, proceed with copying to the destination folder
                shutil.copy(file.path, destination_path)
                print(file)
            else:
                print(f"Error: File '{file.name}' not found.")
       
        
    description_element = TextField(hint_text="Enter description", width= 700)
    file_picker = FilePicker(on_result=uploadFile)
    page.overlay.append(file_picker)
    def removeImage():
        files,path = imageFile()[0], imageFile()[1]
        for file in files:
            file_path = os.path.join(path,file)
            os.remove(file_path)
    def imageFile():
        path = os.path.join(current_directory, 'image')
        files = os.listdir(path)
        filePath = os.path.join(path, files[0])
        return [files, path, filePath]
    def post_all():
        description = description_element.value
        filePath = imageFile()[2]
        tasks = [{'action': 'post_active', 'params': {'image':filePath,'description': description}}]
        web = WebDriverManager()
        web.upload_user_tasks(tasks)
        web.start_service()
        removeImage()


    return View(
     controls=[
        AppBar(
        leading= IconButton(on_click= lambda _: page.go(f"/"), icon= icons.ARROW_BACK),
        leading_width=40,
        title=Text("Home"),
        center_title=False,
        bgcolor=colors.GREY_900,
        elevation= 10,
        actions=[
        ],
    ),
    Column(
        
        controls=[
            # description and upload section 
            Row(
             alignment= MainAxisAlignment.CENTER,
                controls=[
                description_element,
                ElevatedButton("Upload Image", on_click= lambda _: file_picker.pick_files(allow_multiple=True)), 
                ElevatedButton("Post All", on_click=lambda _: post_all())
                ]
            ),
            # table section 
            Row(
             alignment= MainAxisAlignment.CENTER,
             controls=[
                  Column(
            controls=[
                ProfileDataTable_ChBox(page,params,basket, "/profile-update"),
            ]
        )
             ]
         )
        ]
    )
     ]
    )

