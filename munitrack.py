"""
MuniTrack Tests
    https://munitrack.vercel.app/

Finding security loopholes in a javascript based web application.
"""
import json
import requests
import asyncio
from issue_generator import main

target_url = "https://munitrack.vercel.app"

issue_data = {
  "issue_image_url": "",
  "issue_title": "",
  "issue_describe": "",
  "issue_location": "Mira Road",
  "issue_manual_location": "Royal College",
  "issue_user_name": "Faizan Alam",
  "issue_user_email": "maxchannel.mailme@gmail.com",
  "issue_public_view": "true"
}

resolution_dict = {
  "state" : "resolved",
  "resolved_on" : "today",
  "resolved_by" : "testing_",
  "resolved_image":"nothing"
}

async def generate_random_issues(number_of_requests: int = 1):
  """ Create's random Issues 
  :param number_of_requests: Number of requests to generate
  """
  for i in range(number_of_requests):
    data_dict = await main(number_of_requests)
    issue_data['issue_image_url'] = ""
    issue_data['issue_title'] = data_dict['title']
    issue_data['issue_describe'] = data_dict['description']
    print(data_dict)
    response = requests.post(target_url+"/backend/issue", json=issue_data, headers={"Content-Type": "application/json"})
    print(f"Issue {i} created with {response.status_code} code")
        
        
def get_all_issues(email: str):
  """Get all issues created by a user
  :param email: Email of the user
  """
  print(f"== All Issuses from user {email} ==")
  response = requests.get(target_url+f"/backend/{email}")
  print(f"Request Status: {response.status_code}")
  print(f"Issues:\n{response.json()}")

  
def resove_issue(issue_id: str, resolve_dict: dict):
  """ Resolve an Issue 
  :param issue_id: Issue ID
  :param resolve_dict: Resolution dictionary
  """
  print(f"== Resolving issue:{issue_id} ==")
  response = requests.put(target_url+f"/backend/issue/resolve/{issue_id}", json=resolve_dict, headers={"Content-Type": "application/json"})
  print(response.status_code)
  print(f"Issue url : {target_url}/issue/{issue_id}")
  
  
        

if __name__ == "__main__":
  asyncio.run(generate_random_issues(6))
  # get_all_issues("maxchannel.mailme@gmail.com")
  resove_issue("6620315219778e744b483ef3", resolution_dict)
