from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 각 구단의 응원 수를 저장할 딕셔너리
team_support_count = {'team1': 0, 'team2': 0, 'team3': 0}

@app.route('/')
def index():
    return render_template('index.html', teams=team_support_count)

@app.route('/support/<team_name>', methods=['POST'])
def support(team_name):
    # 클라이언트로부터 받은 특정 구단에 대한 응원 클릭
    team_support_count[team_name] += 1
    return jsonify({'success': True, 'count': team_support_count[team_name]})

if __name__ == '__main__':
    app.run(debug=True)
