#users = [] in memory usage


def userexist(userData,cursor):
    #execute sql query

    sql_query = f''' select * from users;
       '''
    try:
        cursor.execute(sql_query)
        users = cursor.fetchall()
    except Exception as error:
        print(error)
    email = userData['email'] #collect user emails
    
    print("Users : ",users)

    for user in users:
        if user[3] == email:
            return {'response': True,'user':user} #email found

    #email not found
    return {'response': False,'user':{}}

        


def registerUser(userData,cursor):
    check = userexist(userData,cursor)

    if(check['response']):
          return {'statuscode': 503,'message':'User Already Exists'}
    else:
         sql_query = f'''
                    INSERT INTO users(name,email,password,contact) VALUES ('{userData['name']}','{userData['email']}','{userData['password']}','{userData['contact']}');
                    '''
         #Executing sql query                   
    try:
        cursor.execute(sql_query)
    except Exception as error:
        print(error)
        
    return {'statuscode': 200,'message':'Registerd Succucsfully Go For Login'}



def loginUser(userData,cursor):

    check = userexist(userData,cursor)

    if(check['response']):

        if userData['password'] == check['user'][4]:
            return {'statuscode': 200,'message':'loggedin'}
        else:
             return {'statuscode': 503,'message':'pwderror'}
    else:
        return {'statuscode': 503,'message':'User Already Exists'}