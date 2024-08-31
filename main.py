import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image

def convert_images_to_pdf(folder_path):
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    # Get all image files in the folder with supported formats
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(supported_formats)]
    
    if not image_files:
        messagebox.showerror("Error", "No JPG, JPEG, PNG, or WEBP images found in the selected folder.")
        return
    
    # Open the first image
    first_image = Image.open(image_files[0]).convert('RGB')

    # Convert all images to RGB mode and store them in a list
    images = [Image.open(image).convert('RGB') for image in image_files[1:]]

    # Save all images into a single PDF file
    output_path = os.path.join(folder_path, 'output.pdf')
    first_image.save(output_path, save_all=True, append_images=images)

    messagebox.showinfo("Success", f"PDF created successfully at {output_path}")

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        convert_images_to_pdf(folder_selected)

# Set up the main application window
root = Tk()
root.title("Image to PDF Converter")
root.geometry("400x200")

# Label
label = Label(root, text="Select a folder containing JPG, JPEG, PNG, or WEBP images to convert to PDF", wraplength=300)
label.pack(pady=20)

# Button to select folder
select_button = Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

# Run the application
root.mainloop()
