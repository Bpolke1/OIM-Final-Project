from flask import Flask, render_template, request
from helper import get_logo_url, get_teams_name, get_team_id, get_uefateam_standings, get_stadium, get_capacity, get_stadiumimg, get_uefadom_data, get_league_data

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'  

@app.get("/")
def index():
    return render_template("index.html")


@app.post("/team")
def show_team():
    team_name = request.form.get("team")
    logo_url = get_logo_url(team_name)
    name = get_teams_name(team_name)
    team_id = get_team_id(team_name)
    team_stadium = get_stadium(team_name)
    stadium_capacity = get_capacity(team_name)
    stadium_image = get_stadiumimg(team_name)
    return render_template("team.html", logo=logo_url, teams_name=name, teamid=team_id, stadium=team_stadium, capacity=stadium_capacity, stadiumimg=stadium_image )

@app.post("/standings")
def team_standings():
    teams_id = request.form.get("teamid")
    uefa_standings = get_uefateam_standings(teams_id)
    uefadom_data = get_uefadom_data(teams_id)
    league_data = get_league_data(teams_id)
    return render_template("standings.html", uefateamstandings = uefa_standings, uefadom = uefadom_data, leaguedata=league_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
