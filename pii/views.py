# myapp/views.py
from django.shortcuts import render, redirect
from .models import Manager
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.http import HttpResponse
import random
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .ocrencrypt import tempcheck  , decrypt_data 
from .imageshow import fetch_image_by_id
import os
from .useridshow import good
from django.shortcuts import render
from .ocrencrypt import main
from .ocrencrypt import tempcheck, decrypt_data
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def manager_view(request):
    return render(request, 'manager.html', {'manager_id': request.GET.get('manager_id')})

# In views.py
from django.shortcuts import render, redirect

def process_user_id(request, user_id):
    # Logic to handle the submitted user_id
    # Example: print or process the user_id
    print(f"Processing user_id: {user_id}")
    return redirect('some-other-view')  # Redirect after processing


def login_show(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Get manager details using login credentials
            manager = Manager.objects.get(manager_username=username, manager_password=password)
            manager_id = manager.manager_id
            
            # Call the good function to retrieve user IDs
            user_ids = good(manager_id)  # Assumes good() prints IDs

            # Convert the user IDs list to a more manageable format (if needed)
            user_ids = [user_id[0] for user_id in user_ids]

            messages.success(request, "Login successful!")
            
            # Pass both manager_id and user_ids to the template
            return render(request, 'manager.html', {'manager_id': manager_id, 'user_ids': user_ids})

        except Manager.DoesNotExist:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')




def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not Manager.objects.filter(manager_username=username).exists():
            manager = Manager(manager_username=username, manager_password=password)
            manager.save()
            messages.success(request, 'Signup successful!')
            return redirect('login')
        else:
            messages.error(request, 'Username already exists!')
    return render(request, 'signup.html')

def manager_view(request):
    
    return render(request, 'manager.html')






def process_image(request):
    if request.method == 'POST':
        # Retrieve the uploaded file and manager ID
        image_file = request.FILES['image']
        manager_id = request.POST['manager_id']
        
        # Save the uploaded file to a temporary location
        file_path = default_storage.save('temp.jpg', image_file)
        
        # Process the image and extract information (include 'manager_id')
        extracted_info = main(file_path, manager_id)
        
        # Generate a random record ID for encryption
        formatted_record_id = random.randint(1, 10000)
        record_id = f"{formatted_record_id:04}"
        # Call save_information_to_database to save the extracted info, manager_id, and file
        # save_information_to_database(extracted_info, record_id, manager_id, file_path)
        # encrypt_data(record_id)
        # Remove the temporary file after processing
        # os.remove(file_path)
        
        # Redirect or respond with success message
        # return HttpResponse("Image processed, and manager ID saved successfully.")
    
    return redirect('index')




def check_image(request):
    if request.method == 'POST':
        # Retrieve the uploaded file
        image_file = request.FILES['image']

        # Save the uploaded file temporarily
        file_path = default_storage.save('temp.jpg', image_file)
        file_path = default_storage.path(file_path)

        try:
            # Call tempcheck to extract sensitive info
            sensitive_info = tempcheck(file_path)

            # Format the dictionary for display in HTML
            formatted_message = "Sensitive Information Detected:<br>"
            for key, value in sensitive_info.items():
                formatted_message += f"<b>{key}:</b> {value}<br>"

        except Exception as e:
            # Handle exceptions and display error messages
            formatted_message = f"Error: {str(e)}"
        
        # Cleanup: Remove the temporary file
        os.remove(file_path)

        # Return the result as JSON for the frontend
        return JsonResponse({'message': formatted_message}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=400)







def image_show(request):
    user_id = request.GET.get('user_id', None)  # Get the user_id from the URL parameters
    print(user_id)
    
    decrypted_info = decrypt_data(user_id)  # Call the decrypt_data function and store the result in decrypted_info
    print(decrypted_info)
    
    fetch_image_by_id(user_id)  # Ensure this function is defined elsewhere and works correctly
    
    return render(request, 'image.html', {'user_id': user_id, 'decrypt_data': decrypted_info})
