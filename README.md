# Champions League Web Application 

 

## Project Overview 

 

The UEFA Soccer Database Application is a platform that provides information about soccer teams, including Champions League and domestic leagues such as the Premier League, LaLiga and more. Users can see their team's basic information as well as inputting their team's id # to see their team's domestic league standings and if they are in any European competitions, it will display those as well. 

 

## Usage Guidelines 

 

To interact with the application: 

Navigate to the website. 

Enter any UEFA soccer team.  

Explore teams, ID (used to find teams standings), Stadium (with its capacity), picture of team’s logo as well as stadium. 

Use Team ID to search your selected teams’ standings. 

Explore Teams UEFA and League Standings, with number of points, games played, wins, draws, losses, and goal differential 

 

## Dependencies 

 

- BOOTSTRAP: (https://getbootstrap.com/): Front-end framework for responsive design. 

- API-SPORTS: (https://www.api-sports.io/): API for football-related data. 

- FLASK: A micro web framework for building web applications 

 

## Project Structure 

Front End: 

 

- `index.html`: Main HTML file  

 	- ‘layout html’: 

- ‘standings.html’: 

- ‘team.html’: 

- `styles.css`: Stylesheet for styling the web application. 

 

Back End: 

‘helper.py’ : Fetches information about the UEFA soccer teams such bas, stadiums, standings, logos etc. from the sports API 

‘app.py’ : Acts as the backend of our web application, providing routes to handle user requests, fetch data from helper functions, and render HTML templates to display the information 

MISC: 

.gitignore (Standard) 

README.md (Project information) 

__pycache__ (Fast access data storage) 

 

## Collaboration Information 

 

This project was developed collaboratively with roles as follows: 

- JORDAN HURD: Front-end development, HTML, and CSS. 

-BRANDON POLKE: API integration and JSON data handling. 

 

## Acknowledgments 

 

[API-Sports] (https://www.api-sports.io/) 

[Bootstrap] (https://getbootstrap.com/) 

[ChatGPT} Help with errors and debugging 

 

 

## Reflection 

 

In the initial coding phase, we created HTML files which gave a strong foundation for our web application. However, challenges quickly emerged when we tried to integrate our API to our website. The main issue we were facing was the API's reliance on Team ID for categorizing teams in standings, making it impossible to find team standings based on a Teams name. To fix this, we implanted a function to fetch the Team ID corresponding to the user-inputted team name. We added a user-friendly search bar on the team page, allowing users to input their team ID for direct access to standings information. During website testing, a significant obstacle surfaced concerning teams not engaged in European competitions, leading to an "Out of Range" error. To address this, we developed distinct functions for European teams' domestic data and teams participating in non-European leagues. This approach proved effective, allowing us to display both UEFA and domestic league data for teams involved in both competitions. Simultaneously, it provided comprehensive league data for teams exclusively participating in domestic leagues. This not only resolved the "Out of Range" issue but also enhanced the user experience by delivering data, regardless of a team's involvement in European competitions. We succeeded our own coding expectations and were able to create a robust and user-friendly web application 

 

From a learning perspective, this project provided valuable insights into several key areas. The challenges encountered during the integration of real-time data enhanced our understanding of API interactions and the importance of adaptability in handling unexpected hurdles. The need for a solution to retrieve Team ID based on team names highlighted the significance of thorough API understanding and effective problem-solving. The creation of distinct functions for European and non-European teams demonstrated the importance of tailored solutions for different scenarios, reinforcing our coding skills and strategy development. The iterative process of refining the website based on testing outcomes emphasized the importance of comprehensive testing for diverse use cases and user scenarios. 

ChatGPT played a crucial role in debugging our code, the ability to seek advice and perspectives from ChatGPT facilitated efficient problem-solving and decision-making throughout the development process. Looking forward, the lessons learned from this project will be instrumental in approaching future projects with a more comprehensive understanding of API integrations, user input handling, and effective debugging strategies. The experience gained in creating a user-friendly interface, coupled with back-end functionality, will be applied to enhance the usability and performance of future web applications we plan to create. We are grateful for the knowledge we learnt throughout this process as we have a better understanding on creating web applications for our own endeavors.  In hindsight, a more detailed pre-project plan, especially a thorough examination of API documentation, could have mitigated initial challenges. Understanding the potential pitfalls and preparing for different scenarios would have streamlined the development process. Nonetheless, the learning experience gained from navigating these challenges will undoubtedly contribute to more efficient and successful projects in the future. 