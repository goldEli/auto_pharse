import requests
import json

def get_all_projects(access_token, base_url="https://api.phrase.com/v2"):
    """
    Get all projects from Phrase Strings API with pagination
    
    Args:
        access_token: Phrase API access token
        base_url: Phrase API base URL (default: https://api.phrase.com/v2)
    
    Returns:
        list: List of all projects
    """
    all_projects = []
    page = 1
    per_page = 100  # Maximum allowed per page
    
    headers = {
        'Authorization': f'token {access_token}',
        'User-Agent': 'My Python App (contact@example.com)'  # Required header
    }
    
    while True:
        # Make request to list projects endpoint
        url = f"{base_url}/projects"
        params = {
            'page': page,
            'per_page': per_page
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            projects = response.json()
            
            # If no projects returned, we've reached the end
            if not projects:
                break
                
            all_projects.extend(projects)
            
            # Check if we got fewer projects than requested (last page)
            if len(projects) < per_page:
                break
                
            page += 1
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return all_projects

def get_all_projects_strings(access_token, base_url="https://api.phrase.com/v2"):
    """
    Get all projects from Phrase Strings API with pagination
    (Alias for get_all_projects for backward compatibility)
    
    Args:
        access_token: Phrase API access token
        base_url: Phrase API base URL (default: https://api.phrase.com/v2)
    
    Returns:
        list: List of all projects
    """
    return get_all_projects(access_token, base_url) 