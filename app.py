from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

courses = [
    {   'name':'Flask',
        'courseid':0,
        'description':'Learn about the Flask',
        'price':100
    },
    {   'name':'Python',
        'courseid':1,
        'description':'Learn about the python',
        'price':100
    },
    {   'name':'Django',
        'courseid':2,
        'description':'Learn about the Django',
        'price':150
    },
    {   'name':'PHP',
        'courseid':3,
        'description':'Learn about the PHP',
        'price':80
    },
    {   'name':'AWS',
        'courseid':4,
        'description':'Learn about the AWS Cloud',
        'price':100
    }
]


@app.route('/')
def index():
    return {'Hi': 'Welcome to the FlaskRest AP'}

@app.route('/courses',methods=['GET'])
def get():
    return {'Courses':courses}



@app.route('/courses/<int:c_id>', methods=['GET'])
def get_course_id(c_id):
    data=None
    course = [course for course in courses if course['courseid'] == c_id]
    if len(course) == 0:
        raise exceptions.NotFound()
    else:
        data = {'Course': course[0]}
    return data


@app.route('/createCourse', methods=['GET','POST'])
def create_course():
    data = None
    if request.method == 'POST':
    
        course = {
            'courseid': courses[-1]['courseid'] + 1,
            'name': str(request.data.get('name', '')),
            'description': str(request.data.get('description', '')),
            'price': str(request.data.get('price', ''))
        }
        courses.append(course)
        data = {'res': course}
        return data, status.HTTP_201_CREATED
    else:
        data = {'res':'Please pass data'}
        return data


@app.route('/updateCourse/<int:c_id>', methods=['GET','PUT'])
def uppdate_course(c_id):
    data = None
    if request.method == 'PUT':
        course = [course for course in courses if course['courseid'] == c_id]
        if len(course) == 0:
            raise exceptions.NotFound()
        print(request.data)
        course[0]['name'] = str(request.data.get('name', ''))
        course[0]['description'] = str(request.data.get('description', ''))
        course[0]['price'] = str(request.data.get('price', ''))
        data = {'res': course}
        return data, status.HTTP_201_CREATED
    else:
        data = {'res':'Please pass data'}
        return data

@app.route('/deleteCourse/<int:c_id>', methods=['GET','DELETE'])
def delete_course(c_id):
    if request.method == 'DELETE':
        course = [course for course in courses if course['courseid'] == c_id]
        if len(course) == 0:
            raise exceptions.NotFound()
        
        courses.remove(course[0])
        return '', status.HTTP_204_NO_CONTENT
    else:
        data = {'res':'Please pass data'}
        return data



if __name__ == "__main__":
    app.run(debug=True)
