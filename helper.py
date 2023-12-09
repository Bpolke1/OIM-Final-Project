import http.client
from pprint import pprint


def search_team(team_name):
    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/teams"

    querystring = {"name": team_name}

    headers = {
        "X-RapidAPI-Key": "6a1a615483mshcefa2bee821e291p1882e5jsne5fbeb7c6c66",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def get_logo_url(team_name):
    data = search_team(team_name)
    return data["response"][0]["team"]["logo"]

def get_teams_name(team_name):
    data = search_team(team_name)
    return data["response"][0]["team"]["name"]

def get_team_id(team_name):
    data = search_team(team_name)
    return data["response"][0]["team"]["id"]

def get_stadium(team_name):
    data = search_team(team_name)
    return data["response"][0]["venue"]["name"]

def get_capacity(team_name):
    data = search_team(team_name)
    return data["response"][0]["venue"]["capacity"]

def get_stadiumimg(team_name):
    data = search_team(team_name)
    return data["response"][0]["venue"]["image"]




def search_standings(team_id):
    import requests

    url = "https://api-football-v1.p.rapidapi.com/v3/standings"

    querystring = {"season": "2023", "team": team_id}

    headers = {
        "X-RapidAPI-Key": "6a1a615483mshcefa2bee821e291p1882e5jsne5fbeb7c6c66",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def get_uefateam_standings(team_id):
    data = search_standings(team_id)
    if data["response"][0]["league"]["name"] == 'UEFA Champions League':
        uefa_data = {'Standing In UEFA Group' : data["response"][0]["league"]["standings"][0][0]["rank"],
            'Points' : data["response"][0]["league"]["standings"][0][0]["points"],
            'Played' : data['response'][0]['league']['standings'][0][0]['all']['played'],
            'Wins' : data['response'][0]['league']['standings'][0][0]['all']['win'],
            'Draws' : data['response'][0]['league']['standings'][0][0]['all']['draw'],
            'Losses' : data['response'][0]['league']['standings'][0][0]['all']['lose'],
            'Goal Diff' : data['response'][0]['league']['standings'][0][0]['goalsDiff']
        } 
        return uefa_data    
def get_uefadom_data(team_id):
    data = search_standings(team_id)   
    if data["response"][0]["league"]["name"] == 'UEFA Champions League':
            uefadom_data = {
                'League Name' : data["response"][1]["league"]['name'],
                'League Standings' : data["response"][1]["league"]["standings"][0][0]["rank"],
                'Points' : data["response"][1]["league"]["standings"][0][0]["points"],
                'Played' : data['response'][1]['league']['standings'][0][0]['all']['played'],
                'Wins' : data['response'][1]['league']['standings'][0][0]['all']['win'],
                'Draws' : data['response'][1]['league']['standings'][0][0]['all']['draw'],
                'Losses' : data['response'][1]['league']['standings'][0][0]['all']['lose'],
                'Goal Diff' : data['response'][1]['league']['standings'][0][0]['goalsDiff']
            }
            return uefadom_data 
    
def get_league_data(team_id):
    data = search_standings(team_id)
    if data["response"][0]["league"]["name"] != 'UEFA Champions League':
        league_data = {
            'League Name' : data["response"][0]["league"]['name'],
            'League Standings' : data["response"][0]["league"]["standings"][0][0]["rank"],
            'Points' : data["response"][0]["league"]["standings"][0][0]["points"],
            'Played' : data['response'][0]['league']['standings'][0][0]['all']['played'],
            'Wins' : data['response'][0]['league']['standings'][0][0]['all']['win'],
            'Draws' : data['response'][0]['league']['standings'][0][0]['all']['draw'],
            'Losses' : data['response'][0]['league']['standings'][0][0]['all']['lose'],
            'Goal Diff' : data['response'][0]['league']['standings'][0][0]['goalsDiff']
        }
        return league_data



def main():
    """for testing"""
    team = "Barcelona"
    response = search_team(team)
    pprint(response)
    logo_url = get_logo_url(team)
    print(logo_url)
    teams_name = get_teams_name(team)
    print(teams_name)
    team_id = "529"
    response = search_standings(team_id)
    uefa_standings = get_uefateam_standings(team_id)
    pprint(uefa_standings)
    uefadom_data = get_uefadom_data(team_id)
    pprint(uefadom_data)
    league_data = get_league_data(team_id)
    pprint(league_data)
    team_stadium = get_stadium(team)
    print(team_stadium)
    stadium_capacity = get_capacity(team)
    print("Capacity: " + str(stadium_capacity))
    stadium_image = get_stadiumimg(team)
    print(stadium_image)
    
if __name__ == "__main__":
    main()

    
# def get_uefateam_standings(team_id):
#     data = search_standings(team_id)
#     if data["response"][0]["league"]["name"] == 'UEFA Champions League':
#         uefa_data = {
#             'Standing In UEFA Group' : data["response"][0]["league"]["standings"][0][0]["rank"],
#             'Points' : data["response"][0]["league"]["standings"][0][0]["points"],
#             'Played' : data['response'][0]['league']['standings'][0][0]['all']['played'],
#             'Wins' : data['response'][0]['league']['standings'][0][0]['all']['win'],
#             'Draws' : data['response'][0]['league']['standings'][0][0]['all']['draw'],
#             'Losses' : data['response'][0]['league']['standings'][0][0]['all']['lose'],
#             'Goal Diff' : data['response'][0]['league']['standings'][0][0]['goalsDiff']
#         }
#         return uefa_data
#     elif data["response"][0]["league"]["name"] != 'UEFA Champions League':
#         league_data = {
#             'League Name' : data["response"][0]["league"]['name'],
#             'League Standings' : data["response"][0]["league"]["standings"][0][0]["rank"],
#             'Points' : data["response"][0]["league"]["standings"][0][0]["points"],
#             'Played' : data['response'][0]['league']['standings'][0][0]['all']['played'],
#             'Wins' : data['response'][0]['league']['standings'][0][0]['all']['win'],
#             'Draws' : data['response'][0]['league']['standings'][0][0]['all']['draw'],
#             'Losses' : data['response'][0]['league']['standings'][0][0]['all']['lose'],
#             'Goal Diff' : data['response'][0]['league']['standings'][0][0]['goalsDiff']
#         }
#         return league_data

# def get_domestic_standings(team_id):
#     data = search_standings(team_id)
#     if data["response"][0]["league"]["name"] != 'UEFA Champions League':
#         domestic_league_data = {
#             'League Name' : data["response"][0]["league"]['name'],
#             'League Standings' : data["response"][0]["league"]["standings"][0][0]["rank"],
#             'Points' : data["response"][0]["league"]["standings"][0][0]["points"],
#             'Played' : data['response'][0]['league']['standings'][0][0]['all']['played'],
#             'Wins' : data['response'][0]['league']['standings'][0][0]['all']['win'],
#             'Draws' : data['response'][0]['league']['standings'][0][0]['all']['draw'],
#             'Losses' : data['response'][0]['league']['standings'][0][0]['all']['lose'],
#             'Goal Diff' : data['response'][0]['league']['standings'][0][0]['goalsDiff']
#         }
#         return domestic_league_data
#     elif data["response"][0]["league"]["name"] != 'UEFA Champions League':
#         league_data = {
#             'League Name' : data["response"][1]["league"]['name'],
#             'League Standings' : data["response"][1]["league"]["standings"][0][0]["rank"],
#             'Points' : data["response"][1]["league"]["standings"][0][0]["points"],
#             'Played' : data['response'][1]['league']['standings'][0][0]['all']['played'],
#             'Wins' : data['response'][1]['league']['standings'][0][0]['all']['win'],
#             'Draws' : data['response'][1]['league']['standings'][0][0]['all']['draw'],
#             'Losses' : data['response'][1]['league']['standings'][0][0]['all']['lose'],
#             'Goal Diff' : data['response'][1]['league']['standings'][0][0]['goalsDiff']
#         }
#         return league_data
