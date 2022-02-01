from flask import Flask, jsonify, request
from datetime import datetime as dt
import pytz
created_at=''
modified_at=''
app = Flask("myapp")
IST = pytz.timezone('Asia/Kolkata')

tasks=[]
count=1
err = {"error": "Invalid task id"}
emp = {"error":"No task is Present, Db is empty"}

@app.route('/task/<int:n>', methods=['GET','PUT','DELETE'])
def rest(n):   
    if request.method == 'GET':
        if len(tasks)==0:
            return jsonify(emp), 200
        for i in range(len(tasks)):
            if tasks[i]['id']==n:
                return jsonify(tasks[i]), 200        
        return jsonify(err),404

    if request.method == 'DELETE':
        if len(tasks)==0:
            return jsonify(emp), 200
        for i in range(len(tasks)):
            if tasks[i]['id']==n:
                tasks.pop(i)
                return jsonify({"msg":"done"}), 200      
        return jsonify(err), 404

    if request.method == 'PUT':    
        global modified_at
        stamp= dt.now(IST)
        data = request.get_json(force = True) 
        print(data)  
        modified_at= stamp.strftime('%Y-%m-%d-%H-%M-%S')    
        if len(tasks) == 0:
            return jsonify(emp), 200
        for i in range(len(tasks)):
            if tasks[i]['id']==n: 
                tasks[i]["task_name"]=data["task_name"]
                tasks[i]["modified_at"]=modified_at  
                return jsonify(tasks[i]), 200      
        return jsonify(err), 404    

@app.route('/task', methods=['GET','POST'])
def rest2():
        global count
        global created_at
        global modified_at
        x={"msg":"done"}
        y={"msg":"task already present"}
        if request.method == 'GET':
            if len(tasks)==0:
                emp={"error":"No task is Present, Db is empty"}
                return jsonify(emp), 200    
            else:
                return jsonify(tasks) , 200      
        if request.method == 'POST':  
            stamp= dt.now(IST)
            data = request.get_json()
            created_at= stamp.strftime('%Y-%m-%d-%H-%M-%S')
            modified_at= stamp.strftime('%Y-%m-%d-%H-%M-%S')                        
            if len(tasks) == 0:
                count=1
                result={
                    "id":count,
                    "task_name": data["task_name"],
                    "created_at": created_at,
                    "modified_at": modified_at
                    }
                count=count+1 
                tasks.append(result) 
                return jsonify(x) ,201               
            for i in range(len(tasks)):
                if tasks[i]["task_name"]==data["task_name"]:    
                    return jsonify(y), 200
            result={
                "id":count,
                "task_name": data["task_name"],
                "created_at": created_at,
                "modified_at": modified_at
                }
            count=count+1 
            tasks.append(result)  
            return jsonify(x) , 201
        

if __name__ == "__main__":
    app.run(debug=True)
