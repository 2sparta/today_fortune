from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.Constellation
db2 = client.animal


# HTML 화면 보여주기
@app.route('/')
def show_main():
    return render_template('index.html')

@app.route('/fortune_con')
def show_con():
    return render_template('index2.html')

@app.route('/fortune_ani')
def show_ani():
    return render_template('index3.html')

@app.route('/constellation_Aquarius')
def constellation_Aquarius():
    return render_template('/Constellation/constellation_Aquarius.html')

@app.route('/constellation_Pisces')
def constellation_Pisces():
    return render_template('/Constellation/constellation_Pisces.html')

@app.route('/constellation_Aries')
def constellation_Aries():
    return render_template('/Constellation/constellation_Aries.html')

@app.route('/constellation_Taurus')
def constellation_Taurus():
    return render_template('/Constellation/constellation_Taurus.html')

@app.route('/constellation_Gemini')
def constellation_Gemini():
    return render_template('/Constellation/constellation_Gemini.html')

@app.route('/constellation_Leo')
def constellation_Leo():
    return render_template('/Constellation/constellation_Leo.html')

@app.route('/constellation_Cancer')
def constellation_Cancer():
    return render_template('/Constellation/constellation_Cancer.html')

@app.route('/constellation_Virgo')
def constellation_Virgo():
    return render_template('/Constellation/constellation_Virgo.html')

@app.route('/constellation_Libra')
def constellation_Libra():
    return render_template('/Constellation/constellation_Libra.html')

@app.route('/constellation_Scorpio')
def constellation_Scorpio():
    return render_template('/Constellation/constellation_Scorpio.html')

@app.route('/constellation_Sagittarius')
def constellation_Sagittarius():
    return render_template('/Constellation/constellation_Sagittarius.html')

@app.route('/constellation_Capricorn')
def constellation_Capricorn():
    return render_template('/Constellation/constellation_Capricorn.html')

@app.route('/animal_mouse')
def animal_mouse():
    return render_template('/animal/animal_mouse.html')

@app.route('/animal_cow')
def animal_cow():
    return render_template('/animal/animal_cow.html')

@app.route('/animal_tiger')
def animal_tiger():
    return render_template('/animal/animal_tiger.html')

@app.route('/animal_rabbit')
def animal_rabbit():
    return render_template('/animal/animal_rabbit.html')

@app.route('/animal_dragon')
def animal_dragon():
    return render_template('/animal/animal_dragon.html')

@app.route('/animal_snake')
def animal_snake():
    return render_template('/animal/animal_snake.html')

@app.route('/animal_horse')
def animal_horse():
    return render_template('/animal/animal_horse.html')

@app.route('/animal_sheep')
def animal_sheep():
    return render_template('/animal/animal_sheep.html')

@app.route('/animal_monkey')
def animal_monkey():
    return render_template('/animal/animal_monkey.html')

@app.route('/animal_chicken')
def animal_chicken():
    return render_template('/animal/animal_chicken.html')

@app.route('/animal_dog')
def animal_dog():
    return render_template('/animal/animal_dog.html')

@app.route('/animal_pig')
def animal_pig():
    return render_template('/animal/animal_pig.html')


@app.route('/special')
def special_thanks():
    return render_template('aboutus.html')


# API 역할을 하는 부분
@app.route('/api/Aquarius', methods=['GET'])
def Aquarius():
    fortune_cons = list(db.fortune.find({'title' : '물병자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Pisces', methods=['GET'])
def Pisces():
    fortune_cons = list(db.fortune.find({'title' : '물고기자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Aries', methods=['GET'])
def Aries():
    fortune_cons = list(db.fortune.find({'title' : '양자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Taurus', methods=['GET'])
def Taurus():
    fortune_cons = list(db.fortune.find({'title' : '황소자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Gemini', methods=['GET'])
def Gemini():
    fortune_cons = list(db.fortune.find({'title' : '쌍둥이자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Cancer', methods=['GET'])
def Cancer():
    fortune_cons = list(db.fortune.find({'title' : '게자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Leo', methods=['GET'])
def Leo():
    fortune_cons = list(db.fortune.find({'title' : '사자자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Virgo', methods=['GET'])
def Virgo():
    fortune_cons = list(db.fortune.find({'title' : '처녀자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Libra', methods=['GET'])
def Libra():
    fortune_cons = list(db.fortune.find({'title' : '천칭자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Scorpio', methods=['GET'])
def Scorpio():
    fortune_cons = list(db.fortune.find({'title' : '전갈자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Sagittarius', methods=['GET'])
def Sagittarius():
    fortune_cons = list(db.fortune.find({'title' : '사수자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Capricorn', methods=['GET'])
def Capricorn():
    fortune_cons = list(db.fortune.find({'title' : '염소자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Mouse', methods=['GET'])
def Mouse():
    fortune_cons = list(db2.fortune.find({'name' : '쥐띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Cow', methods=['GET'])
def Cow():
    fortune_cons = list(db2.fortune.find({'name' : '소띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Tiger', methods=['GET'])
def Tiger():
    fortune_cons = list(db2.fortune.find({'name' : '호랑이띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Rabbit', methods=['GET'])
def Rabbit():
    fortune_cons = list(db2.fortune.find({'name' : '토끼띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Dragon', methods=['GET'])
def Dragon():
    fortune_cons = list(db2.fortune.find({'name' : '용띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Snake', methods=['GET'])
def Snake():
    fortune_cons = list(db2.fortune.find({'name' : '뱀띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Horse', methods=['GET'])
def Horse():
    fortune_cons = list(db2.fortune.find({'name' : '말띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Sheep', methods=['GET'])
def Sheep():
    fortune_cons = list(db2.fortune.find({'name' : '양띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Monkey', methods=['GET'])
def Monkey():
    fortune_cons = list(db2.fortune.find({'name' : '원숭이띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Chicken', methods=['GET'])
def Chicken():
    fortune_cons = list(db2.fortune.find({'name' : '닭띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Dog', methods=['GET'])
def Dog():
    fortune_cons = list(db2.fortune.find({'name' : '개띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Pig', methods=['GET'])
def Pig():
    fortune_cons = list(db2.fortune.find({'name' : '돼지띠' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)