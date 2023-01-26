# tandem-scenario-builder
An application written in Java using Spark library to help QA teams in Tandem bank organisation in their test management procedures. It can provide usage for roles from business analysts to product owners and any stakeholders (technical and non technical). New functionality is being written as you are reading this documentation and requests for new features can be submitted to martin.bachvarov@tandem.co.uk (product owner, developer and tester for this project). If you feel interested and think that you may benefit from the platform please do not hesisatate to request invitation to our planning sessions. Your feedback is important to the project!

## URL: http://localhost:4567/scenarioBuilder

## Available endpoints

### SCENARIO
---

#### Create scenario
- **path**: /scenario 
- **http method**: POST
- **json body**:
    ```json
    {
      "scenarioId": "8a279193-aafb-428e-be8d-bf93715dd093",
      "name": "Example name",
      "service": 0,
      "description": "Example description",
      "reference": "https://myoplo.atlassian.net"
    }
    ```
 - **description on the payload**:
 
      **scenarioId**:  user must provide random UUID for each scenario, but is not required which mean that the service will generate one.
      
      **name**: name of the test to be stored. Must be atleast 4 character long and is required.
      
      **service**: enumerated value representing service under test. It is required field and currently supports only 0 which stands for Decisioning service. More to be released.
      
      **description**: required field with minimum of two characters lenght. Describing what the test is all about.
      
      **reference**: required field containing url reference to a jira ticket, or a documentation. Must be a url.
      
 - example responses:
 
    201 response:
    ```json
    {
      "scenarioId": "8a279193-aafb-428e-be8d-bf93715dd093"
    }
    ```
    
    400 response:
    ```json
    {
      "success": false,
      "message": "Your request was invalid",
      "errors": "[$.name: must be at least 4 characters long]"
    }
    
    ```


